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

#STARTING FROM HERE
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

#Testing exhibition.py
# Create an Exhibition object
exhibition1 = Exhibition(101, "Egyptian Mummies: Secrets of the Pharaohs", "3 months", "South Wing")

# Test adding artwork to the exhibition
artwork2 = Artwork(2, "Mask of Tutankhamun", "Unknown Artist", "1323 BC", "Iconic funerary mask", "South Wing")
exhibition1.add_artwork(artwork2)

# Test attribute access
print(f"Exhibition ID: {exhibition1.id}")
print(f"Name: {exhibition1.name}")
print(f"Location: {exhibition1.location}")

# Print the first artwork in the exhibition (assuming the list is not empty)
if exhibition1.artworks:
    first_artwork = exhibition1.artworks[0]
print(f"First Artwork Title: {first_artwork.title}")

