# Importamos Librerias
import pyqrcode
import png
from pyqrcode import QRCode

# CODIGOS QR ID
# Variables
cod=1234

# Generando codigos QR
while cod <= 1238:

    # id = str('j') + str(cod)
    roster = cod
    id = '65' + str(cod)
    # Creamos los QR
    qr = pyqrcode.create(65 and id, error='L')
    # Guardamos los codigos
    qr.png('A' + str(roster) +  '.png', scale = 6)
    # Aumentamos la variable cod
    cod = cod + 1