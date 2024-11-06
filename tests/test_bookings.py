from lib.bookings import Booking

def test_booking_equality():
    booking1 = Booking(1, 1, 1, "2024-11-10")
    booking2 = Booking(1, 1, 1, "2024-11-10")
    booking3 = Booking(2, 1, 1, "2024-11-11")

    # Assert bookings with the same data are equal
    assert booking1 == booking2

    # Assert bookings with different data are not equal
    assert booking1 != booking3
