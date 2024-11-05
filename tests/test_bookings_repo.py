import pytest
from lib.bookings_repo import BookingsRepo

def test_create_booking():
    repo = BookingsRepo()
    booking = repo.create_booking(1, 1, 1, "01-12-2024", "05-12-2024")
    assert booking.id == 1
    assert booking.user_id == 1
    assert booking.space_id == 1

def test_get_booking():
    repo = BookingsRepo()
    repo.create_booking(1, 1, 1, "01-12-2024", "05-12-2024")
    booking = repo.get_booking(1)
    assert booking is not None
    assert booking.id == 1

def test_get_bookings_by_space():
    repo = BookingsRepo()
    repo.create_booking(1, 1, 1, "01-12-2024", "05-12-2024")
    repo.create_booking(2, 2, 1, "06-12-2024", "10-12-2024")
    bookings = repo.get_bookings_by_space(1)
    assert len(bookings) == 2

def test_update_booking_status():
    repo = BookingsRepo()
    repo.create_booking(1, 1, 1, "01-12-2024", "05-12-2024")
    updated_booking = repo.update_booking_status(1, "confirmed")
    assert updated_booking.status == "confirmed"

def test_delete_booking():
    repo = BookingsRepo()
    repo.create_booking(1, 1, 1, "01-12-2024", "05-12-2024")
    result = repo.remove_booking(1)
    assert result is True
    assert repo.get_booking(1) is None

def test_delete_nonexistent_booking():
    repo = BookingsRepo()
    result = repo.remove_booking(999)  # Non-existent booking ID
    assert result is False
