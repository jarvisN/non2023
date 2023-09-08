import cv2
import mediapipe as mp

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Define function to interpret landmarks as numbers
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

    # Interpret the number of fingers up as the number
    number = sum(fingers_up)
    return number

# Capture Video
cap = cv2.VideoCapture(0)

# Process Frames
while cap.isOpened():
    ret, frame = cap.read()
    # Convert the frame to RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the frame
    result = hands.process(image_rgb)
    # Draw hand landmarks and interpret number
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            number = interpret_landmarks(hand_landmarks)
            cv2.putText(frame, str(number), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    # Display the frame
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release Resources
cap.release()
cv2.destroyAllWindows()
