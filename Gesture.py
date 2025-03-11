import mediapipe as mp
import cv2
import time

video = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

tip = [4, 8, 12, 16, 20]
fingerName = ['Thumb', 'Index Finger', 'Middle Finger', 'Ring Finger', 'Little Finger']

prevTime = 0

while True:
    success, img = video.read()
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    if len(lmList):
        fingers = []

        if ((lmList[tip[0]][1] > lmList[tip[0] - 1][1] and lmList[tip[0]][2] <= lmList[tip[0] - 1][2]) or (
                lmList[tip[0]][1] < lmList[tip[0] - 1][1] and lmList[tip[0]][2] >= lmList[tip[0] - 1][2])):
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmList[tip[id]][2] < lmList[tip[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = sum(fingers)  # to count number of fingers open

        if totalFingers == 1:
            for fin in range(5):
                if fingers[fin] == 1:
                    upFinger = fingerName[fin]
                    cv2.putText(img, str(upFinger), (275, 445), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        elif totalFingers == 5:
            cv2.putText(img, 'Palm', (275, 445), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        elif totalFingers == 0:
            cv2.putText(img, 'Fist', (275, 445), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

        cv2.putText(img, str(totalFingers), (45, 45), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    currTime = time.time()
    fps = 1 / (currTime - prevTime)
    prevTime = currTime

    cv2.putText(img,str(int(fps)), (575, 45), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
