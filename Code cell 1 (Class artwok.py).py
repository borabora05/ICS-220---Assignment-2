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