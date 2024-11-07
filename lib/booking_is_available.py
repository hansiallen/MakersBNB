def booking_is_available(db_connection, space_id,start_date, end_date):
    if start_date> end_date:
        return False
    available_dates = db_connection.execute("SELECT * FROM available_dates WHERE space_id = %s and not (start_date > %s or %s > end_date)",[space_id,start_date,end_date])
    booked_dates = db_connection.execute("SELECT * FROM bookings WHERE space_id = %s and not (start_date > %s or %s > end_date)",[space_id,end_date,start_date])

    if booked_dates != []:#checks if it overlaps with another booking 
        return False
    
    if available_dates != []: # checks if it is not in the available dates range
        return True
    return False