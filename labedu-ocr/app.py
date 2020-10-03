from flask import Flask, request, jsonify
from werkzeug import secure_filename
import os
import sys
from PIL import Image
import pytesseract
import argparse
import cv2

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024


def process_file(file_path):
   #f = request.files['file2']
   # print(f)

   f = file_path

   filename = secure_filename(f.filename)
   print(filename)


   filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
   f.save(filepath)


   # converta imagem em preto e branco
   image = cv2.imread(filepath)
   gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   # aplicar threshould
   gray = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

   # remove borrado
   gray = cv2.medianBlur(gray, 3)

   # salve a imagem em /tmp
   ofilename = os.path.join(app.config['UPLOAD_FOLDER'], "{}.png".format(os.getpid()))
   cv2.imwrite(ofilename, gray)

   # aplica o ocr
   text = pytesseract.image_to_string(Image.open(ofilename), lang='por')

   if len(text.strip()) < 8:
      text_raw = pytesseract.image_to_string(Image.open(filepath), lang='por').strip()
      if len(text_raw) > len(text):
         text = text_raw


   os.remove(filepath)
   os.remove(ofilename)

   # return jsonify({ 'text': text} )
   return {'filename': filename, 'text': text}



@app.route('/imgtotext', methods = ['POST'])
def img_to_text():
    if request.method == 'POST':
        files = request.files
        answer = []
        for f in files:
            answer.append(process_file(files[f]))

        return jsonify(answer)



@app.route('/imgtobox', methods = ['POST'])
def file_to_box():
   if request.method == 'POST':
      f = request.files['file']

      filename = secure_filename(f.filename)

      filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
      f.save(filepath)

      # converta imagem em preto e branco
      image = cv2.imread(filepath)
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      # aplicar threshould
      gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

      # remove borrado
      gray = cv2.medianBlur(gray, 3)

      # salve a imagem em /tmp
      ofilename = os.path.join(app.config['UPLOAD_FOLDER'],"{}.png".format(os.getpid()))
      cv2.imwrite(ofilename, gray)

      # aplica o ocr
      text = pytesseract.image_to_data(Image.open(ofilename), lang='por')

      #os.remove(ofilename)
      import shutil
      shutil.rmtree('/tmp')

      return text

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5001, debug=True)
