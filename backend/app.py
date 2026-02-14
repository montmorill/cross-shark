import dotenv
from fastapi import FastAPI

from src.longmao_parser import parse_content


dotenv.load_dotenv('.dev.local')

app = FastAPI()

@app.get("/parse")
def parse(url: str):
    return parse_content(url)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
