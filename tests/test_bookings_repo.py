from lib.bookings_repo import BookingRepo
from lib.bookings import Booking
from mock import Mock

def test_add_booking(db_connection):
    booking_repo = BookingRepo(db_connection)
    db_connection.execute("DELETE FROM bookings")
    
    booking = Mock()
    booking.booking_id = None
    booking.space_id = 1
    booking.user_id = 2
    booking.booking_date = "2024-11-12"
    
    booking_id = booking_repo.add_booking(booking)
    assert booking_id is not None

def test_remove_booking(db_connection):
    booking_repo = BookingRepo(db_connection)
    db_connection.execute("DELETE FROM bookings")
    
    # Add and then remove booking
    booking = Booking(None, 1, 2, "2024-11-12")
    booking_id = booking_repo.add_booking(booking)
    assert booking_repo.remove_booking(booking_id) == True
    assert booking_repo.get_booking(booking_id) is None

def test_get_booking(db_connection):
    booking_repo = BookingRepo(db_connection)
    db_connection.execute("DELETE FROM bookings")
    
    # Add booking and retrieve it
    booking = Booking(None, 1, 2, "2024-11-12")
    booking_id = booking_repo.add_booking(booking)
    retrieved_booking = booking_repo.get_booking(booking_id)
    
    assert retrieved_booking is not None
    assert retrieved_booking.space_id == 1
    assert retrieved_booking.user_id == 2

def test_list_bookings(db_connection):
    booking_repo = BookingRepo(db_connection)
    db_connection.execute("DELETE FROM bookings")
    
    booking_repo.add_booking(Booking(None, 1, 2, "2024-11-12"))
    booking_repo.add_booking(Booking(None, 1, 3, "2024-11-13"))
    all_bookings = booking_repo.list_bookings()
    
    assert len(all_bookings) == 2
