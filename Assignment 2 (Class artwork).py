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