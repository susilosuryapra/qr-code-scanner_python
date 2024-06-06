import cv2
from pyzbar.pyzbar import decode
import time

# Inisialisasi kamera
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Lebar
cam.set(4, 480)  # Tinggi

while True:
    success, frame = cam.read()
    if not success:
        break

    for barcode in decode(frame):
        # Menampilkan tipe dan data dari QR code yang terdeteksi
        print(barcode.type)
        print(barcode.data.decode('utf-8'))
        time.sleep(6)  # Menunda selama 6 detik setelah mendeteksi QR code

    # Menampilkan output dari kamera
    cv2.imshow("QR_Code_Scanner", frame)

    # Menggunakan 'q' untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Mematikan kamera
cam.release()
cv2.destroyAllWindows()