"""Weegie Bot - Agent Quest: Glasgow Edition (Levels 4 + 5).

A friendly Glasgow guide agent with three MOCKED tools.
No extra API keys needed: every tool returns made-up demo data.
"""
from google.adk.agents import Agent

# ---------------------------------------------------------------- TOOLS --
# A tool is just a Python function. ADK reads the name, the type hints
# and the docstring, and tells the model when and how to call it.


def get_glasgow_weather(area: str) -> dict:
    """Gets the current weather for an area of Glasgow.

    Args:
        area: A Glasgow neighbourhood, e.g. "West End", "Merchant City".

    Returns:
        A dict with status, area, forecast and a top tip.
    """
    # Mock data. Spoiler: it's raining.
    return {
        "status": "success",
        "area": area,
        "forecast": "Light rain, 11C, chance of a sunny spell around 3pm",
        "umbrella_needed": True,
        "tip": "Bring a jacket. And a backup jacket.",
    }


SUBWAY_STATIONS = [
    "Buchanan Street", "St Enoch", "Bridge Street", "West Street",
    "Shields Road", "Kinning Park", "Cessnock", "Ibrox", "Govan",
    "Partick", "Kelvinhall", "Hillhead", "Kelvinbridge",
    "St George's Cross", "Cowcaddens",
]


def next_subway_train(station: str, circle: str = "outer") -> dict:
    """Gets the next Glasgow Subway train from a station (mock timetable).

    Args:
        station: Subway station name, e.g. "Hillhead".
        circle: "inner" (anticlockwise) or "outer" (clockwise).

    Returns:
        A dict with status and minutes until the next train, or an error.
    """
    match = next((s for s in SUBWAY_STATIONS
                  if s.lower() == station.strip().lower()), None)
    if match is None:
        return {
            "status": "error",
            "error_message": f"'{station}' is not a Subway station.",
            "valid_stations": SUBWAY_STATIONS,
        }
    minutes = len(match) % 6 + 1  # deterministic fake timetable
    return {
        "status": "success",
        "station": match,
        "circle": circle.lower(),
        "next_train_in_minutes": minutes,
    }


def find_munchies(area: str, craving: str = "chips") -> dict:
    """Suggests a (made-up) place to eat in a Glasgow area.

    Args:
        area: A Glasgow neighbourhood, e.g. "Finnieston".
        craving: What the user fancies, e.g. "chips", "curry", "vegan".

    Returns:
        A dict with status and a list of fictional suggestions.
    """
    return {
        "status": "success",
        "area": area,
        "craving": craving,
        "suggestions": [
            {"name": f"The Wee {craving.title()} Shop", "walk_minutes": 4},
            {"name": "Clydeside Kitchen", "walk_minutes": 9},
        ],
        "note": "Demo data - these places are fictional.",
    }


# ---------------------------------------------------------------- AGENT --
root_agent = Agent(
    model="gemini-3.1-flash-lite",
    name="weegie_bot",
    description="A friendly Glasgow guide for students.",
    instruction=(
        "You are Weegie Bot, a warm, upbeat guide to Glasgow for university "
        "students. Use a light sprinkle of Scots words (aye, wee, braw, "
        "gonnae) but keep answers clear for everyone. Keep replies short. "
        "Use get_glasgow_weather for weather questions, next_subway_train for "
        "Subway questions and find_munchies for food. If a tool returns an "
        "error, explain it kindly and suggest a fix. Never invent tool data."
    ),
    tools=[get_glasgow_weather, next_subway_train, find_munchies],
)
