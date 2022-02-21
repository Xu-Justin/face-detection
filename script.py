import cv2

class Predictor():
    
    cascade = 'haarcascade/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade)    
    
    def preprocess(self, image_bgr):
        image = image_bgr.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.GaussianBlur(image, (3,3), cv2.BORDER_DEFAULT)
        image = cv2.equalizeHist(image)
        return image
    
    def draw(self, image_bgr, bouding_boxes):
        image = image_bgr.copy()
        for (x,y,w,h) in bouding_boxes:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
        return image
        
    def predict(self, image_bgr):
        image = image_bgr.copy()
        gray_image = self.preprocess(image)
        bouding_boxes = self.face_cascade.detectMultiScale(gray_image, 1.3, 5)
        result = self.draw(image, bouding_boxes)
        return result

def load_image(path):
    image_bgr = cv2.imread(path)
    return image_bgr

def save_image(path, image_bgr):
    cv2.imwrite(path, image_bgr)
    
if __name__ == '__main__':
    predictor = Predictor()
    
    input_path = input("Image Path: ")
    image = load_image(input_path)
    result = predictor.predict(image)
    
    output_path = input("Output Path: ")
    save_image(output_path, result)