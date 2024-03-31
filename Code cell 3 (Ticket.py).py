# File: ticket.py

from enum import Enum


class TicketType(Enum):
    """
    Enumeration for different ticket types.
    """
    EXHIBITION = "Exhibition"
    TOUR = "Tour"
    EVENT = "Event"


# Define the Ticket class
class Ticket:
    """
    This class represents a ticket for the Louvre Museum.

    Attributes:
        id (int): Unique identifier for the ticket.
        price (float): Price of the ticket (including VAT if applicable).
        type (TicketType): Type of the ticket (exhibition, tour, or event).
        visitor (Visitor): Visitor associated with the ticket (can be None initially).
        event (Event): Event associated with the ticket (can be None for exhibition or tour tickets).
    """

    # Constructor method to initialize attributes
    def __init__(self, id, price, ticket_type, visitor, event):
        # Initialize attributes with provided values
        self.id = id  # Unique identifier for the ticket
        self.price = price  # Price of the ticket
        self.ticket_type = ticket_type  # Type of the ticket (e.g., adult, child, group)
        self.visitor = visitor  # Visitor associated with the ticket
        self.event = event  # Event associated with the ticket

        # Calculate base price based on event type (if applicable)
        self.base_price = 0.0
        if event:
            self.base_price = event.price
        elif ticket_type == TicketType.EXHIBITION:
            # Default price for exhibitions (can be replaced with dynamic pricing)
            self.base_price = 20.0

        # Apply discount based on visitor type
        self.price = self.calculate_price(visitor.type)

    def calculate_price(self, type):
        discount = 0.0
        if type == "Adult" and 18 <= self.visitor.age <= 60:
            discount = 0.0
        elif type == "Child" and self.visitor.age < 18:
            discount = 1.0  # Free ticket for children
        elif type in ("Senior", "Teacher/Student"):
            discount = 1.0  # Free ticket for seniors and students
        elif type == "Group":
            discount = 0.5

        # Apply discount and add 5% VAT
        self.price = (self.base_price * (1 - discount)) * 1.05
        return self.price