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
