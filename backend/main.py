import fastapi
import fastapi.middleware.cors
import pydantic


app = fastapi.FastAPI()

# Needed for cors support
app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def amogus():
    return {"amogus" : "sus"}



class Test(pydantic.BaseModel):
    name: str
    desc: str


@app.post("/")
async def post_test(amogus: Test):
    print(amogus)
    return {"coggers":"amogus"}