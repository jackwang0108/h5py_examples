# h5py_examples
Examples for h5py, including create and read hdf5 files

There are two core concepts in h5py: dataset and group. Correspondingly, there are three major object binds the two concepts: `File`(`h5py._hl.files.File`), `Group`(`h5py._hl.group.Group`), and `Dataset`(`h5py._hl.dataset.Dataset`). Notes, `Dataset` class in h5py is totally different from `torch.utils.data.Dataset`.

In Linux Filesystem Hierarchy Standard (FHS), files should (more preciesly, suggested to) be split and ranged in a given hierarchy. So, in a real Linux system, Ubuntu for an instance, file or directory paths in the Linux file system are like `/etc/apt/source.list`, `/home/jack/`, etc.

However, file paths are only the symbolic representation of the file is the virtual file system. File still need to be saved in the physical driver. So, **the root directory** `/` **is the bridge of constructed file system and physical driver**.

In h5py, `File` object corresponds to root directory, `Group` corresponds to sub-directory, and `Dataset` corresponds to file in the directory. We can creat file and directory in root directory or parent directory.

