import dotenv
from fastapi import FastAPI


dotenv.load_dotenv('.env.local', verbose=True)

app = FastAPI()


@app.get("/parse")
def parse(url: str):
    import longmao_parser as parser
    return parser.parse_content(url)['data']['info']


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
