# external
import uvicorn
import pydantic
import fastapi
import fastapi.middleware.cors
import fastapi.security.api_key
# python native
import logging
# project
import util.func
import util.config
import auth


app = fastapi.FastAPI()


# Needed for cors support
app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"]
)

# ------ basemodels ------

class Key(pydantic.BaseModel):
    key: str


class Username(pydantic.BaseModel):
    name: str


# ------ locations ------

@app.get("/key/")
async def get_key():
    """Gets new key for a new user
    Returns:
        {key:value}    
    """
    key = auth.generate_key()
    return {"key" : key}


@app.get("/test/", dependencies=[fastapi.Depends(auth.check_api_key)])
async def test_con():
    return {"amogus":"wurstbrot"}


@app.post("/username/")
async def post_test(user: Username, key: str = fastapi.Depends(auth.check_api_key)):
    """Recieves username, evaluates and replies with key or error.
    Username must be between 3 and 20 characters.
    Args:
        amogus: _description_
    Returns:
        {"valid": bool, "key": str, "msg": str}
    """
    print(f"recieved name: {user.name} for key: {key}")

    # Check if username is acceptable
    try:
        util.func.validate_username(user.name)
    except util.func.UsernameError as e:
        return {"valid": False, "error": str(e)}
    return {"valid": True, "error": None}


if __name__ == "__main__":
    uvicorn.run(
        app       = "main:app",
        log_level = logging.DEBUG,
        reload    = True
    )