"""
Tests for evaluation framework
"""
import pytest
from unittest.mock import patch, MagicMock
from core.evaluation import evaluate_interaction, EVAL_PROMPT


class TestEvaluationFramework:
    """Test automated scoring system"""

    @patch('core.evaluation.llm_evaluator.invoke')
    def test_evaluate_interaction_returns_score(self, mock_invoke):
        """Test evaluation returns normalized score"""
        mock_invoke.return_value = MagicMock(content='{"accuracy": 9, "pedagogy": 8, "tone": 9, "total": 26}')

        topic = "Python Basics"
        level = "beginner"
        student_input = "What is a variable?"
        agent_response = "A variable is a container for storing data values."

        score = evaluate_interaction(topic, level, student_input, agent_response)

        assert score is not None
        assert 0 <= score <= 1  # Normalized to 0-1

    @patch('core.evaluation.llm_evaluator.invoke')
    def test_evaluate_interaction_handles_parse_error(self, mock_invoke):
        """Test evaluation handles JSON parse errors gracefully"""
        mock_invoke.return_value = MagicMock(content='invalid json')

        topic = "Python"
        level = "beginner"
        student_input = "Test"
        agent_response = "Test response"

        score = evaluate_interaction(topic, level, student_input, agent_response)

        assert score is None  # Returns None on parse failure

    @patch('core.evaluation.llm_evaluator.invoke')
    def test_evaluation_criteria_weighting(self, mock_invoke):
        """Test that all three criteria are weighted equally"""
        mock_invoke.return_value = MagicMock(content='{"accuracy": 10, "pedagogy": 10, "tone": 10, "total": 30}')

        topic = "Python"
        level = "beginner"
        student_input = "Question"
        agent_response = "Answer"

        score = evaluate_interaction(topic, level, student_input, agent_response)

        # Perfect score should be 1.0 (30/30)
        assert score == 1.0

    @patch('core.evaluation.llm_evaluator.invoke')
    def test_evaluation_catches_low_quality_responses(self, mock_invoke):
        """Test evaluation identifies poor pedagogical approaches"""
        mock_invoke.return_value = MagicMock(content='{"accuracy": 10, "pedagogy": 2, "tone": 5, "total": 17}')

        topic = "Python"
        level = "beginner"
        student_input = "How do I solve this problem?"
        agent_response = "The answer is 42."  # Just gives answer, no guidance

        score = evaluate_interaction(topic, level, student_input, agent_response)

        # Low pedagogy score should result in lower overall score
        assert score < 0.6


class TestEvaluationIntegration:
    """Integration tests for evaluation pipeline"""

    @patch('core.evaluation.llm_evaluator.invoke')
    def test_evaluation_with_realistic_interaction(self, mock_invoke):
        """Test evaluation with realistic tutoring scenario"""
        mock_invoke.return_value = MagicMock(
            content='{"accuracy": 9, "pedagogy": 8, "tone": 9, "total": 26}'
        )

        topic = "Object-Oriented Programming"
        level = "intermediate"
        student_input = "Can you explain inheritance with an example?"
        agent_response = """
        Inheritance lets one class reuse another class's code.
        For example, a Dog class can inherit from Animal class:

        class Animal:
            def breathe(self):
                print("Breathing")

        class Dog(Animal):
            def bark(self):
                print("Woof!")

        Now Dog has both breathe() and bark() methods.
        """

        score = evaluate_interaction(topic, level, student_input, agent_response)

        assert score is not None
        assert score > 0.7  # Good pedagogical example
