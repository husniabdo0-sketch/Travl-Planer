destination = input("Destination: ").strip()
distance = float(input("Distance in kilometers: "))
average_speed = float(input("Average speed in km/h: "))

if average_speed <= 0:
    print("Average speed must be greater than zero.")
else:
    travel_hours = distance / average_speed
    whole_hours = int(travel_hours)
    minutes = round((travel_hours - whole_hours) * 60)

    # Adjust if rounding gives us 60 minutes
    if minutes == 60:
        whole_hours += 1
        minutes = 0

    print()
    print("=" * 42)
    print("               TRAVEL PLAN")
    print("=" * 42)
    print(f"Destination: {destination}")
    print(f"Distance: {distance:g} km")
    print(f"Average speed: {average_speed:g} km/h")
    print(f"Estimated travel time: {whole_hours} hours and {minutes} minutes")
    print("=" * 42)