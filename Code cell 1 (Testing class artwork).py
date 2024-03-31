#Testing artwork.py
# Create an Artwork object
artwork1 = Artwork(1, "Mona Lisa", "Leonardo da Vinci", "1503-1506", "Highly significant portrait painting", "Denon Wing")

# Test attribute access
print(f"Artwork ID: {artwork1.id}")
print(f"Title: {artwork1.title}")
print(f"Artist: {artwork1.artist}")
print(f"date_of_creation: {artwork1.date_of_creation}")
print(f"historical_significance: {artwork1.historical_significance}")
print(f"location: {artwork1.location}")