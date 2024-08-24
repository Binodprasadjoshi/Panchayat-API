from fastapi import FastAPI, Request
from fastapi import HTTPException
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import json
from typing import List

with open ("data/data.json", "r") as f:
    data = json.load(f)

seasons_data = data["seasons"]
cast_data = data["cast"]

#Data models
class Episode(BaseModel):
    episode_number: int
    title: str
    description: str

class Season(BaseModel):
    season_number: int
    episodes: List[Episode]

class Cast(BaseModel):
    name: str
    role: str

app = FastAPI()
templates = Jinja2Templates(directory="template")

#Routes(Endpoints)
@app.get("/", include_in_schema=False)
async def get_homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/seasons/", response_model=List[Season])
async def get_all_seasons():
    return seasons_data

@app.get("/api/seasons/{season_number}/", response_model = Season)
async def get_season(season_number: int):
    for season in seasons_data:
        if season_number == season["season_number"]:
            return season
    raise HTTPException(status_code = 404, detail = "Season not found")

@app.get("/api/seasons/{season_number}/episodes/", response_model= List[Episode])
async def get_episodes_by_season(season_number: int):
    for season in seasons_data:
        if season_number == season["season_number"]:
            return season["episodes"]
    raise HTTPException(status_code = 404, detail = "Season not found")

@app.get("/api/seasons/{season_number}/episode/{episode_number}/", response_model= Episode)
async def get_episode(season_number: int, episode_number: int):
    for season in seasons_data:
        if(season_number == season["season_number"]):
            for episode in season["episodes"]:
                if episode_number == episode["episode_number"]:
                    return episode
    raise HTTPException(status_code=404, detail= "Episode Not Found")

@app.get("/api/cast/", response_model=List[Cast])
async def get_cast():
    return cast_data