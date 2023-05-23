from fastapi import FastAPI
import uvicorn

from api import router


app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
