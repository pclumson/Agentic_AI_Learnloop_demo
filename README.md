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

---

## 🏗️ Architecture


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
