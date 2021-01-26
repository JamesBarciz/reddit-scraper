from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

from app.api.scraping import TEMP_SUBREDDITS, get_top_subreddits


app = FastAPI()


@app.get('/top-subreddits')
async def subreddits():
    output = []
    get_top_subreddits(subreddits=TEMP_SUBREDDITS, output=output)
    return output


if __name__ == '__main__':
    uvicorn.run(app)
