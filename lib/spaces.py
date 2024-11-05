class Space:
    _id_counter = 1  # Class-level counter for unique IDs

    def __init__(self, user_id, name, description, price_per_night, available_dates):
        if not name:
            raise ValueError("Name is required")
        self.user_id = user_id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.available_dates = available_dates
        self.id = Space._id_counter
        Space._id_counter += 1

    def is_available(self, start_date, end_date):
        return all(date in self.available_dates for date in range(start_date, end_date))
    
    def book(self, start_date, end_date):
        for date in range(start_date, end_date):
            self.available_dates.remove(date)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.user_id}, {self.name}, {self.description}, {self.price_per_night}, {self.available_dates})"
    
