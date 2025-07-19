import cv2

img = cv2.imread('DATA/00-puppy.jpg')

while True:
    cv2.imshow('Puppy', img)
    
    # If we waited at least one second and pressed the Esc key
    # 0xFF acts as a key listener
    # 27 is the ASCII value of Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()