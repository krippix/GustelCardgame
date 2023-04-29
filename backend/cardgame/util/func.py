# external
# python native
import os, base64
# project

def check_username(name: str) -> bool:
    """Checks if username is acceptable

    Args:
        name: username
    """
    if len(name) < 3 or len(name) > 20:
        return False
    return True


def generate_key() -> str:
    """Generates key for users to authenticate themselves

    Returns:
        key
    """
    random_bytes = os.urandom(64)
    key = base64.b64encode(random_bytes).decode('utf-8')
    return key