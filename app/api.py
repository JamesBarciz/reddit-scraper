from fastapi import FastAPI

from .scraping import TEMP_SUBREDDITS, get_top_subreddits


app = FastAPI()

@app.get('/')
async def root():
    output = []
    get_top_subreddits(subreddits=TEMP_SUBREDDITS, output=output)
    return output
