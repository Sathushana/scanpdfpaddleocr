import pytesseract
import cv2
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def correct_image_rotation(image_path):
    try:
        image = Image.open(image_path)
        osd = pytesseract.image_to_osd(image)
        rotation_angle = int([line for line in osd.split('\n') if 'Rotate' in line][0].split(':')[1].strip())
        
        if rotation_angle != 0:
            print(f"Image is rotated by {rotation_angle} degrees. Correcting it...")
            corrected_image = image.rotate(-rotation_angle, expand=True)
            
            return corrected_image
        else:
            print("Image is already correctly oriented.")
            return image
    except Exception as e:
        return e
        
    
def preprocess_image(image_path):
    try:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #gray = cv2.equalizeHist(gray)
        adjusted = cv2.convertScaleAbs(gray, alpha=1, beta=30)
        denoised = cv2.GaussianBlur(adjusted, (1, 1), 0)
        #kernel = np.ones((5, 5), np.uint8)
        #img_erosion = cv2.erode(denoised, kernel, iterations=1)
        #print("Preprocess....")
        return denoised
    except Exception as e:
        return e