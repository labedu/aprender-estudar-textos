FROM ubuntu:22.04
RUN apt update -y
RUN apt install -y python2 python2-dev build-essential python3-pip python-is-python3
RUN pip3 install pip -U
RUN apt install -y libsm6 libxext6 libgl1
RUN apt install -y tesseract-ocr-por
COPY . /app
WORKDIR /app
# RUN pip install pillow
# RUN pip3 install pytesseract
# RUN pip install opencv-contrib-python
# RUN pip install numpy
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
