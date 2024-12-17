from PIL import Image
import numpy as np

def detect_flag(image_path):
    # Load the image and convert it to an array
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)

    # Divide the image into two equal horizontal halves
    height, width, _ = img_array.shape
    top_half = img_array[:height//2, :, :]
    bottom_half = img_array[height//2:, :, :]

    # Calculate average brightness of the top and bottom halves
    top_brightness = np.mean(top_half)
    bottom_brightness = np.mean(bottom_half)

    # Compare the brightness levels
    if top_brightness < bottom_brightness:
        print("The flag is Indonesia (Top is Red, Bottom is White).")
    elif top_brightness > bottom_brightness:
        print("The flag is Poland (Top is White, Bottom is Red).")
    else:
        print("Cannot determine the flag.")

# Example usage
image_path = "p2.jpg"  # Replace with your image file
detect_flag(image_path)
