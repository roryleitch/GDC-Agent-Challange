# MEDIUM (2 stars): a tool that looks things up and handles bad input.
# Fill in the TODOs, add get_landmark_fact to tools=[...], then ask:
# "Tell me something about the Finnieston Crane" and "What about Hogwarts?"

LANDMARKS = {
    "finnieston crane": "A giant cantilever crane on the Clyde, a symbol "
                        "of the city's shipbuilding past.",
    "kelvingrove": "Kelvingrove Art Gallery and Museum - free to visit.",
    "duke of wellington": "The statue outside GoMA, famous for its cone hat.",
    # TODO: add 2 more landmarks (the cloisters? the Necropolis? the Riverside Museum?)
}


def get_landmark_fact(landmark: str) -> dict:
    """Returns a fun fact about a Glasgow landmark.

    Args:
        landmark: Name of the landmark, e.g. "Kelvingrove".

    Returns:
        A dict with status and a fact, or status "error" and a message.
    """
    key = landmark.strip().lower()
    if key in LANDMARKS:
        return {"status": "success", "landmark": landmark,
                "fact": LANDMARKS[key]}
    # TODO: return a helpful error dict listing the known landmarks
    return {"status": "error", "error_message": "..."}
