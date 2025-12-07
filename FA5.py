destinations = []

print("Please enter your 5 travel destinations:")
for i in range(5):
    place = input(f"Destination {i + 1}: ")
    destinations.append(place)

print("\nOriginal Travel Itinerary:")
for i in range(5):
    print(f"{i + 1}. {destinations[i]}")

print("\nLet's update your 2nd and 5th destinations.")

new_scd = input("Enter a new destination for position 2: ")
new_ffth = input("Enter a new destination for position 5: ")

destinations[1] = new_scd
destinations[4] = new_ffth

print("\nUpdated Travel Itinerary:")
for i in range(5):
    print(f"{i + 1}. {destinations[i]}")
