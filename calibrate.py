import argparse
import numpy as np
from src.array import SensorArray
from src.calibrate import estimate_offsets, estimate_gain


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames', type=int, default=200)
    args = parser.parse_args()
    arr = SensorArray(16)
    readings = np.stack([arr.read() for _ in range(args.frames)])
    print(estimate_offsets(readings).round(3))
    print(estimate_gain(readings, readings.mean(axis=0)).round(3))


if __name__ == '__main__':
    main()
