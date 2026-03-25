from django.shortcuts import render

"""
API Views for LearnLoop
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import LearningSession, InteractionLog, Learner
from .tasks import process_learning_interaction
from .evaluation import evaluate_interaction



class SessionListView(APIView):
    permission_classes = [IsAuthenticated]




class SessionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Retrieve specific session details"""

            return Response({"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND)


class ChatInteractionView(APIView):
    permission_classes = [IsAuthenticated]



class MetricsView(APIView):
    permission_classes = [IsAuthenticated]



class LearnerProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Retrieve learner profile"""
        try:
            learner = Learner.objects.get(pk=pk)
            serializer = LearnerSerializer(learner)
            return Response(serializer.data)
        except Learner.DoesNotExist:
            return Response({"error": "Learner not found"}, status=status.HTTP_404_NOT_FOUND)



class EvaluationReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """List all evaluation reports"""
        evaluations = InteractionLog.objects.exclude(evaluation_score__isnull=True)
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)

    def aggregate(self, request):
        """Get aggregate evaluation statistics"""

        )
        return Response(stats)
