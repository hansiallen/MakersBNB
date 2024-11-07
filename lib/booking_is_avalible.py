def booking_is_avalible(db_connection, space_id,start_date, end_date):
    if start_date> end_date:
        return False
    avalible_dates = db_connection.execute("SELECT * FROM avalible_dates WHERE space_id = %s",[space_id])
    booked_dates = db_connection.execute("SELECT * FROM bookings WHERE space_id = %s",[space_id])

    for daterange in booked_dates:#checks if it overlaps with another booking 
        if not (daterange.get("start_date") > end_date or start_date > daterange.get("end_date")):
            return False
    
    for daterange in avalible_dates: # checks if it is not in the avalible dates range
        if not (daterange.get("start_date") > start_date or end_date > daterange.get("end_date")):
            return True
    return False