import cv2

video = cv2.VideoCapture('videos/runners.mp4')

while True:
    check, img = video.read()
    imgRedin = cv2.resize(img,dsize=(640,420)) 
    cv2.imshow('video', imgRedin)
    cv2.waitKey(0)
    cv2.destroyAllWindows()