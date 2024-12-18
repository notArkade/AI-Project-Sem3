import cv2
from face_rec_model import modelFaceRec

mfr = modelFaceRec()
mfr.load_encoding_images("images/")

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    face_locations, face_names = mfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)

        # print(face_loc)

    cv2.imshow("FameFrame", frame)

    key = cv2.waitKey(1)
    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()