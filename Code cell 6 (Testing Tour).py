#Testing tour.py
# Create a Tour object with valid visitor count
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