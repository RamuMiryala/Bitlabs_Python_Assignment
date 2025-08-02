# taxi_fare_calculation.py

def calculate_fare(distance_km, base_fare=50, rate_per_km=10):
    """
    Calculates the fare for a single trip.

    Parameters:
    distance_km (float or int): Distance traveled in kilometers.
    base_fare (int): Fixed base fare for every trip.
    rate_per_km (int): Fare per kilometer.

    Returns:
    int: Total fare for the trip.
    """
    return base_fare + (distance_km * rate_per_km)

def main():
    trips = [5, 10, 3]  # Distances in km
    total_fare = 0

    for i, distance in enumerate(trips, start=1):
        fare = calculate_fare(distance)
        total_fare += fare
        print(f"Trip {i}: ${fare}")

    print(f"Total Fare: ${total_fare}")

if __name__ == "__main__":
    main()
