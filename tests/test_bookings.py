import pytest
from lib.bookings import Booking

def test_is_equal():
    booking1 = Booking(1, 1, 1, "2024-11-10", "2024-11-12",False)
    booking2 = Booking(1, 1, 1, "2024-11-10", "2024-11-12",False)
    assert booking1 == booking2

def test_create_booking():
    booking = Booking(1, 1, 1, "2024-11-10", "2024-11-12",False)
    assert booking.booking_id == 1
    assert booking.space_id == 1
    assert booking.user_id == 1
    assert booking.start_date == "2024-11-10"
    assert booking.end_date == "2024-11-12"

def test_missing_dates():
    with pytest.raises(ValueError):
        Booking(1, 1, 1, None, "2024-11-12",False)
    with pytest.raises(ValueError):
        Booking(1, 1, 1, "2024-11-10", None,False)
