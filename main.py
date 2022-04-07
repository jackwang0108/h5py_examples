from typing import *
from pathlib import Path

import h5py
import numpy as np

base_path: Path = Path(__file__).resolve().parent
hdf5_path: Path = base_path / "dataset.hdf5"


def creat_hdf5():
    with h5py.File(hdf5_path, "w") as f:
        for area in range(1, 6):
            area_group = f.create_group(name=f"Area_{area}")
            total_num = 0
            for room in range(1, 20):
                data = np.ones(shape=(30, 3), dtype=np.float64) * np.arange(30)[:, np.newaxis]
                room_ds = area_group.create_dataset(name=f"room_{room}", data=data, chunks=True)
                room_ds.attrs["note"] = "Point are first centered, so that mean is (0, 0, 0). " \
                                        "And then range is scaled to -1 ~ 1"
                room_ds.attrs["point_num"] = len(data)
                total_num += data
            area_group.attrs["point_num"] = total_num
        print("Done")


def read_hdf5():
    with h5py.File(hdf5_path, "r") as f:
        for area in f.keys():
            for room in f[area].keys():
                ds = f[area][room]
                data = np.asarray(ds)
                print(ds.attrs["point_num"], data.shape, data.dtype)


if __name__ == "__main__":
    creat_hdf5()
    read_hdf5()
