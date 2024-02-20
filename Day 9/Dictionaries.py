
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Key is the word is the meaning, while Value is the definition.

# Formatted as > {Key: Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# To call the diction, we need to include the key.
print(programming_dictionary["Bug"])

# Adding new or modifing items to the dictionary.
programming_dictionary['Loop'] = "This is a modifed definition."

# You can create an empty dictionary.
empty_dict = {}

# Additonally, you can wipe an existing dictionary, modifies the dict to an empty string.
programming_dictionary = {}

# Loop through a dictionary.
for x in programming_dictionary:
    print(x)
    print(programming_dictionary[x])



# Nesting a List in a Dictionary.
travel_log = {
'France': ['Paris', 'Lille', 'Dijon'],          # Each Key can only have one value, convert to list to overcome this.
'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
}


# Nesting a Dictionary in a Dictionary.
travel_log = {
'France': {"cities_visited": ['Paris', 'Lille', 'Dijon'], "total_visits": 12},
'Germany': {"cities_visited": ['Berlin', 'Hamburg', 'Stuttgart'], "total_visits": 6}
}


# Nesting a Dictionary in a List.
travel_log = [                                  # Notice the brackets for travel log.
{"country": "France", 
 "cities_visited": ['Paris', 'Lille', 'Dijon'], 
 "total_visits": 12
 },

{"country": "Germany", 
 "cities_visited": ['Berlin', 'Hamburg', 'Stuttgart'], 
 "total_visits": 6
 }
]