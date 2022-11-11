#importing libraries
import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol

#main funtion
if __name__ == '__main__':

    #setting capture device and window sizes
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    capture.set(3,640)
    capture.set(4,480)

    #extracting the data from qrcode
    while (True):
        ret, frame = capture.read()
        for qrcode in decode(frame, symbols=[ZBarSymbol.QRCODE]):
            data = qrcode.data.decode("utf-8")
            #printing the data
            print(data)
        
        #setting window name and window closekwy
        cv2.imshow('AuthSys Scanning', frame)
        if cv2.waitKey(1) == ord('q'):
            break