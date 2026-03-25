"""
Custom middleware for LearnLoop API
Handles authentication, rate limiting, and request logging
"""
import logging
import time
from django.conf import settings
from django.core.cache import cache
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed, Throttled

logger = logging.getLogger(__name__)


class APILoggingMiddleware:
    """Logs all API requests for monitoring and debugging"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip logging for health checks
        if request.path == '/api/health/':
            return self.get_response(request)

        # Log request start
        start_time = time.time()
        logger.info(
            f"REQUEST_START: {request.method} {request.path} "
            f"user={request.user.id if request.user.is_authenticated else 'anonymous'}"
        )

        # Process request
        response = self.get_response(request)

        # Log request completion
        duration = time.time() - start_time
        logger.info(
            f"REQUEST_END: {request.method} {request.path} "
            f"status={response.status_code} duration={duration:.3f}s"
        )

        return response


class RateLimitMiddleware:
    """Simple rate limiting based on IP address"""

    def __init__(self, get_response):
        self.get_response = get_response
        self.limit = getattr(settings, 'RATE_LIMIT_REQUESTS', 100)
        self.window = getattr(settings, 'RATE_LIMIT_WINDOW', 3600)  # 1 hour

    def __call__(self, request):
        # Skip rate limiting for authenticated users (they have DRF throttling)
        if request.user.is_authenticated:
            return self.get_response(request)

        # Get client IP
        client_ip = self.get_client_ip(request)
        cache_key = f"rate_limit:{client_ip}"

        # Check rate limit
        request_count = cache.get(cache_key, 0)

        if request_count >= self.limit:
            logger.warning(f"RATE_LIMIT_EXCEEDED: {client_ip}")
            raise Throttled(detail="Too many requests. Please try again later.")

        # Increment counter
        cache.set(cache_key, request_count + 1, self.window)

        return self.get_response(request)

    def get_client_ip(self, request):
        """Extract client IP from request"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class SecurityHeadersMiddleware:
    """Adds security headers to all responses"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Add security headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response['Content-Security-Policy'] = "default-src 'self'"

        return response


class AgentTraceMiddleware:
    """Tracks agent invocation metrics for monitoring"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Track agent-related requests
        if '/api/v1/interactions/' in request.path:
            request._agent_start_time = time.time()

        response = self.get_response(request)

        # Log agent metrics
        if hasattr(request, '_agent_start_time'):
            duration = time.time() - request._agent_start_time
            logger.info(
                f"AGENT_INVOCATION: {request.path} duration={duration:.3f}s "
                f"status={response.status_code}"
            )

            # Store in cache for metrics aggregation
            cache_key = f"agent_metrics:{int(time.time())}"
            current = cache.get(cache_key, {'count': 0, 'total_duration': 0})
            cache.set(
                cache_key,
                {
                    'count': current['count'] + 1,
                    'total_duration': current['total_duration'] + duration
                },
                3600  # 1 hour TTL
            )

        return response
