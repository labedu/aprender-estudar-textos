import pytesseract

import shutil
import os
import random

# FROM ubuntu:latest
# MAINTAINER Rick Torzynski "ricktorzynski@gmail.com"
# RUN apt-get update -y
# RUN apt-get install -y python-pip python-dev build-essential
# RUN apt update && apt install -y libsm6 libxext6
# RUN apt-get -y install tesseract-ocr
# COPY . /app
# WORKDIR /app
# RUN pip install pillow
# RUN pip install pytesseract
# RUN pip install opencv-contrib-python
# RUN pip install -r requirements.txt
# ENTRYPOINT ["python"]
# CMD ["app.py"]

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

image_path_in_colab= '../imgs/a0.png'
extractedInformation = pytesseract.image_to_string(Image.open(image_path_in_colab), lang='por')
print(extractedInformation)


if __name__ == '__main__':
    print('Hello Labedu!')
