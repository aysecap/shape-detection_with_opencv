import numpy as np
import cv2



img = cv2.imread("shapess.png",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh1 = cv2.threshold(img,140, 255, cv2.THRESH_TOZERO)
Canny = cv2.Canny(thresh1,70,150)


#filter = cv2.fastNlMeansDenoising(img, None,10,10,10)  //sadece yeni buldum bi kaynakta gördüğüm filtre deneme amaçlı sonuç olumlu

contours,_ = cv2.findContours(Canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


for cnt in contours :
    (x,y,w,h) = cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)
    aspectRatio = float(w) / float(h)
    extent = area / float(w*h)
    perimeter = cv2.arcLength(cnt, True)

    print("perimeter"+ str(perimeter))
    print("area"+ str(area))
    print("h"+ str(h))
    print("w"+ str(w))

    cv2.drawContours(thresh1,[cnt],-1,(255,0,0),3)
    shape=""
    if extent < 0.80 :
        if 0.90 < aspectRatio <1.1 :
            shape = "Circle"
        elif area - (area * 5/ 100) <= (w * h / 2) <= area + (area * 5/ 100):
            shape = "Triangle"
        elif area - (area * 25 / 100) <=  5.1961 * ((perimeter / 6)**2) / 2 <= area + (area * 25 / 100):
            shape = "Pentagon"
        elif area - (area * 20 / 100) <=  (perimeter / 5) * (h/2) / 2 * 5 <= area + (area * 20 / 100):
            shape = "Hexagon"


    elif aspectRatio <= 1.70:
         shape = "Rectangle"





    cv2.putText(thresh1, shape, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 100, 170), 2)
    print("Contour #{}, extent={:.2f}".format(cnt + 1, extent))
    cv2.drawContours(thresh1, cnt, -1, (0, 0, 255), 2)


cv2.imshow("Test2",Canny)
cv2.imshow("Original",img)
cv2.imshow("thresh", thresh1)

#cv2.imshow("Filter", filter)  kaynaktan bulup denediğim bir fonksiyon çıktısı için
cv2.waitKey(0)