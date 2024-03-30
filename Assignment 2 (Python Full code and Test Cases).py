# File: artwork.py

# Define the Artwork class
class Artwork:
    ''' A class to represent the Artwork of the Lovure museum'''
    # Constructor method to initialize attributes
    def __init__(self, id, title, artist, date_of_creation, historical_significance, location):
        # Initialize attributes with provided values
        self.id = id  # Unique identifier for the artwork
        self.title = title  # Title of the artwork
        self.artist = artist  # Artist who created the artwork
        self.date_of_creation = date_of_creation  # Date of creation of the artwork
        self.historical_significance = historical_significance  # Historical significance of the artwork
        self.location = location  # Location of the artwork (e.g., permanent galleries, exhibition halls, outdoor spaces)


# File: exhibition.py

# Define the Exhibition class
class Exhibition:
    """
    This class represents an exhibition in the Louvre Museum.

    Attributes:
        id (int): Unique identifier for the exhibition.
        name (str): Name of the exhibition.
        duration (str): Duration of the exhibition (e.g., 3 months).
        location (str): Location of the exhibition (e.g., South Wing).
        artworks (List[Artwork]): List of artworks associated with the exhibition.
    """

    # Constructor method to initialize attributes
    def __init__(self, id, name, duration, location):
        # Initialize attributes with provided values
        self.id = id  # Unique identifier for the exhibition
        self.name = name  # Name of the exhibition
        self.duration = duration  # Duration of the exhibition
        self.location = location  # Location of the exhibition
        self.artworks = []  # List to store artworks associated with the exhibition

    def add_artwork(self, artwork: Artwork):
        """
        Adds an artwork to the exhibition's associated list.

        Args:
            artwork (Artwork): Artwork object to be added.
        """
        self.artworks.append(artwork)


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



#Testing artwork.py
# Create an Artwork object
artwork1 = Artwork(1, "Mona Lisa", "Leonardo da Vinci", "1503-1506", "Highly significant portrait painting", "Denon Wing")

# Test attribute access
print('TESTING Artwork.py')
print(f"Artwork ID: {artwork1.id}")
print(f"Title: {artwork1.title}")
print(f"Artist: {artwork1.artist}")
print(f"date_of_creation: {artwork1.date_of_creation}")
print(f"historical_significance: {artwork1.historical_significance}")
print(f"location: {artwork1.location}")

print('..................................................')

#Testing exhibition.py
# Create an Exhibition object
exhibition1 = Exhibition(101, "Egyptian Mummies: Secrets of the Pharaohs", "3 months", "South Wing")

# Test adding artwork to the exhibition
artwork2 = Artwork(2, "Mask of Tutankhamun", "Unknown Artist", "1323 BC", "Iconic funerary mask", "South Wing")
exhibition1.add_artwork(artwork2)

# Test attribute access
print('Testing Exhibition.py')
print(f"Exhibition ID: {exhibition1.id}")
print(f"Name: {exhibition1.name}")
print(f"Location: {exhibition1.location}")

# Print the first artwork in the exhibition (assuming the list is not empty)
if exhibition1.artworks:
    first_artwork = exhibition1.artworks[0]
print(f"First Artwork Title: {first_artwork.title}")

print('.....................................................')

#Testing ticket.py
# Create a Visitor object
visitor1 = Visitor(200, "Alice Smith", 30, "USA")

# Create a Ticket object (assuming an event object exists)
event1 = Event(1, "Lecture: The History of the Louvre", "2024-04-15", "Auditorium", 15.0)
ticket1 = Ticket(301, 0.0, TicketType.EVENT, visitor1, event1)

# Simulate calculating the price with discount (modify as needed)
visitor1.type = "Adult"  # Set visitor type for discount calculation
ticket1.calculate_price(visitor1.type)

# Test attribute access
print('TESTING Ticket.py')
print(visitor1.type)
print(f"Ticket ID: {ticket1.id}")
print(f"Price (after discount): {ticket1.price}")
print(f"Ticket Type: {ticket1.ticket_type.name}")

print('....................................................')

#Testing visitor.py
# Create a Visitor object
visitor2 = Visitor(201, "John Doe", 12, "France")

# Test attribute access
print('TESTING Visitor.py')
print(f"Visitor ID: {visitor2.id}")
print(f"Name: {visitor2.name}")
print(f"Age: {visitor2.age}")
print(f"Nationality: {visitor2.nationality}")

print('.....................................................')

#Testing event.py
# Create an Event object
event2 = Event(2, "Concert: Music through the Ages", "2024-05-10", "Auditorium", 20.0)

# Test attribute access
print('TESTING Event.py')
print(f"Event ID: {event2.id}")
print(f"Name: {event2.name}")
print(f"Date: {event2.date}")
print(f"Location: {event2.location}")
print(f"Price: {event2.price} AED")

print('.........................................................')

#Testing tour.py
# Create a Tour object with valid visitor count
print('TESTING Tour.py')
try:
    visitor_count = 20
    tour1 = Tour(visitor_count, "Michael", "2024-04-01")
    print(f"Tour Guide: {tour1.guide}")
    print(f"Tour Date: {tour1.date}")
except ValueError as e:
    print(f"Error: {e}")

# Create a Tour object with invalid visitor count (should raise an error)
try:
    visitor_count = 10
    tour2 = Tour(visitor_count, "Lisa", "2024-04-20")
except ValueError as e:
    print(f"Error: {e}")
