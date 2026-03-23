# Agentic_AI_Learnloop_demo
Uses LangChain to create a dynamic tutor agent that adapts to learner profiles.


# Project keys Functionalities :
# Agentic Backend:
Uses LangChain to create a dynamic tutor agent that adapts to learner profiles.
# Scalable API
Built with Django REST Framework; uses Celery for async processing to handle load.
# Data Pipelines
Logs every interaction
(InteractionLog) with traces and scores for downstream analysis.
# Evaluation Frameworks
Includes evaluate_interaction() to score agent performance automatically (Accuracy, Pedagogy).
#Real-time Analysis
The agent_trace field captures latency and token usage for performance monitoring.
# Python at Scale
Modular architecture separating logic (agents), data (models), and async tasks (Celery).
# AWS Readiness	
This structure maps directly to AWS Lambda (for tasks), DynamoDB (for logs), and SQS (for queues).
