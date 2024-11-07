from datetime import date  # Import date to create date objects
from lib.booking_is_available import booking_is_available
def test_valid_day(db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    db_connection.seed("seeds/available_dates.sql")
    assert booking_is_available(db_connection,1,date(2024,11,5),date(2024,11,7))

def test_invalid_date(db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    db_connection.seed("seeds/available_dates.sql")
    result =booking_is_available(db_connection,1,date(2024,11,8),date(2024,11,7))
    assert result == False

def test_invalid_day(db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    db_connection.seed("seeds/available_dates.sql")
    result =booking_is_available(db_connection,1,date(2024,11,14),date(2024,12,27))
    assert result == False
    result =booking_is_available(db_connection,1,date(2024,11,10),date(2024,11,14))
    assert result == False

def test_different_time_slot(db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    db_connection.seed("seeds/available_dates.sql")
    db_connection.execute("""
    INSERT INTO available_dates (space_id, user_id, start_date, end_date) VALUES 
    (1, 2, '2025-10-10', '2025-12-24');
    """)
    assert booking_is_available(db_connection,1,date(2025,11,14),date(2025,12,23))
    result  =booking_is_available(db_connection,1,date(2025,10,9),date(2025,11,14))
    assert result == False
