import random

#Destinations

destination_list = ["Boone", "Asheville", "Wilmington", "Raleigh"]

#Restaurants

restaurant_list = ["Random hole-in-the-wall joint", "Highest rated on TripAdvisor", "Recommendation from locals", "First place you see"]

#Modes of transportation

modes_of_transportation = ["Vespa", "Car", "Electric scooter", "Bicycle"]

#Types of entertainment

types_of_entertainment = ["Sightseeing", "Museums", "Breweries", "People watching"]

day_trip_destination = random.choice(destination_list)

day_trip_restaurant = random.choice(restaurant_list)

day_trip_transportation = random.choice(modes_of_transportation)

day_trip_entertainment = random.choice(types_of_entertainment)

print("Welcome to your random day trip generator! Let's get started.")
print(day_trip_destination)
print(day_trip_transportation)
print(day_trip_entertainment)
print(day_trip_restaurant)