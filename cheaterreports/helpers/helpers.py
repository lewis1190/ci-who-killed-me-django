from urllib.parse import urlparse
from typing import Optional

# Needed to use `Optional` to appease the type checker...


def is_valid_youtube_url(url: Optional[str]) -> bool:
    """
    Validate that a URL is a valid YouTube URL.
    Accepts formats:
    - https://www.youtube.com/watch?v=dQw4w9WgXcQ
    - https://youtu.be/dQw4w9WgXcQ
    - https://youtube.com/watch?v=dQw4w9WgXcQ (without www)
    - http:// variants
    """
    if not url:
        return False

    # Parse the URL
    try:
        parsed = urlparse(url)
    except Exception:
        return False

    # Check if scheme is http or https
    if parsed.scheme not in ['http', 'https']:
        return False

    # Check if domain is youtube.com or youtu.be
    domain = parsed.netloc.lower()
    if domain not in ['youtube.com', 'www.youtube.com',
                      'youtu.be', 'www.youtu.be']:
        return False

    return True
