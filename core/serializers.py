"""
Serializers for LearnLoop API
"""

"""
Serializers for LearnLoop API
Handles data validation and transformation for all models
"""
from rest_framework import serializers
from django.utils import timezone
from .models import Learner, LearningSession, InteractionLog
from .agents import create_tutor_agent
from .evaluation import evaluate_interaction





#
#
# from rest_framework import serializers
# from .models import Learner, LearningSession, InteractionLog
#
#
# class LearnerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Learner
#         fields = ['id', 'name', 'skill_level', 'created_at']
#
#
# class SessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LearningSession
#         fields = ['id', 'learner', 'topic', 'started_at', 'ended_at', 'status']
#         read_only_fields = ['started_at']
#
#
# class InteractionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InteractionLog
#         fields = [
#             'id', 'session', 'timestamp', 'user_input',
#             'agent_response', 'agent_trace', 'evaluation_score'
#         ]
#         read_only_fields = ['timestamp', 'agent_trace', 'evaluation_score']
#
#
# class EvaluationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InteractionLog
#         fields = ['id', 'timestamp', 'evaluation_score', 'agent_trace']
