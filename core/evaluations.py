from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm_evaluator = ChatOpenAI(model="gpt-4-turbo", temperature=0)

EVAL_PROMPT = PromptTemplate.from_template("""
Evaluate the following tutoring interaction.
Topic: {topic}
Student Level: {level}
Student Input: {student_input}
Agent Response: {agent_response}

Criteria:
1. Accuracy (0-10): Is the information correct?
2. Pedagogy (0-10): Did it guide the student or just give the answer?
3. Tone (0-10): Was it encouraging and appropriate for the level?

Return a JSON object: {"accuracy": int, "pedagogy": int, "tone": int, "total": int}
""")

def evaluate_interaction(topic: str, level: str, student_input: str, agent_response: str):
    """
    Runs an automated evaluation of the agent's performance.
    This feeds the 'continuous improvement cycles'
    """
    chain = EVAL_PROMPT | llm_evaluator

    result = chain.invoke({
        "topic": topic,
        "level": level,
        "student_input": student_input,
        "agent_response": agent_response
    })

    # Parse the JSON result (simplified for demo)
    try:
        # In production, use Pydantic output parser
        import json
        parsed = json.loads(result.content)
        return parsed.get("total", 0) / 30.0 # Normalize to 0-1
    except:
        return None
