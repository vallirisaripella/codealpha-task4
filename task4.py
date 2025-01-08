import random
import time

# Simulated "video frame" dimensions
FRAME_WIDTH = 20
FRAME_HEIGHT = 10

# Classes to detect
CLASSES = ["Car", "Person", "Bike"]

# Generate a random frame with simulated objects
def generate_frame():
    frame = [[" " for _ in range(FRAME_WIDTH)] for _ in range(FRAME_HEIGHT)]
    num_objects = random.randint(1, 5)
    objects = []

    for _ in range(num_objects):
        obj_class = random.choice(CLASSES)
        x = random.randint(0, FRAME_WIDTH - 4)
        y = random.randint(0, FRAME_HEIGHT - 2)
        width = random.randint(2, 4)
        height = random.randint(1, 2)
        objects.append((obj_class, x, y, width, height))

        # Draw the object on the frame
        for i in range(y, y + height):
            for j in range(x, x + width):
                if 0 <= i < FRAME_HEIGHT and 0 <= j < FRAME_WIDTH:
                    frame[i][j] = obj_class[0]  # Represent with the first letter of the class

    return frame, objects

# Display a frame
def display_frame(frame):
    print("\n" + "-" * FRAME_WIDTH)
    for row in frame:
        print("".join(row))
    print("-" * FRAME_WIDTH)

# Simulated object detection
def detect_objects(objects):
    detected = []
    for obj in objects:
        obj_class, x, y, width, height = obj
        detected.append({
            "class": obj_class,
            "bounding_box": (x, y, width, height)
        })
    return detected

# Object tracking: assigns IDs to detected objects
def track_objects(detections, prev_tracks):
    new_tracks = {}
    for i, detection in enumerate(detections):
        new_tracks[f"ID-{i}"] = detection
    return new_tracks

# Main loop: Simulate real-time detection and tracking
def main():
    prev_tracks = {}
    print("Starting object detection and tracking simulation... Press Ctrl+C to stop.\n")
    try:
        while True:
            frame, objects = generate_frame()
            display_frame(frame)
            
            detections = detect_objects(objects)
            tracks = track_objects(detections, prev_tracks)
            
            print("\nDetected Objects:")
            for track_id, data in tracks.items():
                bbox = data["bounding_box"]
                print(f"{track_id}: {data['class']} at {bbox}")
            
            prev_tracks = tracks
            time.sleep(1)  # Simulate real-time processing
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

# Run the simulation
main()


