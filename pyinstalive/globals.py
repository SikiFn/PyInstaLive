from .config import Config
def init():
    global config
    global download
    global comments
    global session
    global config_path
    global args
    config = Config
    download = None
    comments = None
    session = None
    config_path = None
    args = None