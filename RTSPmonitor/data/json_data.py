class Device:
    def __init__(self, name, rtsp_url, save_path, active=False):
        self.name = name
        self.rtsp_url = rtsp_url
        self.save_path = save_path
        self.active = active


    def to_dict(self):
        return {
            'name': self.name,
            'rtsp_url': self.rtsp_url,
            'save_path': self.save_path,
            'active': self.active
        }

