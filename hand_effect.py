import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

# Canvas for hand trails
trail = np.zeros((480, 640, 3), dtype=np.uint8)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    h, w, c = frame.shape

    # Resize trail if needed
    if trail.shape[:2] != (h, w):
        trail = np.zeros((h, w, 3), dtype=np.uint8)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    # Fade previous trails slowly
    trail = cv2.addWeighted(trail, 0.92, np.zeros_like(trail), 0, 0)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Index fingertip
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)

            # Draw glowing circle
            cv2.circle(trail, (x, y), 20, (255, 0, 255), -1)
            cv2.circle(trail, (x, y), 40, (255, 0, 255), 2)

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # Blur trail for glow effect
    glow = cv2.GaussianBlur(trail, (31, 31), 0)

    # Combine webcam + glow
    output = cv2.addWeighted(frame, 1.0, glow, 0.8, 0)

    cv2.imshow("Magic Hand Effect", output)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
