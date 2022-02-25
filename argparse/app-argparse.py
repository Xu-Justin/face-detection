import cv2

class Predictor():
    
    cascade = 'haarcascade/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade)    
    
    @staticmethod
    def resize(image):
        width = int(1080)
        height = int(image.shape[0] * (width / image.shape[1]))
        dim = (width, height)
        image = cv2.resize(image, dim)
        return image

    @staticmethod
    def preprocess(image_bgr):
        image = image_bgr.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.GaussianBlur(image, (3,3), cv2.BORDER_DEFAULT)
        image = cv2.equalizeHist(image)
        return image
    
    @staticmethod
    def draw(image_bgr, bouding_boxes):
        image = image_bgr.copy()
        for (x,y,w,h) in bouding_boxes:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
        return image
    
    @staticmethod
    def load_image(path):
        image_bgr = cv2.imread(path)
        return image_bgr

    @staticmethod
    def save_image(path, image_bgr):
        cv2.imwrite(path, image_bgr)

    @classmethod
    def predict(cls, image_bgr):
        image = image_bgr.copy()
        gray_image = cls.preprocess(image)
        bouding_boxes = cls.face_cascade.detectMultiScale(gray_image, 1.3, 5)
        result = cls.draw(image, bouding_boxes)
        return result

def process(source, target):
    image = Predictor.load_image(source)
    image = Predictor.resize(image)
    result = Predictor.predict(image)
    Predictor.save_image(target, result)

import argparse

parser = argparse.ArgumentParser(description='Draw a bounding box on each detected face in an image.')
parser.add_argument('source', metavar='source', type=str, help='path to load image')
parser.add_argument('target', metavar='target', type=str, help='path to save result image')
args = parser.parse_args()

source_path = args.source
target_path = args.target

if __name__=='__main__':
    process(source_path, target_path)