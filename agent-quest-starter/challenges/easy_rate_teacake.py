# EASY (1 star): add a tool with a fixed answer.
# 1. Paste this function into weegie_bot/agent.py (above root_agent).
# 2. Add rate_teacake to the tools=[...] list.
# 3. Restart `adk web` and ask: "Rate a teacake for me!"


def rate_teacake(snack: str) -> dict:
    """Rates a Scottish snack out of 10.

    Args:
        snack: The snack to rate, e.g. "teacake", "caramel wafer".

    Returns:
        A dict with status, snack, score and a verdict.
    """
    return {
        "status": "success",
        "snack": snack,
        "score": 10,  # TODO: make this depend on the snack!
        "verdict": "Pure dead brilliant.",
    }
