# external
import fastapi
import fastapi.security.api_key
# python native
import os, pathlib, secrets
# project
import util.func as func


key_header = fastapi.security.api_key.APIKeyHeader(name="key", auto_error=True)


def generate_key() -> str:
    """Generates key for users to authenticate themselves

    Returns:
        key
    """
    # Used paths
    datafolder = func.get_root().joinpath("data") #os.path.join(get_root(),"data")
    keyfile = datafolder.joinpath("keys.txt")

    # ensure folder
    pathlib.Path(datafolder).mkdir(parents=True, exist_ok=True)
    
    # generate the key
    key = secrets.token_urlsafe(16)

    # check if the key exists already (this should be impossible)
    if key_exists(key):
        return generate_key()

    # ensure / append to file
    with open(keyfile, 'a+') as file:
        file.write(f"{key}\n")

    return key


def key_exists(key: str) -> bool:
    """Checks if a provided key already exists in the dataset
    Args:
        key: _description_
    Returns:
        bool
    """
    if len(key) != 22:
        return False

    keyfile = func.get_root().joinpath(f"data{os.sep}keys.txt")
    # check if file exists
    if not keyfile.exists():
        return False
    
    # check if key exists
    with open(keyfile, 'r') as keyfile:
        for line in keyfile:
            if line.strip() == key:
                return True
    print("no matching key found??")
    return False


def check_api_key(key: str = fastapi.Depends(key_header)):
    """Helper function to check if access is allowed
    Args:
        key: _description_. Defaults to fastapi.Depends(key_header).
    Raises:
        fastapi.HTTPException: _description_
    """
    if not key_exists(key):
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )
    return key


if __name__ == "__main__":
    pass
    generate_key()
    print(key_exists("MbQ+Mzy2GfylZOYMBihFBw=="))