# external
# python native
import pathlib
# project


def get_root() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent


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


class UsernameError(Exception):
    pass


if __name__ == "__main__":
    pass
    #generate_key()
    #print(key_exists("testing"))