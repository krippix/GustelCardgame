# external
import uvicorn
import pydantic
import fastapi
import fastapi.middleware.cors
# python native
import logging
# project
import util.func
import util.config


app = fastapi.FastAPI()


# Needed for cors support
app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"]
)

# ------ basemodels ------

class User(pydantic.BaseModel):
    name: str
    key: str


# ------ locations ------

@app.get("/")
async def test_get():
    return {"key" : "value"}


@app.post("/username/")
async def post_test(user: User):
    """Recieves username, evaluates and replies with key or error.
    Args:
        amogus: _description_
    Returns:
        {"valid": bool, "key": str, "msg": str}
    """
    print(f"recieved name: {user.name}")

    # Check if username is acceptable
    try:
        util.func.validate_username(user.name)
    except util.func.UsernameError as e:
        return {"valid": False, "key": None, "msg": str(e)}

    # Check if a key has been provided
    if user.key is None or not util.func.key_exists(user.key):
        user.key = util.func.generate_key()

    return {"valid": True, "key": user.key, "msg": None}


if __name__ == "__main__":
    uvicorn.run(
        app       = "main:app",
        log_level = logging.DEBUG,
        reload    = True
    )