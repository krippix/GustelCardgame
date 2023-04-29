# external
import fastapi
import fastapi.middleware.cors
import pydantic
# python native
import logging
# project
import util.func

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = fastapi.FastAPI()

# Needed for cors support
app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def test_get():
    return {"key" : "value"}




class Username(pydantic.BaseModel):
    name: str

@app.post("/username/")
async def post_test(username: Username):
    """Creates username and id-pair 

    Args:
        amogus: _description_

    Returns:
        _description_
    """
    logger.info(f"recieved name: {username.name}")
    key = util.func.generate_key()

    return {"key" : key}