"""Boss level - a multi-agent Glasgow guide.

A root "guide" agent hands questions to specialist sub-agents.
ADK uses each sub-agent's `description` to decide who gets the question.
"""
from google.adk.agents import Agent

MODEL = "gemini-3.1-flash-lite"


def get_glasgow_weather(area: str) -> dict:
    """Gets the current weather for an area of Glasgow (mock data)."""
    return {"status": "success", "area": area,
            "forecast": "Drizzle, 10C. Classic.", "umbrella_needed": True}


def find_munchies(area: str, craving: str = "chips") -> dict:
    """Suggests a fictional place to eat in a Glasgow area (mock data)."""
    return {"status": "success", "area": area,
            "suggestions": [f"The Wee {craving.title()} Shop",
                            "Clydeside Kitchen"],
            "note": "Demo data - these places are fictional."}


weather_agent = Agent(
    model=MODEL,
    name="weather_agent",
    description="Answers Glasgow weather questions.",
    instruction="You report Glasgow weather. Always use get_glasgow_weather.",
    tools=[get_glasgow_weather],
)

food_agent = Agent(
    model=MODEL,
    name="food_agent",
    description="Recommends places to eat in Glasgow.",
    instruction="You suggest food in Glasgow. Always use find_munchies.",
    tools=[find_munchies],
)

root_agent = Agent(
    model=MODEL,
    name="glasgow_guide",
    description="Main Glasgow guide that routes questions to specialists.",
    instruction=(
        "You are the Glasgow Guide. Greet the user warmly. "
        "Weather questions go to weather_agent, "
        "food questions go to food_agent. "
        "Answer anything else yourself, briefly."
    ),
    sub_agents=[weather_agent, food_agent],
)
