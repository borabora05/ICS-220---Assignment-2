# File: event.py

# Define the Event class
class Event:
    """
    This class represents an event happening at the Louvre Museum.

    Attributes:
        id (int): Unique identifier for the event.
        name (str): Name of the event (e.g., concert, lecture).
        date (str): Date of the event.
        location (str): Location of the event within the museum.
        price (float): Price of the event ticket (excluding VAT).
    """
    # Constructor method to initialize attributes
    def __init__(self, id, name, date, location, price):
        # Initialize attributes with provided values
        self.id = id  # Unique identifier for the event
        self.name = name  # Name of the event
        self.date = date  # Date of the event
        self.location = location  # Location of the event
        self.price = price  # Price of the event