print("Welcome to the Hotel Booking System")

room = {
    "single": {"price": 50, "available": 5},
    "double": {"price": 80, "available": 3},
    "suite": {"price": 150, "available": 2},
}

s = 0

while True:
    print("\nAvailable rooms and prices: ")
    for key, val in room.items():
        print(f"{key}: ${val['price']} (Available: {val['available']})")

    order = (
        input("\nWhich room would you like to book? (done): ").strip().lower()
    )

    if order == "done":
        break

    booked = False
    for key in room:
        if key.lower() == order:
            if room[key]["available"] > 0:
                room[key]["available"] -= 1
                s += room[key]["price"]
                print(f"{key} room booked successfully.")
                booked = True
            else:
                print(f"Sorry, no available rooms for {key}.")
                booked = True
            break

    if not booked:
        print("Invalid room choice, please try again.")

print(f"\nTotal cost for your bookings: ${s}")
print("Thank you for choosing our hotel!")