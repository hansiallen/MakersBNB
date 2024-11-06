from lib.bookings_repo import BookingRepo
from lib.bookings import Booking
from mock import Mock

def test_add_booking():
    db_connection = Mock()
    repo = BookingRepo(db_connection)

    # Mock the database response for INSERT query
    db_connection.execute.return_value = [{'booking_id': 1}]

    booking = Booking(None, 1, 1, "2024-11-10")
    added_booking = repo.add_booking(booking)

    assert added_booking.booking_id == 1
    assert added_booking.space_id == 1
    assert added_booking.user_id == 1
    assert added_booking.booking_date == "2024-11-10"

def test_get_booking():
    db_connection = Mock()
    repo = BookingRepo(db_connection)

    # Mock the database response for SELECT query
    db_connection.execute.return_value = [{'booking_id': 1, 'space_id': 1, 'user_id': 1, 'booking_date': '2024-11-10'}]

    booking = repo.get_booking(1)
    assert booking is not None
    assert booking.booking_id == 1
    assert booking.space_id == 1
    assert booking.user_id == 1
    assert booking.booking_date == "2024-11-10"

def test_get_booking_not_found():
    db_connection = Mock()
    repo = BookingRepo(db_connection)

    # Mock the database response for a missing booking
    db_connection.execute.return_value = []

    booking = repo.get_booking(999)
    assert booking is None
