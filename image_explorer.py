"""
Explore the position of each pixel -explores with text

"""
import matplotlib.pyplot as plt
import os


examplemap = \
    {1: [134, 757], 2:[193,762],
     3: [134, 715], 4:[186,710],
     5: [107, 629], 6:[254,620],
     7: [230, 496], 8:[92.6, 475],
     9: [40.8,273], 10:[25.3, 218],
     11: [102,223], 12:[155,224],
     13: [219, 240], 14:[28,148],
     15: [161.7, 99.7], 16: [59,87]
     }


IMAGE = "L2_R1_L1_R1.png"  # image chosen as background
IMAGE_FILEPATH = os.path.join(os.getcwd(), "background_images", IMAGE)
background_img = plt.imread(IMAGE_FILEPATH)
fig, ax = plt.subplots(figsize=(16, 8))
ax.imshow(background_img, interpolation='nearest')
plt.show()
# fig, ax = plt.subplots(figsize=(16, 2))
#
# ax.imshow(background_img, interpolation='nearest')
# plt.tight_layout()
# for key, value in examplemap.items():
#  ax.scatter(*value)
#  plt.text(value[0]+10, value[1], str(key))
# plt.show()
