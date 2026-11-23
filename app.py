def classify(text: str) -> str:
    """Toy model: flags a message as urgent or normal."""
    urgent_words = ["urgent", "court", "today"]
    return "urgent" if any(w in text.lower() for w in urgent_words) else "normal"