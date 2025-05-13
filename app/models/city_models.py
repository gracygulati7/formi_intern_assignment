# from pydantic import BaseModel, Field
# from typing import List, Optional, Dict

# class BranchTiming(BaseModel):
#     opening_time: str
#     last_entry_time: str
#     closing_time: str

# class DayTimings(BaseModel):
#     Lunch: Optional[BranchTiming]
#     Dinner: Optional[BranchTiming]

# class BranchInfo(BaseModel):
#     address: str
#     bar_availability: str
#     valet_parking: str
#     baby_chair: str
#     lift_availability: str
#     pdr_availability: str
#     pdr_capacity: str
#     pdr_minimum_pax_required: str
#     outlet_numbers: List[str]

# class NearestOutlet(BaseModel):
#     name: str
#     distance: str
#     address: str

# class Offers(BaseModel):
#     early_bird: str
#     kitty_party: str
#     student_offer: str
#     buffet_5_plus_1: str = Field(..., alias="5+1_buffet")
#     army_offer: str
#     drinks_offer: str

# class AdditionalInfo(BaseModel):
#     complimentary_drinks: str
#     food_festival: str

# class BookingInstructions(BaseModel):
#     root: Dict[str, Dict[str, str]]

# class Branch(BaseModel):
#     name: str
#     modified_on: str
#     special_notice: Optional[str]
#     booking_instructions: BookingInstructions
#     branch_info: BranchInfo
#     branch_timings: Dict[str, DayTimings]
#     additional_info: AdditionalInfo
#     nearest_outlets: List[NearestOutlet]
#     offers: Offers

# class CityData(BaseModel):
#     city: str
#     branches: List[Branch]