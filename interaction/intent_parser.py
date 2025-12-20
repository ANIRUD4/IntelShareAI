class IntentParser:
    """
    Converts raw text into high-level intent.
    """

    def parse(self, text: str) -> str:
        text = text.lower()

        if "learn" in text:
            return "LEARN"

        if "what is this" in text or "identify" in text:
            return "INFER"

        if text in ["yes", "correct", "right"]:
            return "CONFIRM_YES"

        if text in ["no", "wrong"]:
            return "CONFIRM_NO"

        return "UNKNOWN"
