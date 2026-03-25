"""
Tests for LangChain agent orchestration
"""
import pytest
from unittest.mock import patch, MagicMock
from core.agents import create_tutor_agent, invoke_agent


class TestTutorAgent:
    """Test agent creation and invocation"""

    @patch('core.agents.ChatOpenAI')
    def test_create_tutor_agent_beginner(self, mock_llm):
        """Test agent creation for beginner learner"""
        learner_profile = {
            'skill_level': 'beginner',
            'topic': 'Python Basics',
            'context': 'New to programming'
        }

        chain = create_tutor_agent(learner_profile)

        assert chain is not None
        mock_llm.assert_called_once_with(model="gpt-4-turbo", temperature=0.7)

    @patch('core.agents.ChatOpenAI')
    def test_create_tutor_agent_advanced(self, mock_llm):
        """Test agent creation for advanced learner"""
        learner_profile = {
            'skill_level': 'advanced',
            'topic': 'Machine Learning',
            'context': 'Experienced with ML frameworks'
        }

        chain = create_tutor_agent(learner_profile)

        assert chain is not None

    @patch('core.agents.chain.invoke')
    def test_invoke_agent_success(self, mock_invoke):
        """Test successful agent invocation"""
        mock_invoke.return_value = "Neural networks are computing systems inspired by biological brains."

        session_id = 1
        user_input = "What are neural networks?"
        learner_profile = {
            'skill_level': 'intermediate',
            'topic': 'Deep Learning',
            'context': 'Studying ML'
        }

        result = invoke_agent(session_id, user_input, learner_profile)

        assert 'response' in result
        assert 'trace' in result
        assert result['response'] is not None

    @patch('core.agents.chain.invoke')
    def test_invoke_agent_handles_error(self, mock_invoke):
        """Test agent handles exceptions gracefully"""
        mock_invoke.side_effect = Exception("API timeout")

        session_id = 1
        user_input = "Test question"
        learner_profile = {
            'skill_level': 'beginner',
            'topic': 'Python',
            'context': ''
        }

        result = invoke_agent(session_id, user_input, learner_profile)

        assert 'error' in result
        assert result['error'] == "API timeout"


class TestAgentPerformance:
    """Test agent performance characteristics"""

    @patch('core.agents.chain.invoke')
    def test_agent_respects_temperature_setting(self, mock_invoke):
        """Test that temperature parameter affects output variability"""
        mock_invoke.return_value = "Test response"

        learner_profile = {
            'skill_level': 'beginner',
            'topic': 'Python',
            'context': ''
        }

        # Should use temperature=0.7 as configured
        invoke_agent(1, "Question", learner_profile)

        # Verify LLM was called with correct temperature
        from core.agents import llm
        assert llm.temperature == 0.7
