
states_of_america = ["Texas", "Utah", "Florida"]

for states in states_of_america:
    print(states)
    print(states + " of America")


# Loop to count to ten.
for n in range(1, 11):
    print(n)

# Loop to count backwards from 10.
for countdown in reversed(range(1, 11)):
    print(countdown)
print("HAPPY NEW YEAR!")

# Loop to count backwards while using the range function, change step to -1.
for count in range(10, 0, -1):      # range( from, to, step (-1 goes backwards)).
    print(count)

# Loop that counts in 3 increments.
for n in range(0, 10, 3):
    print(n)


# Loops with lists.
credit_card = "abc-123-xyz-456"
for y in credit_card:
    print(y)

# This will skip 13 and continue with the count.
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# This will break out of the loop entirely.
for k in range(0, 21):
    if k == 5:
        break
    else:
        print(k)
