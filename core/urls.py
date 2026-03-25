"""
Core app URL configuration for LearnLoop
Agentic AI Learning Platform - API Endpoints
"""
from django.urls import path
from .views import (
    ChatInteractionView,
    SessionDetailView,
    SessionListView,
    MetricsView,
    LearnerProfileView,
    EvaluationReportView,
)

app_name = 'core'

urlpatterns = [
    # =============================================================================
    # LEARNING SESSIONS
    # =============================================================================
    path('sessions/', SessionListView.as_view(), name='session-list'),
    path('sessions/<uuid:pk>/', SessionDetailView.as_view(), name='session-detail'),

    # =============================================================================
    # INTERACTIONS (Chat with Agent)
    # =============================================================================
    path('interactions/', ChatInteractionView.as_view(), name='interaction-create'),
    path('interactions/<uuid:pk>/', ChatInteractionView.as_view(), name='interaction-detail'),

    # =============================================================================
    # METRICS & MONITORING
    # =============================================================================
    path('metrics/', MetricsView.as_view(), name='metrics'),
    path('metrics/summary/', MetricsView.as_view({'get': 'summary'}), name='metrics-summary'),

    # =============================================================================
    # LEARNER PROFILES
    # =============================================================================
    path('learners/<uuid:pk>/', LearnerProfileView.as_view(), name='learner-profile'),
    path('learners/<uuid:pk>/history/', LearnerProfileView.as_view({'get': 'history'}), name='learner-history'),

    # =============================================================================
    # EVALUATION REPORTS
    # =============================================================================
    path('evaluations/', EvaluationReportView.as_view(), name='evaluation-list'),
    path('evaluations/<uuid:pk>/', EvaluationReportView.as_view({'get': 'detail'}), name='evaluation-detail'),
    path('evaluations/aggregate/', EvaluationReportView.as_view({'get': 'aggregate'}), name='evaluation-aggregate'),
]
