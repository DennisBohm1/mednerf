import numpy as np
import SimpleITK as sitk
import pydicom
import pydicom._storage_sopclass_uids
from pydicom import Dataset
import datetime
import os
import tempfile

from pydicom.dataset import FileMetaDataset, FileDataset
from pydicom.uid import UID


def convert2d(image2d, idx):
    # Create some temporary filenames
    suffix = '.dcm'
    filename_little_endian = f"/Users/datacation/Library/CloudStorage/OneDrive-Datacation/Pancreas Data/NIH/Enhanced/{idx:04}.dcm"
    filename_big_endian = tempfile.NamedTemporaryFile(suffix=suffix).name

    print("Setting file meta information...")
    # Populate required values for file meta information
    file_meta = FileMetaDataset()
    file_meta.MediaStorageSOPClassUID = UID('1.2.840.10008.5.1.4.1.1.2')
    file_meta.MediaStorageSOPInstanceUID = UID("1.2.3")
    file_meta.ImplementationClassUID = UID("1.2.3.4")

    print("Setting dataset values...")
    # Create the FileDataset instance (initially no data elements, but file_meta
    # supplied)
    ds = FileDataset(filename_little_endian, {},
                     file_meta=file_meta, preamble=b"\0" * 128)

    # Add the data elements -- not trying to set all required here. Check DICOM
    # standard
    ds.PatientName = "Test^Firstname"
    ds.PatientID = "123456"

    # Set the transfer syntax
    ds.is_little_endian = True
    ds.is_implicit_VR = True

    # Set creation date/time
    dt = datetime.datetime.now()
    ds.ContentDate = dt.strftime('%Y%m%d')
    timeStr = dt.strftime('%H%M%S.%f')  # long format with micro seconds
    ds.ContentTime = timeStr

    print("Writing test file", filename_little_endian)
    ds.save_as(filename_little_endian)
    print("File saved.")

    # # Write as a different transfer syntax XXX shouldn't need this but pydicom
    # # 0.9.5 bug not recognizing transfer syntax
    # ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRBigEndian
    # ds.is_little_endian = False
    # ds.is_implicit_VR = False
    #
    # print("Writing test file as Big Endian Explicit VR", filename_big_endian)
    # ds.save_as(filename_big_endian)

ct = np.load('/Users/datacation/Library/CloudStorage/OneDrive-Datacation/Pancreas Data/NIH/Images npy/0001.npy')
mask = np.load('/Users/datacation/Library/CloudStorage/OneDrive-Datacation/Pancreas Data/NIH/Mask npy/0001.npy')

mask = (mask == 1)
image = np.copy(ct)
print('Changing')
image[mask] = 2000

image = np.moveaxis(image, -1, 0)
# print(new_array.dtype)
# print(new_array.shape)

for i, x in enumerate(image):
    convert2d(x, i)

