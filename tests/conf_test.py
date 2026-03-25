"""
Pytest configuration and fixtures
"""
import pytest
import os
import django

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnloop.settings')
django.setup()


@pytest.fixture
def sample_learner_profile():
    """Fixture for reusable learner profile"""
    return {
        'skill_level': 'intermediate',
        'topic': 'Python Programming',
        'context': 'Has basic programming knowledge'
    }


@pytest.fixture
def sample_interaction():
    """Fixture for reusable interaction data"""
    return {
        'user_input': 'What is a list comprehension?',
        'agent_response': 'List comprehension is a concise way to create lists.',
        'topic': 'Python Basics',
        'level': 'beginner'
    }


@pytest.fixture
def mock_llm_response():
    """Fixture for mocked LLM responses"""
    return {
        'response': 'Test response from agent',
        'trace': {
            'tokens_used': 150,
            'latency_ms': 450,
            'model': 'gpt-4-turbo'
        }
    }
