"""
Custom authentication classes for LearnLoop API
"""
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone
from datetime import timedelta


class ExpiringTokenAuthentication(TokenAuthentication):
    """Token authentication with automatic expiration"""

    def authenticate_credentials(self, key):
        """Authenticate with token expiration check"""

        return token.user, token
