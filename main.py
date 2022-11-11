#importing libraries
import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol

#this funtion activates when a person is authorized
def process_auth():
    from playsound import playsound
    print(f"Authorized - {data}")
    playsound("auth.mp3")

#this funtion activates when a person is unauthorized
def process_unauth():
    from playsound import playsound
    print(f"Unauthorized - {data}")
    playsound("unauth.mp3")

#main funtion
if __name__ == '__main__':

    #setting capture device and window sizes
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    capture.set(3,640)
    capture.set(4,480)

    #opens file and reads the file (file handling)
    with open('allowlist.txt') as f:
        lock = f.read()

    #extracting the data from qrcode
    while (True):
        ret, frame = capture.read()
        for qrcode in decode(frame, symbols=[ZBarSymbol.QRCODE]):
            data = qrcode.data.decode("utf-8")
            #verifing scanned data == data on allowlist
            if data in lock:
                #if authourized do this
                process_auth()
            else:
                #if unauthourized do this
                process_unauth()
        
        #setting window name and window closekwy
        cv2.imshow('AuthSys Scanning', frame)
        if cv2.waitKey(1) == ord('q'):
            break