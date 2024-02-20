country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆


def add_new_country(name, times_visited, cities_visited):
    new_item = {}                           # creating a blank dict.
    new_item["country"] = name              # passing the input data into the key data for each below.
    new_item["visits"] = times_visited      
    new_item["cities"] = cities_visited
    travel_log.append(new_item)             # since travel log is a list, we can append this new dict to it.



# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")