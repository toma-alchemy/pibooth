import pibooth
from pibooth.utils import LOGGER
from pibooth import camera
import cv2

__version__ = "0.0.1"

def get_ipwebcam_camera_proxy(ipaddress=None):
    if ipaddress is not None:
        if not isinstance(ipaddress, str):
            raise TypeError(f"IP address must be a string'{type(ipaddress)}'")
        stream_url = f"http://{ipaddress}:8080/video"
        stream = cv2.VideoCapture(stream_url)
        if stream.isOpened():
            return stream
        print("Couldn't connect to Ip Webcam")
    return None 

class IpWebCamera(camera.CvCamera):
    """Android Ip Camera management
    """
    
    def __init__(self, camera_proxy):
        super().__init__(camera_proxy)
 
      
        
@pibooth.hookimpl
def pibooth_setup_camera(cfg):
    ipweb_cam_proxy = get_ipwebcam_camera_proxy("192.168.20.146")

    if ipweb_cam_proxy:
        LOGGER.info("Configuring Ip Webcam camera ...")
        return(IpWebCamera(ipweb_cam_proxy))
