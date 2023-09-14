from PIL import Image

# Open an image file
image_path = "DSCF5701.jpeg"  # Replace with the path to your image file
image = Image.open(image_path)

# Get dimensions
width, height = image.size
print(f"Image Dimensions: Width = {width}, Height = {height}")

# Show the image
image.show()