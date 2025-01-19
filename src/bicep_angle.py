import cv2
import math
import mediapipe as mp

class bicepCurl():
    def __init__(self, mode=False, upBody=True, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode 
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode, model_complexity=self.upBody, smooth_landmarks=self.smooth,
                                     min_detection_confidence=self.detectionCon, min_tracking_confidence=self.trackCon)
    
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img
    
    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList
    
    def findAngle(self, img, p1, p2, p3, draw=True):
        pass

    def findAngle(self, img, p1, p2, p3, p4, draw=True):
        _, x1, y1 = self.lmList[p1]
        _, x2, y2 = self.lmList[p2]
        _, x3, y3 = self.lmList[p3]
        _, x4, y4 = self.lmList[p4]
        
        angle = math.degrees(math.atan2(y4 - y3, x4 - x3) - 
                            math.atan2(y2 - y3, x2 - x3))
        
        if angle < 0:
            angle += 360
            
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
            cv2.line(img, (x2, y2), (x3, y3), (0, 255, 255), 2)
            cv2.line(img, (x3, y3), (x4, y4), (0, 255, 255), 2)
            cv2.circle(img, (x1, y1), 5, (0, 255, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 10, (0, 255, 2555), 2)
            cv2.circle(img, (x2, y2), 5, (0, 255, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (0, 255, 255), 2)
            cv2.circle(img, (x3, y3), 5, (0, 255, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 10, (0, 255, 255), 2)
            cv2.circle(img, (x4, y4), 5, (0, 255, 255), cv2.FILLED)
            cv2.circle(img, (x4, y4), 10, (0, 255, 255), 2)
            # cv2.putText(img, str(int(angle)), (x3 + 20, y3 + 50), 
            #             cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
            
        return angle
        