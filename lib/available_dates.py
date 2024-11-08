class AvailableDate:
    def __init__(self, date_id, space_id, user_id, start_date, end_date):
        self.date_id = date_id
        self.space_id = space_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"AvailableDate({self.date_id}, {self.space_id}, {self.user_id}, {self.start_date}, {self.end_date})"
