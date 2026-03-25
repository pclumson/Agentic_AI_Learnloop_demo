from celery import shared_task
from .models import InteractionLog, LearningSession
from .agents import invoke_agent
from .evaluation import evaluate_interaction

@shared_task
def process_learning_interaction(session_id: int, user_input: str):
    """
    Background task to:
    1. Invoke the agent
    2. Log the interaction
    3. Run evaluation
    4. Update session metrics
    """
    session = LearningSession.objects.get(id=session_id)
    learner = session.learner

    # Prepare profile
    profile = {
        "skill_level": learner.skill_level,
        "topic": session.topic,
        "context": "Previous interactions..." # Fetch from DB in real app
    }

    # 1. Invoke Agent
    result = invoke_agent(session.id, user_input, profile)

    if "error" in result:
        return {"status": "error", "message": result["error"]}

    # 2. Log Interaction
    log = InteractionLog.objects.create(
        session=session,
        user_input=user_input,
        agent_response=result["response"],
        agent_trace=result["trace"]
    )

    # 3. Evaluate (Async evaluation to avoid blocking)
    score = evaluate_interaction(
        topic=session.topic,
        level=learner.skill_level,
        student_input=user_input,
        agent_response=result["response"]
    )

    if score is not None:
        log.evaluation_score = score
        log.save()

    return {"status": "success", "response": result["response"], "score": score}
