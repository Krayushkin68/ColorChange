import random

import cv2
import numpy as np

colors = {'blue': range(0, 25),
          'light blue': range(25, 50),
          'green': range(50, 75),
          'yellow': range(75, 100),
          'orange': range(100, 110),
          'red': range(110, 125),
          'pink': range(125, 155),
          'purple': range(155, 170)
          }


def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    return list(int(hex[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


def transform_colors(col):
    col = col.split()
    col = [hex_to_rgb(i) for i in col]
    random.shuffle(col)
    return col


def change_colors(img, means, col):
    change_colors = [cv2.cvtColor(np.uint8([[i]]), cv2.COLOR_BGR2HSV) for i in col]

    # ---------------------------------  Load default image ----------------------------------------------------
    img = cv2.imread(img)
    Z = img.reshape((-1, 3))

    # ---------------------------------  Find K main colors ----------------------------------------------------
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.5)
    K = means
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)

    # ---------------------------------  Transform main colors in HSV and change ---------------------------------
    center = center.reshape(1, center.shape[0], 3)
    hsv = cv2.cvtColor(center, cv2.COLOR_RGB2HSV)

    keys = list(colors.keys())
    random.shuffle(keys)
    ch_dict = {i: j for i, j in zip(keys, change_colors)}

    for num, i in enumerate(hsv[:, :, 0][0]):
        for col_name, val in colors.items():
            if col_name in ch_dict.keys():
                if i in val:
                    new_col = ch_dict[col_name][0, 0, :]
                    add_h = new_col[0] - (max(val) + min(val)) // 2
                    hsv[:, :, 0][0][num] = hsv[:, :, 0][0][num] + add_h

    center = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    center = center.reshape(center.shape[1], 3)

    # ---------------------------------  Back transform with changed main colors ---------------------------------
    Z = center[label.flatten()]
    Z = np.uint8(Z)

    Z = Z.reshape((img.shape))
    cv2.imwrite('Image/res.jpg', Z)
