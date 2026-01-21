import re
from django import template

register = template.Library()


@register.filter
def youtube_video_id(url):
    """
    Extract YouTube video ID from a YouTube URL.
    Handles formats:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/watch?v=VIDEO_ID&t=123s
    """
    if not url:
        return ''

    # Pattern for youtube.com/watch?v=
    match = re.search(r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\s]+)', url)
    if match:
        return match.group(1)

    return ''
