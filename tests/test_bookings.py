from lib.bookings import Booking

def test_booking_creation():
    booking = Booking(1, 1, 1, "01-12-2024", "05-12-2024")
    assert booking.id == 1
    assert booking.user_id == 1
    assert booking.space_id == 1
    assert booking.start_date.strftime("%d-%m-%Y") == "01-12-2024"
    assert booking.end_date.strftime("%d-%m-%Y") == "05-12-2024"
    assert booking.status == "pending"

def test_booking_equality():
    booking1 = Booking(1, 1, 1, "01-12-2024", "05-12-2024")
    booking2 = Booking(1, 1, 1, "01-12-2024", "05-12-2024")
    assert booking1 == booking2

def test_booking_str():
    booking = Booking(1, 1, 1, "01-12-2024", "05-12-2024")
    expected_str = "Booking 1: User 1 for Space 1 from 01-12-2024 to 05-12-2024, Status: pending"
    assert str(booking) == expected_str

def test_booking_repr():
    booking = Booking(1, 1, 1, "01-12-2024", "05-12-2024", "confirmed")
    expected_repr = "Booking(id=1, user_id=1, space_id=1, start_date=01-12-2024, end_date=05-12-2024, status='confirmed')"
    assert repr(booking) == expected_repr