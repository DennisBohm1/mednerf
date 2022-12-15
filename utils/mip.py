import random

import matplotlib.image
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc
import tensorflow as tf
# import tf.experimental.numpy as tnp
from PIL import Image


def generate_angles(array, filename, index):
    angle = random.uniform(-180, 180)
    rotated = np.max(scipy.ndimage.rotate(array, angle, mode='nearest', axes=(0, 1), reshape=False), axis=0)
    matplotlib.image.imsave(
        f"/Users/datacation/Library/Mobile Documents/com~apple~CloudDocs/CSE/Jaar 5/SCG/mednerf/"
        f"graf-main/data/Pancreas MIP/{filename + 1:04}-{index}.png",
        rotated,
        cmap='Greys_r'
    )


def resize_image(filename, index):
    im = Image.open(
        f"/Users/datacation/Library/Mobile Documents/com~apple~CloudDocs/CSE/Jaar 5/SCG/mednerf/"
        f"graf-main/data/Pancreas MIP/{filename + 1:04}-{index}.png"
    )

    max = 466
    thisx = im.size[0]

    padding = int((max - thisx) / 2)
    im.crop((-padding, 0, max - padding, 512))
    new_image = Image.new("RGBA", (max, 512), "BLACK")
    new_image.paste(im, (padding, 0), im)
    new_image.convert('RGB').save(
        f"/Users/datacation/Library/Mobile Documents/com~apple~CloudDocs/CSE/Jaar 5/SCG/mednerf/"
        f"graf-main/data/Pancreas MIP/{filename + 1:04}-{index}.png",
        "PNG"
    )

im = np.load(
    f"/Users/datacation/Library/CloudStorage/OneDrive-Datacation/Pancreas Data/NIH/Images npy/0001.npy"
)
mask = np.load(
    f"/Users/datacation/Library/CloudStorage/OneDrive-Datacation/Pancreas Data/NIH/Mask npy/0001.npy"
)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(im[:, :, 120], cmap="Greys_r")
ax2.imshow(mask[:, :, 120], cmap="Greys_r")
plt.show()
