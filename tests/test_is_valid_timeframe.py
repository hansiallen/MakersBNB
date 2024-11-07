from datetime import date  # Import date to create date objects

def test_add_booking(db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    db_connection.seed("seeds/avaliable_dates.sql")