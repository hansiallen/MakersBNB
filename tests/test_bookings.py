import pytest
from lib.bookings import Booking

def test_is_equal():
    booking1 = Booking(1, 1, 1, "2024-11-10")
    booking2 = Booking(1, 1, 1, "2024-11-10")
    assert booking1 == booking2

def test_create_booking():
    booking = Booking(1, 1, 1, "2024-11-10")
    assert booking.booking_id == 1
    assert booking.space_id == 1
    assert booking.user_id == 1
    assert booking.booking_date == "2024-11-10"

def test_missing_booking_date():
    with pytest.raises(ValueError):
        Booking(1, 1, 1, None)
