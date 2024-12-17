from PIL import Image
import numpy as np

def detect_flag(image_path):
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)

    height, width, _ = img_array.shape
    top_half = img_array[:height//2, :, :]
    bottom_half = img_array[height//2:, :, :]

    top_brightness = np.mean(top_half)
    bottom_brightness = np.mean(bottom_half)

    if top_brightness < bottom_brightness:
        print("The flag is Indonesia (Top is Red, Bottom is White).")
    elif top_brightness > bottom_brightness:
        print("The flag is Poland (Top is White, Bottom is Red).")
    else:
        print("Cannot determine the flag.")


image_path = "p2.jpg"  
detect_flag(image_path)
