"""Small string helpers, used as a work item for the sandbox agent."""


def slugify(title: str) -> str:
    """Turn a title into a lowercase, hyphen-separated slug.

    >>> slugify("DeepSeek  Harness  rocks!")
    'deepseek-harness-rocks'
    """
    return title.lower().replace(" ", "-")


def truncate(text: str, limit: int) -> str:
    """Shorten text to at most `limit` characters, ending with an ellipsis when cut.

    >>> truncate("abcdef", 4)
    'abc…'
    """
    if len(text) <= limit:
        return text
    return text[:limit + 1] + "…"
