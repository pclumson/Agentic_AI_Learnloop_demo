# Agentic_AI_Learnloop_demo
Uses LangChain to create a dynamic tutor agent that adapts to learner profiles.

# 🎓 LearnLoop - Agentic AI Learning Platform

> A Django-based backend demonstrating agentic AI orchestration, evaluation frameworks, and real-time learner interaction analysis for personalized education.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Evaluation Framework](#evaluation-framework)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**LearnLoop** is a production-ready backend architecture for AI-powered learning platforms. It demonstrates how to build scalable agentic AI systems that:

- **Adapt dynamically** to individual learner skill levels
- **Orchestrate multiple AI agents** for personalized tutoring
- **Measure effectiveness** through automated evaluation frameworks
- **Enable continuous improvement** via interaction data pipelines

This project was designed to showcase backend engineering patterns for AI learning platforms, with direct applicability to enterprise-scale educational technology.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **🤖 Agent Orchestration** | LangChain-based tutor agents that adapt to beginner/intermediate/advanced learner profiles |
| **📊 Evaluation Framework** | Automated scoring system measuring accuracy, pedagogy, and tone (0-1 normalized) |
| **⚡ Async Processing** | Celery + Redis for non-blocking agent invocation and real-time interaction handling |
| **📈 Metrics Collection** | Token usage, latency tracking, and model performance monitoring per interaction |
| **🗄️ Data Logging** | PostgreSQL models storing interactions, traces, and evaluation scores for downstream analysis |
| **🔒 Secure APIs** | Django REST Framework with authentication and secure transport methodologies |


## 🏗️ Architecture

<img width="1218" height="678" alt="archi" src="https://github.com/user-attachments/assets/a5294e88-aa73-4b39-ae46-448c2060b4e9" />





## 🛠️ Tech Stack

|Category | Technology |
|---------|-------------|
| **🤖 Backend Framework** |Django 4.2+, Django REST Framework |
| **📊AI/MLk** | LangChain 0.1+, OpenAI API |
| **⚡ Async Processing** | Celery + Redis for non-blocking agent invocation and real-time interaction handling |
| **📈 Database** |Postgresql |
| **🗄️ Containerizatio** |Docker, Docker Compose |
| **🔒 Secure APIs** | Django REST Framework with authentication and secure transport methodologies |
| ** CI/CD **|  GitHub Actions |
| ** Monitoring ** | Custom logging with trace metadata |


## 📦 Installation
Prerequisites

    Python 3.10+
    PostgreSQL 14+
    Redis 7+
    Docker (optional, for containerized deployment)

Quick Start

# Clone the repository
git clone https://github.com/pclumson/Agentic_AI_Learnloop_demo.git
cd Agentic_AI_Learnloop_demo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys and database credentials

# Run migrations
python manage.py migrate

# Start Redis (if not running)
redis-server

# Start Celery worker
celery -A learnloop worker --loglevel=info

# Start Django development server
python manage.py runserver

Docker Deployment

docker-compose up --build

🔌 API Documentation
Endpoints
Method	Endpoint	Description
POST	/api/v1/sessions/	Create new learning session
GET	/api/v1/sessions/<id>/	Retrieve session details
POST	/api/v1/interactions/	Submit learner input for agent response
GET	/api/v1/interactions/<id>/	Retrieve interaction with evaluation score
GET	/api/v1/metrics/	Get aggregated performance metrics
Example Request

curl -X POST http://localhost:8000/api/v1/interactions/ \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "abc123-def456",
    "input": "Can you explain how neural networks work?",
    "learner_id": "learner-789"
  }'

Example Response

{
  "message": "Processing...",
  "task_id": "celery-task-uuid-12345",
  "status": "queued",
  "estimated_latency_ms": 500
}

📊 Evaluation Framework

The evaluation framework automatically scores each agent interaction across three dimensions:
Metric	Description	Weight
Accuracy	Is the information factually correct?	33%
Pedagogy	Does it guide discovery vs. giving answers?	33%
Tone	Is it encouraging and level-appropriate?	33%
Evaluation Flow

User Input → Agent Response → Evaluation LLM → Score (0-1) → Stored in DB
                                                              ↓
                                                    Continuous Improvement Loop

Sample Evaluation Output

{
  "interaction_id": "int-uuid-67890",
  "scores": {
    "accuracy": 0.9,
    "pedagogy": 0.8,
    "tone": 0.95
  },
  "total_score": 0.88,
  "feedback": "Strong pedagogical approach with accurate content."
}

🚀 Deployment
AWS Architecture Mapping

This codebase is designed to map directly to AWS services:
Component	AWS Equivalent
Django API	AWS Lambda + API Gateway
Celery Queue	Amazon SQS
PostgreSQL	Amazon RDS or Aurora
Redis	Amazon ElastiCache
Interaction Logs	Amazon DynamoDB
Evaluation Data	Amazon S3 + Athena
Environment Variables

# Required
OPENAI_API_KEY=your-api-key
DATABASE_URL=postgres://user:pass@host:5432/dbname
REDIS_URL=redis://localhost:6379/0

# Optional
DJANGO_ENV=production
CELERY_WORKERS=4
LOG_LEVEL=INFO

📈 Metrics & Monitoring

The system tracks the following metrics for each interaction:

    Latency: Time from request to agent response
    Token Usage: Input/output tokens consumed
    Evaluation Score: Pedagogical quality rating
    Error Rate: Failed invocations per session

These metrics enable the Data Science team to:

    Identify underperforming agents
    Track personalization effectiveness
    Optimize infrastructure costs
    Guide continuous improvement cycles

🧪 Testing

# Run unit tests
pytest

# Run integration tests
pytest tests/integration/

# Run with coverage
pytest --cov=.

🤝 Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository
    Create a feature branch (git checkout -b feature/amazing-feature)
    Commit your changes (git commit -m 'Add amazing feature')
    Push to the branch (git push origin feature/amazing-feature)
    Open a Pull Request

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
👤 Author

Prince Clumson-Eklu

    Email: 
    GitHub: @pclumson
    LinkedIn: linkedin.com/in/prince_clumson-eklu

🔗 Related Projects

    dj-apis-allauth - Django REST API with AllAuth
    Smart Health App - Java database capstone
    C++ Crypto Trading App

📞 Contact

For questions or collaboration opportunities, please reach out via email or open an issue on GitHub.

Built with ❤️ for human-centered learning in the age of AI




