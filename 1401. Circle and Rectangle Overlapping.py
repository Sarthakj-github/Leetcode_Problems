class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        X1=(radius**2)-(y1-yCenter)**2
        X2=(radius**2)-(y2-yCenter)**2
        Y1=(radius**2)-(x1-xCenter)**2
        Y2=(radius**2)-(x2-xCenter)**2

        if X1>=0:
            X1=X1**(0.5)+xCenter
            if x1<=X1<=x2:
                return True
        if X2>=0:
            X2=X2**(0.5)+xCenter
            if x1<=X2<=x2:
                return True
        if Y1>=0:
            Y1=Y1**(0.5)+yCenter
            if y1<=Y1<=y2:
                return True
        if Y2>=0:
            Y2=Y2**(0.5)+yCenter
            if y1<=Y2<=y2:
                return True

        if x1<=xCenter<=x2 and y1<=yCenter<=y2:
            return True
        
        d1= ((xCenter-x1)**2+(yCenter-y1)**2)**(0.5)
        d2= ((xCenter-x2)**2+(yCenter-y2)**2)**(0.5)

        if d1<=radius or d2<=radius:
            return True
        return False
