from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os

# Initialize LLM (In production, use environment variables)
os.environ["OPENAI_API_KEY"] = "your-api-key"
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.7)

def create_tutor_agent(learner_profile: dict):
    """
    Creates a dynamic agent chain based on the learner's profile.
    This demonstrates 'agent orchestration' and 'personalization'.
    """

    system_prompt = f"""
    You are an expert AI Tutor for a {learner_profile['skill_level']} student.
    Topic: {learner_profile['topic']}

    Rules:
    1. Adapt your explanation style to the student's level.
    2. Ask clarifying questions if the student seems confused.
    3. Do not give the answer immediately; guide them to discover it.
    4. Keep responses under 150 words.

    Current Context:
    {learner_profile['context']}
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])

    chain = (
        {"input": RunnablePassthrough(), "chat_history": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

def invoke_agent(session_id: int, user_input: str, learner_profile: dict):
    """
    Orchestrates the agent call and returns the response + trace metadata.
    """
    chain = create_tutor_agent(learner_profile)

    # In a real app, you'd fetch chat history from DB here
    chat_history = []

    try:
        response = chain.invoke({
            "input": user_input,
            "chat_history": chat_history
        })

        # Simulate trace metadata for evaluation
        trace_data = {
            "tokens_used": 150, # Mock metric
            "latency_ms": 450,  # Mock metric
            "model": "gpt-4-turbo"
        }

        return {
            "response": response,
            "trace": trace_data
        }
    except Exception as e:
        return {"error": str(e), "trace": {}}
