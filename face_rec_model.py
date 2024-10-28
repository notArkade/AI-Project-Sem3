import face_recognition
import cv2
import os

class modelFaceRec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        self.frame_resizing = 0.25

    