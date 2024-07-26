# tests/test_utils.py


def clear_stream(stream):
    """Clears the content of a stream (like StringIO)."""
    stream.seek(0)
    stream.truncate(0)
