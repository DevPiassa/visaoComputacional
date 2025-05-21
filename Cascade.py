import cv2

video = cv2.VideoCapture()
ip = "https://***.***.**.***:8080/video" # para abrir webcan do celular "app ipWebcam "
video.open(ip)
classicador = cv2.CascadeClassifier(r'cascades\haarcascade_frontalface_alt.xml')

while True:
    check, img = video.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    objetos = classicador.detectMultiScale(imgGray,minSize=(50,50),scaleFactor=1.5)
    for x,y,l,a in objetos:
        cv2.rectangle(img,(x,y),(x+l,y+a),(255,0,0),2)


    cv2.imshow("img",img)
    key =cv2.waitKey(1)
    if key ==  ord('q'):
        break
