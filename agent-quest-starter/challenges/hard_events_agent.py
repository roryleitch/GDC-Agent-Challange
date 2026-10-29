# HARD (3 stars): add a NEW specialist sub-agent to the Boss level.
# Work in glasgow_guide/agent.py:
# 1. Paste the tool + agent below (above root_agent).
# 2. Add events_agent to root_agent's sub_agents=[...].
# 3. Update the root instruction so it hands "what's on" questions over.
# Bonus: add a `day: str` parameter and return different mock events per day.
from google.adk.agents import Agent


def whats_on(area: str) -> dict:
    """Lists (fictional) student events happening in a Glasgow area.

    Args:
        area: A Glasgow neighbourhood, e.g. "West End".

    Returns:
        A dict with status and a list of mock events.
    """
    return {
        "status": "success",
        "area": area,
        "events": [
            {"name": "Ceilidh Night (beginners welcome)", "time": "19:30"},
            {"name": "Pixel Art Meetup", "time": "18:00"},
        ],
        "note": "Demo data - these events are fictional.",
    }


events_agent = Agent(
    model="gemini-flash-latest",
    name="events_agent",
    description="Finds student-friendly events and things to do in Glasgow.",
    instruction="You suggest things to do in Glasgow. Always use whats_on.",
    tools=[whats_on],
)
