import numpy as np


class SensorArray:
    def __init__(self, channels, offsets=None):
        self.channels = channels
        self.offsets = offsets if offsets is not None else np.zeros(channels)

    def read(self):
        return np.random.randn(self.channels) + self.offsets
