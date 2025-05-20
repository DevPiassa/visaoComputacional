import cv2

img = cv2.imread('videos/farol.jpg')
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

print(img)

cv2.imshow('imagem',img)
cv2.imshow('imagem cinza',imgCinza)

cv2.waitKey(0)
cv2.destroyAllWindows()