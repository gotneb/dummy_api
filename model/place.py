from dataclasses import dataclass

@dataclass
class Place:
    id: int
    country: str
    city: str
    description: str
    rating: float
    price: float
    image: str