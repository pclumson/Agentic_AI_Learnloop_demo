from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LearningSession
from .tasks import process_learning_interaction

class ChatInteractionView(APIView):
    def post(self, request):
        session_id = request.data.get('session_id')
        user_input = request.data.get('input')

        if not session_id or not user_input:
            return Response({"error": "Missing session_id or input"}, status=status.HTTP_400_BAD_REQUEST)

        # Trigger async task
        task = process_learning_interaction.delay(session_id, user_input)

        return Response({
            "message": "Processing...",
            "task_id": task.id,
            "status": "queued"
        }, status=status.HTTP_202_ACCEPTED)
