from lib.bookings_repo import BookingRepo
from lib.bookings import Booking
from mock import Mock
from datetime import date  # Import date to create date objects

def test_add_booking(db_connection):
    booking_repo = BookingRepo(db_connection)
    db_connection.execute("DELETE FROM bookings")
    
    booking = Mock()
    booking.booking_id = None
    booking.space_id = 1
    booking.user_id = 2
    booking.start_date = date(2024, 11, 12)  # Use date object here
    booking.end_date = date(2024, 11, 14)    # Use date object here
    booking.accepted = False
    
    booking_id = booking_repo.add_booking(booking)
    assert booking_id is not None

def test_remove_booking(db_connection):
    booking_repo = BookingRepo(db_connection)
    db_connection.execute("DELETE FROM bookings")
    
    booking = Booking(None, 1, 2, date(2024, 11, 12), date(2024, 11, 14),False)
    booking_id = booking_repo.add_booking(booking)
    assert booking_repo.remove_booking(booking_id) == True
    assert booking_repo.get_booking(booking_id) is None

def test_get_booking(db_connection):
    booking_repo = BookingRepo(db_connection)
    db_connection.execute("DELETE FROM bookings")
    
    # Use date objects for start and end dates instead of string
    booking = Booking(None, 1, 2, date(2024, 11, 12), date(2024, 11, 14),False)
    booking_id = booking_repo.add_booking(booking)
    retrieved_booking = booking_repo.get_booking(booking_id)
    
    assert retrieved_booking is not None
    assert retrieved_booking.start_date == date(2024, 11, 12)  # Compare with date object
    assert retrieved_booking.end_date == date(2024, 11, 14)    

def test_list_bookings(db_connection):
    booking_repo = BookingRepo(db_connection)
    db_connection.execute("DELETE FROM bookings")
    
    # Use date objects for start and end dates
    booking_repo.add_booking(Booking(None, 1, 2, date(2024, 11, 12), date(2024, 11, 14),False))
    booking_repo.add_booking(Booking(None, 1, 3, date(2024, 11, 15), date(2024, 11, 18),False))
    all_bookings = booking_repo.list_bookings()
    
    assert len(all_bookings) == 2
