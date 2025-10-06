import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.5, maxHands=2)
cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 400)

while True:
    ret, img = cap.read()
    if not ret:
        break
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands and hands[0]['type'] == 'Left':
        fingers = detector.fingersUp(hands[0])
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers: {totalFingers}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        if totalFingers == 5:
            pyautogui.keyDown("right")
            '''pyautogui.keyDown("up")
            pyautogui.keyDown("down")'''
            pyautogui.keyUp("left")
        elif totalFingers == 0:
            pyautogui.keyDown("left")
            '''pyautogui.keyDown("top")
            pyautogui.keyDown("down")'''
            pyautogui.keyUp("right")
        '''elif totalFingers == 5:
            pyautogui.keyDown("left")
            pyautogui.keyDown("right")
            pyautogui.keyDown("down")
            pyautogui.keyUp("up")
        elif totalFingers == 0:
            pyautogui.keyDown("left")
            pyautogui.keyDown("up")
            pyautogui.keyDown("right")
            pyautogui.keyUp("down")'''

    cv2.imshow('chandu', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
