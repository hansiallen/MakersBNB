from lib.booking import Booking

def test_booking_initialization():
    booking = Booking(booking_id=1, space_id=101, user_id=202, booking_date="2024-11-10")
    assert booking.booking_id == 1
    assert booking.space_id == 101
    assert booking.user_id == 202
    assert booking.booking_date == "2024-11-10"

def test_booking_to_dict():
    booking = Booking(booking_id=1, space_id=101, user_id=202, booking_date="2024-11-10")
    expected_dict = {
        "booking_id": 1,
        "space_id": 101,
        "user_id": 202,
        "booking_date": "2024-11-10"
    }
    assert booking.to_dict() == expected_dict

def test_booking_repr():
    """Test that the __repr__ method returns the expected string representation"""
    booking = Booking(booking_id=1, space_id=101, user_id=202, booking_date="2024-11-10")
    expected_repr = "<Booking 1 for space 101 by user 202 on 2024-11-10>"
    assert repr(booking) == expected_repr
