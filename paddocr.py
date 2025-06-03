#import easyocr

#reader = easyocr.Reader(['en'])
#result = reader.readtext(r'D:\Hexabins_AI_ML_Intern\behaviourapp_ocr\Scanned_PDF\Behaviour_ocr_scanned_Pdf\preprocessImage\img_1.jpg')
#texts = [text[1] for text in result]

#print(texts)
#import paddle
#from paddle import PaddleOcr

#clocr = PaddleOCR(use_textline_orientation=True, lang='en')

from paddleocr import PaddleOCR
import os
import time
from PIL import Image

ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)


def resize_image(image_path, max_dim=2048):
    img = Image.open(image_path)
    img.thumbnail((max_dim, max_dim))
    img.save(image_path)

#resize_image(r"D:\Hexabins_AI_ML_Intern\behaviourapp_ocr\Scanned_PDF\Behaviour_ocr_scanned_Pdf\preprocessImage\img_1.jpg")

"""
result = ocr.predict(
    input= r"D:\Hexabins_AI_ML_Intern\behaviourapp_ocr\Scanned_PDF\Behaviour_ocr_scanned_Pdf\preprocessImage\img_1.jpg"
)
recognized_texts = result[0]['rec_texts']


for text in recognized_texts:
    print(text)
"""

def extract_text_paddleocr():
    folder_path = r"D:\Hexabins_AI_ML_Intern\behaviourapp_ocr\Scanned_PDF\Behaviour_ocr_scanned_Pdf\preprocessImage"
    all_text = []
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            resize_image(file_path)
            result = ocr.predict(input=file_path)
            recognized_texts = result[0]['rec_texts']
            """
            for text in recognized_texts:
                print(text)"""
            text_string = " ".join(recognized_texts)
            all_text.append(text_string)
            
    return print("\n\n".join(all_text))

          
"""
start_time = time.time()
extract_text_paddleocr()
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Processing time of OCR: {elapsed_time:.4f} [sec]")"""

#extract_text_paddleocr()


