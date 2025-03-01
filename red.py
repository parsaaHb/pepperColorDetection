import cv2 as cv

img = cv.imread('photo/k2.jpg')

#digidaga boom 
img = cv.resize(img , (400,400))
b , g , r = img[200 , 200]

#defining a range 
low_red= (0, 0, 150)  
high_red = (100, 100, 255)  

#if all the items are true then the value will be True else its false 
X= (low_red[0] <= b <= high_red[0] and
             low_red[1] <= g <= high_red[1] and
             low_red[2] <= r <= high_red[2])

#obvious
print("yes" if X else "NO")

#unnessesery bs 
cv.imshow('image' , img)
cv.waitKey(0)
cv.destroyAllWindows()