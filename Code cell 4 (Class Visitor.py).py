# File: visitor.py

# Define the Visitor class
class Visitor:
    """
    This class represents a visitor to the Louvre Museum.

    Attributes:
        id (int): Unique identifier for the visitor.
        name (str): Name of the visitor.
        age (int): Age of the visitor.
        nationality (str): Nationality of the visitor.
        ticketHistory (List[Ticket]): List of tickets purchased by the visitor.
    """
    # Constructor method to initialize attributes
    def __init__(self, id, name, age, nationality):
        # Initialize attributes with provided values
        self.id = id  # Unique identifier for the visitor
        self.name = name  # Name of the visitor
        self.age = age  # Age of the visitor
        self.nationality = nationality  # Nationality of the visitor
        self.ticket_history = []  # List to store ticket history for the visitor
        self.type = type