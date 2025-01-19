import cv2
import math
import PoseModule

def findAngle(self, img, p1, p2, p3, p4, p5, p6, draw=True):
    _, x1, y1 = self.lmList[p1]
    _, x2, y2 = self.lmList[p2]
    _, x3, y3 = self.lmList[p3]
    _, x4, y4 = self.lmList[p4]
    _, x5, y5 = self.lmList[p5]
    _, x6, y6 = self.lmList[p6]
    
    angle1 = math.degrees(math.atan2(y5 - y3, x5 - x3) - 
                         math.atan2(y1 - y3, x1 - x3))

    angle2 = math.degrees(math.atan2(y6 - y5, x6 - x5) - 
                         math.atan2(y3 - y5, x3 - x5))
    
    if angle1 < 0:
        angle1 += 360
        
    if angle2 < 0:
        angle2 += 360
        
    if draw:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
        cv2.line(img, (x3, y3), (x4, y4), (0, 255, 255), 2)
        cv2.line(img, (x1, y1), (x3, y3), (0, 255, 255), 2)
        cv2.line(img, (x3, y3), (x5, y5), (0, 255, 255), 2)
        cv2.line(img, (x5, y5), (x6, y6), (0, 255, 255), 2)
        cv2.circle(img, (x1, y1), 5, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (x1, y1), 10, (0, 255, 2555), 2)
        cv2.circle(img, (x2, y2), 5, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (0, 255, 255), 2)
        cv2.circle(img, (x3, y3), 5, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 10, (0, 255, 255), 2)
        cv2.circle(img, (x4, y4), 5, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (x4, y4), 10, (0, 255, 255), 2)
        cv2.circle(img, (x5, y5), 5, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (x5, y5), 10, (0, 255, 255), 2)
        cv2.circle(img, (x6, y6), 5, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (x6, y6), 10, (0, 255, 255), 2)
        cv2.putText(img, str(int(angle2)), (x3 + 20, y3 + 50), 
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        
    return angle1, angle2
        
PoseModule.poseDetector.findAngle = findAngle # monkey patching