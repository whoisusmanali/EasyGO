import cv2
from simple_facerec import SimpleFacerec
import math
import cvzone

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(1)

count=0
record = []
while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        cv2.putText(frame, "Welcome to EasyGO", (800, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (500, 100, 100), 4)
        if count <20:
            count = count+1
        if count ==20:
            if name != "Unknown":
                record.append(name)
                for records in record:
                    if records == name:
                    # pass
                    # print(records)
                        cv2.putText(frame, "You are done with boarding", (100, 50), cv2.FONT_HERSHEY_DUPLEX, 1,
                                (500, 100, 100),
                                4)
                    else:
                        print(name)







    cv2.putText(frame, f'{count}', (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (500, 100, 100), 4)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()