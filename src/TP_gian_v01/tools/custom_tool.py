from pydantic import BaseModel, Field
from typing import List, Optional
    
class Activity(BaseModel):
    name: str = Field(..., description="The name of the activity")
    description: str = Field(..., description="A description of the activity")
    location: str = Field(..., description="The location of the activity")
    date: str = Field(..., description="The date of the activity")
    cuisine: str = Field(..., description="The cuisine of the activity")
    why_its_suitable: str = Field(..., description="Why it's suitable for the user")
    rating: str = Field(..., description="The rating of the activity")
    reviews: str = Field(..., description="The reviews of the activity")

class DayPlan(BaseModel):
    date: str = Field(..., description="The date of the day plan")
    activities: List[Activity] = Field(..., description="The activities of the day plan")
    restaurants: List[str] = Field(..., description="The restaurants of the day plan")

class Itinerary(BaseModel):
    days: List[DayPlan] = Field(..., description="The day plans of the trip")
    name: str = Field(..., description="The name of the itinerary")
    hotel: str = Field(..., description="The hotel of the itinerary")
