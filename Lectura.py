# Importamos libreria para lecturas
import cv2
import pyqrcode
import png
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
import numpy as np

# Creacion de videocaptura
cap = cv2.VideoCapture(0)


# Bucle para leer indefinidamente los QR
while True:
    # Leemos los frames
    ret, frame = cap.read()

    # Leemos los codigos QR
    for codes in decode(frame):
        # Extraemos info
        # info = codes.data

        # Decodificamos
        info = codes.data.decode('utf-8')

        # Tipo de persona LETRA
        tipo = info[0:2]
        tipo = int(tipo)

        # Extraemos las coordenadas
        pts = np.array([codes.polygon], np.int32)
        xi, yi = codes.rect.left, codes.rect.top

        # Redimensionamos
        pts = pts.reshape((-1,1,2))

        # Repetir para genear disintas lecturas de LETRAS como se muestra en ejemplo del if
        if tipo == 65: # J->74 # E->65
            # Dibujamos contorno del QR
            cv2.polylines(frame, [pts], True, (255, 255, 0,), 5)
            cv2.putText(frame, 'A0' + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 55, 0), 2)
            print(" El usuario es accionista de la empresa \n"
                  " Numero de identificacion: A", str(info[2:]))
            
    # Mostramos FPS
    cv2.imshow(" LECTOR DE QR", frame)
    # Leemos el teclado
    t = cv2.waitKey(5)
    if t == 27:
        break

cv2.destroyAllWindows()
cap.release()