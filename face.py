import cv2,mediapipe as mp

class FaceDetector():

    def __init__(self, minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon) # 加载人脸检测模块

    def findFaces(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB) # 获取结果
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box # 脸部的位置信息
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih) # 反归一化
                bboxs.append([id, bbox, detection.score])
                img = self.fancyDraw(img,bbox) # 绘制框图
                break
        return img, bboxs

    def fancyDraw(self, img, bbox, l=30, t=2, rt= 1):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h
        # 左上
        cv2.line(img, (x, y), (x + l, y), (255,191,0), t)
        cv2.line(img, (x, y), (x, y+l), (255,191,0), t)
        # 右上
        cv2.line(img, (x1, y), (x1 - l, y), (255,191,0), t) 
        cv2.line(img, (x1, y), (x1, y+l), (255,191,0), t)
        # 左下
        cv2.line(img, (x, y1), (x + l, y1), (255,191,0), t)
        cv2.line(img, (x, y1), (x, y1 - l), (255,191,0), t)
        # 右下
        cv2.line(img, (x1, y1), (x1 - l, y1), (255,191,0), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (255,191,0), t)
        return img