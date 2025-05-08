import random
import json
from typing import List, Optional
from .place import Place

def get_places() -> List[Place]:
    with open("data/regular_places.json", "r") as file:
        data = json.load(file)

    print("Loaded regular places")
    places = [Place(**place) for place in data]
    return places


def get_famous_places() -> List[Place]:
    with open("data/famous_places.json", "r") as file:
        data = json.load(file)

    print("Loaded famous places")
    places = [Place(**place) for place in data]
    return places


def find_place_by_id(places: List[Place], place_id: int) -> Optional[Place]:
    for place in places:
        if place.id == place_id:
            return place
    return None


def find_places_by_country(places: List[Place], country_name: str) -> List[Place]:
    return [place for place in places if place.country.lower() == country_name.lower()]

def get_random_places(places: List[Place]) -> List[Place]:
    return random.sample(places, 10)