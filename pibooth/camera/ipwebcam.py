try:
    import cv2
except ImportError:
    print("cv2 required!")

from pibooth.camera.opencv import CvCamera

def get_ipwebcam_camera_proxy(ipaddress=None):
    if ipaddress is not None:
        if not isinstance(ipaddress, str):
            raise TypeError(f"IP address must be a string'{type(ipaddress)}'")
        stream_url = f"http://{ipaddress}:8080/video"
        camera = cv2.VideoCapture(stream_url)
        if camera.isOpened():
            return camera
        print("Couldn't connect to Ip Webcam")
    return None

class IpWebCamera(CvCamera):
    """Android Ip Camera management
    """
    
    def __init__(self, camera_proxy):
        super().__init__(camera_proxy)