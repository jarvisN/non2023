import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    ab = [b.x - a.x, b.y - a.y]
    bc = [c.x - b.x, c.y - b.y]

    cosine_angle = (ab[0]*bc[0] + ab[1]*bc[1]) / (math.sqrt(ab[0]**2 + ab[1]**2) * math.sqrt(bc[0]**2 + bc[1]**2))
    angle = math.degrees(math.acos(cosine_angle))

    return angle

# Define function to interpret landmarks as fingers up
def interpret_landmarks(landmarks):
    # Get the tip of the thumb, index, middle, ring, and pinky fingers
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    # Check which fingers are up
    fingers_up = [
        thumb_tip.x > landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x,
        index_tip.y < landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y,
        middle_tip.y < landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y,
        ring_tip.y < landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y,
        pinky_tip.y < landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y,
    ]
    
     # Get the landmarks for the thumb
    thumb_mcp = landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
    thumb_pip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

    # Calculate the angles
    angle_mcp = calculate_angle(thumb_mcp, thumb_pip, thumb_tip)
    angle_pip = calculate_angle(thumb_pip,thumb_tip,thumb_mcp)
    
    # Get the landmarks for each finger
    finger_landmarks = [
        [mp_hands.HandLandmark.THUMB_MCP, mp_hands.HandLandmark.THUMB_IP, mp_hands.HandLandmark.THUMB_TIP],
        [mp_hands.HandLandmark.INDEX_FINGER_MCP, mp_hands.HandLandmark.INDEX_FINGER_PIP, mp_hands.HandLandmark.INDEX_FINGER_TIP],
        [mp_hands.HandLandmark.MIDDLE_FINGER_MCP, mp_hands.HandLandmark.MIDDLE_FINGER_PIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
        [mp_hands.HandLandmark.RING_FINGER_MCP, mp_hands.HandLandmark.RING_FINGER_PIP, mp_hands.HandLandmark.RING_FINGER_TIP],
        [mp_hands.HandLandmark.PINKY_MCP, mp_hands.HandLandmark.PINKY_PIP, mp_hands.HandLandmark.PINKY_TIP],
    ]

    # Calculate and print the angles for each finger
    for i, (mcp, pip, tip) in enumerate(finger_landmarks):
        angle_mcp = calculate_angle(landmarks.landmark[mcp], landmarks.landmark[pip], landmarks.landmark[tip])
        angle_pip = calculate_angle(landmarks.landmark[pip], landmarks.landmark[tip], landmarks.landmark[mcp])
        
        print(f'Finger {i} - MCP angle: {angle_mcp:.2f} degrees, PIP angle: {angle_pip:.2f} degrees')

    


    return fingers_up



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
            fingers_up = interpret_landmarks(hand_landmarks)
            cv2.putText(frame, f'Thumb: {"Up" if fingers_up[0] else "Down"}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, f'Index: {"Up" if fingers_up[1] else "Down"}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, f'Middle: {"Up" if fingers_up[2] else "Down"}', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, f'Ring: {"Up" if fingers_up[3] else "Down"}', (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, f'Pinky: {"Up" if fingers_up[4] else "Down"}', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    # Display the frame
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release Resources
cap.release()
cv2.destroyAllWindows()
