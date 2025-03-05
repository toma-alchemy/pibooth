try:
    import cv2
except ImportError:
    print("cv2 required!")

from pibooth.camera.base import BaseCamera

def get_ipwebcam_proxy(ipaddress=None):
    if ipaddress is not None:
        if not isinstance(ipaddress, str):
            raise TypeError(f"IP address must be a string'{type(ipaddress)}'")
        stream_url = f"http://{ipaddress}:8080/video"
        camera = cv2.VideoCapture(stream_url)
        if camera.isOpened():
            return camera
        print("Couldn't connect to camera")
    return None