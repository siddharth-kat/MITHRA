import cv2
import face_recognition

def detect_faces(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Find all face locations in the image
    face_locations = face_recognition.face_locations(image)

    # Find facial landmarks for each face
    face_landmarks_list = face_recognition.face_landmarks(image)

    # Create a list to store face information
    faces_info = []

    # Iterate through each detected face
    for (top, right, bottom, left), face_landmarks in zip(face_locations, face_landmarks_list):
        # Calculate face width and height
        face_width = right - left
        face_height = bottom - top

        # Calculate face center coordinates
        face_center_x = (left + right) // 2
        face_center_y = (top + bottom) // 2

        # Prepare face information dictionary
        face_info = {
            "Top": top,
            "Right": right,
            "Bottom": bottom,
            "Left": left,
            "Width": face_width,
            "Height": face_height,
            "Center_X": face_center_x,
            "Center_Y": face_center_y,
            "Landmarks": face_landmarks
        }

        # Append face information to the list
        faces_info.append(face_info)

    return faces_info

def main():
    image_path = "path/to/your/image.jpg"  # Replace with your image path

    # Detect faces and gather information
    faces_info = detect_faces(image_path)

    # Print face information
    for idx, face_info in enumerate(faces_info, start=1):
        print(f"Face {idx} Information:")
        for key, value in face_info.items():
            print(f"{key}: {value}")
        print("\n")

main()