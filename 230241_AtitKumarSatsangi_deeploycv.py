import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load pre-trained YOLOv8 model
model = YOLO('yolov9s.pt')  # Use yolov8s.pt or other variants as needed

# Define classes of interest (you might need to adjust these based on your specific model's classes)
flags_of_interest_indices = [0, 1]  # Placeholder for class indices of Poland and Indonesia flags

# Function to detect and classify flags
def detect_flag(image_path, conf_threshold=0.5):
    results = model(image_path)

    # Accessing results and converting to a more usable format
    results = results[0].boxes.data.cpu().numpy()

    img = cv2.imread(image_path)
    detected_flags = []
    for result in results:
        xmin, ymin, xmax, ymax, conf, cls = result
        if conf > conf_threshold and int(cls) in flags_of_interest_indices:
            detected_flags.append(int(cls))
            # Draw bounding box and label
            cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
            label = 'Poland flag' if int(cls) == flags_of_interest_indices[0] else 'Indonesia flag'
            cv2.putText(img, f'{label} {conf:.2f}', (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display results
    plt.figure(figsize=(12, 8))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(f'Detection Results for {image_path}')
    plt.axis('off')
    plt.show()

    # Return classification result
    if len(detected_flags) == 0:
        return "No flag detected."
    elif flags_of_interest_indices[0] in detected_flags:
        return "Detected flag: Poland"
    elif flags_of_interest_indices[1] in detected_flags:
        return "Detected flag: Indonesia"
    else:
        return "No relevant flag detected."

# Path to the image
image_path = 'p1.jpg'  # Replace with your image path

# Process the single image
classification_result = detect_flag(image_path, conf_threshold=0.85)

# Output classification result
print(classification_result)
