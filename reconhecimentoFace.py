import cv2

camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier(r'cascades/haarcascade_frontalface_default.xml')

while True:
    check, img = camera.read()
    img = imgGray
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objetos = classificador.detectMultiScale(imgGray,minSize=(40,40),scaleFactor = 1.5)

    for x,y,l,a in objetos:
        cv2.rectangle(img,(x,y),(x+l,y+a),(255,0,0),2)

    cv2.imshow('Imagem', img)
    key =cv2.waitKey(1)
    if key ==  ord('q'):
        break
    cv2.waitKey(1)
