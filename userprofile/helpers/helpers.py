# Setting a max size variable ensures that I can change this in the future if
# I want, or I could turn this into a config var in the future
def validate_file_size(file, max_size_mb: int = 1) -> tuple[bool, str]:
    """
    Validate that a file is under the specified size limit.

    Args:
        file: The uploaded file object
        max_size_mb: Maximum file size in megabytes (default: 1)

    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if not file:
        return True, ""

    # Convert MB to bytes (1 MB = 1,048,576 bytes)
    max_size_bytes = max_size_mb * 1024 * 1024

    if file.size > max_size_bytes:
        return False, f"File size must be under {max_size_mb} MB. " + \
            f"Your file is {file.size / 1024 / 1024:.2f} MB."

    return True, ""
