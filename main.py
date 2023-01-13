import random

#Destinations

destination_list = ["Boone", "Asheville", "Wilmington", "Raleigh"]

#Restaurants

restaurant_list = ["random hole-in-the-wall joint", "highest rated on TripAdvisor", "recommendation from locals", "first place you see"]

#Modes of transportation

modes_of_transportation = ["Vespa", "car", "electric scooter", "bicycle"]

#Types of entertainment

types_of_entertainment = ["sightseeing", "museums", "breweries", "people watching"]

day_trip_destination = random.choice(destination_list)

day_trip_restaurant = random.choice(restaurant_list)

day_trip_transportation = random.choice(modes_of_transportation)

day_trip_entertainment = random.choice(types_of_entertainment)

print(day_trip_destination)