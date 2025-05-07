from fastapi import FastAPI, HTTPException, Query
import model
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/places/search/{name}")
async def search_places(name: str):
    all_places = model.get_places() + model.get_famous_places()
    places = model.find_places_by_country(all_places, name)
    return places


@app.get("/places/recommended")
async def get_recommended_places():
    places = model.get_famous_places()
    print(places)
    return places


@app.get("/places/top")
async def get_top_places():
    all_places = model.get_places() + model.get_famous_places()
    places = model.get_random_places(all_places)
    print(places)
    return places

@app.get("/places/{id}")
async def get_place_id(id: int):
    all_places = model.get_places() + model.get_famous_places()
    place = model.find_place_by_id(all_places, id)
    print(f"Found place {place.country}")
    return place