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
print(visitor1.type)
print(f"Ticket ID: {ticket1.id}")
print(f"Price (after discount): {ticket1.price}")
print(f"Ticket Type: {ticket1.ticket_type.name}")
