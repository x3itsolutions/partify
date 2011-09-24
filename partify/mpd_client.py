from mpd import MPDClient

class mpd_client(object):
    """A simple wrapper to enable the with statement to grab an MPD connection."""
    def __init__(self, host="ubuntu.local", port=6600):
        self.host = host
        self.port = port
        self.c = MPDClient()
        self.c.connect(host=self.host, port=self.port)
    
    def __enter__(self):
        return self.c
    
    def __exit__(self, type, value, traceback):
        self.c.disconnect()
        if type is not None:
            raise Exception("%r,%r,%r" % (type, value, traceback))