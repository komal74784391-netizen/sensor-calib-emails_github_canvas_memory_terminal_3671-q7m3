import numpy as np


def estimate_offsets(readings):
    """Estimate per-channel offsets from static-pose readings."""
    return readings.mean(axis=0)


def estimate_gain(readings, reference):
    """Estimate per-channel gain drift relative to reference."""
    return np.linalg.lstsq(readings, reference, rcond=None)[0]
