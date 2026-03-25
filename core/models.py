from django.db import models

# Create your models here.
from django.db import models
import uuid

class Learner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    skill_level = models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class LearningSession(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=[('active', 'Active'), ('completed', 'Completed'), ('failed', 'Failed')], max_length=20, default='active')

class InteractionLog(models.Model):
    session = models.ForeignKey(LearningSession, on_delete=models.CASCADE, related_name='interactions')
    timestamp = models.DateTimeField(auto_now_add=True)
    user_input = models.TextField()
    agent_response = models.TextField()
    agent_trace = models.JSONField(default=dict) # Stores LangChain trace/metrics
    evaluation_score = models.FloatField(null=True, blank=True) # Score from evaluation framework

    class Meta:
        ordering = ['-timestamp']
