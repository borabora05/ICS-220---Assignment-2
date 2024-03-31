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
