# File: tour.py

# Define the Tour class
class Tour:
    """
    This class represents a guided tour offered at the Louvre Museum.

    Attributes:
        id (int): Unique identifier for the tour.
        guide (str): Name of the tour guide.
        date (str): Date of the tour.
        visitorCount (int): Number of visitors signed up for the tour (limited to 15-40).
    """

    # Constructor method to initialize attributes
    def __init__(self, id, guide, date):
        # Initialize attributes with provided values
        self.id = id  # Unique identifier for the tour
        self.guide = guide  # Guide for the tour
        self.date = date  # Date of the tour
        self.visitor_count = visitor_count  # Initialize visitor count for the tour

        if visitor_count < 15 or visitor_count > 40:
            raise ValueError("Tour visitor count must be between 15 and 40")