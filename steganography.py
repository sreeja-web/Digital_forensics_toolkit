
import streamlit as st
from PIL import Image
import numpy as np
import wave
import cv2
import os

def stego_ui():
    st.title("🔐 Steganography (Decode Only)")

    type_choice = st.selectbox("Select Media Type", ["Image", "Audio", "Video"])

    # 🖼️ IMAGE
    if type_choice == "Image":
        file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

        if file and st.button("Decode Image"):
            img = Image.open(file).convert("RGB")
            pixels = np.array(img)

            binary = ""
            for row in pixels:
                for pixel in row:
                    for c in pixel:
                        binary += str(c & 1)

            chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
            msg = "".join([chr(int(c, 2)) for c in chars if int(c, 2) < 128])

            st.success(msg)

    # 🎵 AUDIO
    elif type_choice == "Audio":
        file = st.file_uploader("Upload WAV", type=["wav"])

        if file and st.button("Decode Audio"):
            audio = wave.open(file, 'rb')
            frames = audio.readframes(audio.getnframes())

            binary = "".join([str(b & 1) for b in frames])

            chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
            msg = "".join([chr(int(c, 2)) for c in chars if int(c, 2) < 128])

            st.success(msg)

    # 🎥 VIDEO
    elif type_choice == "Video":
        file = st.file_uploader("Upload Video", type=["mp4", "avi"])

        if file:
            temp = "temp.mp4"
            with open(temp, "wb") as f:
                f.write(file.read())

            if st.button("Decode Video"):
                cap = cv2.VideoCapture(temp)
                binary = ""

                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break

                    for row in frame:
                        for pixel in row:
                            binary += str(pixel[0] & 1)

                cap.release()

                chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
                msg = "".join([chr(int(c, 2)) for c in chars if int(c, 2) < 128])

                st.success(msg)

