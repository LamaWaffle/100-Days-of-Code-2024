names = ['matthew', 'mark', 'luke', 'john']
heights = [31, 61, 91, 121]

names_and_heights = zip(names, heights)
print(names_and_heights)

converted_zip = list(names_and_heights)
print(converted_zip)


owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)
list_names_and_dogs_names = names_and_dogs_names

print(list_names_and_dogs_names)