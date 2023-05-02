# external
# python native
import os, base64
# project


def validate_username(name: str):
    """Checks if username fulfills the requirents, raises exception if it doesent.
    Args:
        name: username to check
    Returns:
        bool
    """
    error = "username invalid:"
    valid = True

    if len(name) < 3:
        error += "\n - must be 3 or more characters"
        valid = False
    if len(name) > 20:
        error += "\n - must be 20 or less characters"
        valid = False
    
    if valid:
        return True
    else:
        raise UsernameError(error)


def generate_key() -> str:
    """Generates key for users to authenticate themselves

    Returns:
        key
    """
    random_bytes = os.urandom(64)
    key = base64.b64encode(random_bytes).decode('utf-8')
    return key

class UsernameError(Exception):
    pass