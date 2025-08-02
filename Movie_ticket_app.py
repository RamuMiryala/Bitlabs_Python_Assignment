# movie_ticket_booking.py

def get_available_seats(total_seats, booked_seats):
    """
    Returns a list of currently available seats.

    Parameters:
    total_seats (int): Total number of seats in the cinema.
    booked_seats (list): List of already booked seat numbers.

    Returns:
    list: Available seat numbers.
    """
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def book_seat(booked_seats, seat_to_book, total_seats):
    """
    Books a seat if it's not already booked and within valid range.

    Parameters:
    booked_seats (list): List of booked seat numbers.
    seat_to_book (int): Seat number to book.
    total_seats (int): Total number of seats.

    Returns:
    list: Updated list of booked seats.
    """
    if seat_to_book < 1 or seat_to_book > total_seats:
        print(f"Seat {seat_to_book} is out of range.")
    elif seat_to_book in booked_seats:
        print(f"Seat {seat_to_book} is already booked.")
    else:
        booked_seats.append(seat_to_book)
        print(f"Seat {seat_to_book} booked successfully.")
    return booked_seats

def cancel_seat(booked_seats, seat_to_cancel):
    """
    Cancels a booked seat if it exists.

    Parameters:
    booked_seats (list): List of booked seat numbers.
    seat_to_cancel (int): Seat number to cancel.

    Returns:
    list: Updated list of booked seats.
    """
    if seat_to_cancel in booked_seats:
        booked_seats.remove(seat_to_cancel)
        print(f"Seat {seat_to_cancel} cancelled successfully.")
    else:
        print(f"Seat {seat_to_cancel} is not currently booked.")
    return booked_seats

def main():
    total_seats = 10
    booked_seats = [2, 5, 7]

    # Booking a seat
    seat_to_book = 3
    booked_seats = book_seat(booked_seats, seat_to_book, total_seats)

    # Cancel a seat
    seat_to_cancel = 5
    booked_seats = cancel_seat(booked_seats, seat_to_cancel)

    # Show available seats
    available_seats = get_available_seats(total_seats, booked_seats)
    print("Available seats:", available_seats)

if __name__ == "__main__":
    main()
