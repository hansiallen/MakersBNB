# tests/test_booking_integration.py

import pytest
from lib.bookings import Booking
from lib.bookings_repo import BookingRepo

@pytest.fixture
def setup_booking_repo(db_connection):
    repo = BookingRepo(db_connection)
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    yield repo

from datetime import date

def test_create_and_retrieve_booking(setup_booking_repo):
    repo = setup_booking_repo
    booking = Booking(None, 1, 2, date(2024, 11, 12)) 
    
    booking_id = repo.add_booking(booking)
    retrieved_booking = repo.get_booking(booking_id)
    
    assert retrieved_booking is not None
    assert retrieved_booking.space_id == 1
    assert retrieved_booking.user_id == 2
    assert retrieved_booking.booking_date == date(2024, 11, 12) 


def test_remove_booking(setup_booking_repo):
    repo = setup_booking_repo
    booking = Booking(None, 1, 2, "2024-11-12")
    booking_id = repo.add_booking(booking)
    
    repo.remove_booking(booking_id)
    assert repo.get_booking(booking_id) is None

def test_list_bookings(setup_booking_repo):
    repo = setup_booking_repo
    
    all_bookings = repo.list_bookings()
    assert len(all_bookings) > 0  # Ensure there's at least one booking in the seeded data

def test_invalid_booking_id_removal(setup_booking_repo):
    repo = setup_booking_repo
    result = repo.remove_booking(9999)  # Assuming 9999 is a non-existent ID
    assert result is False
