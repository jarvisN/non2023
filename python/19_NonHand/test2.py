import cv2
import mediapipe as mp
import math
import json
import serial
import random

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    ab = [b.x - a.x, b.y - a.y]
    bc = [c.x - b.x, c.y - b.y]

    cosine_angle = (ab[0] * bc[0] + ab[1] * bc[1]) / (math.sqrt(ab[0] ** 2 + ab[1] ** 2) * math.sqrt(bc[0] ** 2 + bc[1] ** 2))
    angle = math.degrees(math.acos(cosine_angle))

    return angle

# Define function to interpret landmarks as fingers up
def interpret_landmarks(landmarks):
    # Initialize an empty list to store the angles for all fingers
    finger_angles = []

    # Iterate through each finger
    for finger_landmark in mp_hands.HandLandmark:
        # Check if the landmark is for a finger tip
        if "TIP" in finger_landmark.name:
            tip_landmark = landmarks.landmark[finger_landmark]
            mcp_landmark = landmarks.landmark[finger_landmark.value - 2]  # MCP (Metacarpophalangeal) landmark
            pip_landmark = landmarks.landmark[finger_landmark.value - 1]  # PIP (Proximal Interphalangeal) landmark

            # Calculate the angles
            angle_mcp = calculate_angle(mcp_landmark, pip_landmark, tip_landmark)
            # angle_pip = calculate_angle(pip_landmark, tip_landmark, mcp_landmark)

            # Append the angles to the finger_angles list
            # finger_angles.append((angle_mcp, angle_pip))
            finger_angles.append(angle_mcp)

    return finger_angles

# Capture Video
cap = cv2.VideoCapture(0)

# Process Frames
while cap.isOpened():
    ret, frame = cap.read()
    # Convert the frame to RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the frame
    result = hands.process(image_rgb)
    # Draw hand landmarks and interpret fingers up
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            finger_angles = interpret_landmarks(hand_landmarks)

            # # Create a dictionary to store finger angles
            # finger_data = {
            #     "thumb": finger_angles[0],
            #     "index": finger_angles[1],
            #     "middle": finger_angles[2],
            #     "ring": finger_angles[3],
            #     "pinky": finger_angles[4]
            # }

            # # Convert the finger data to JSON
            # json_data = json.dumps(finger_data)
            # # print(json_data)

            # Open a serial connection to Arduino (Replace 'COMX' with your Arduino's COM port)
            ser = serial.Serial('COM19', baudrate=9600)  # Replace 'COMX' with your Arduino's COM port

            # # Send the JSON data to Arduino
            # ser.write(json_data.encode())
            # print(json_data.encode())

            # # Close the serial connection
            # ser.close()
            random_number = random.randint(0, 100)
            print(random_number)
            ser.write(random_number)
            ser.close()

    # Display the frame
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release Resources
cap.release()
cv2.destroyAllWindows()
