from __future__ import print_function
import os
import time
import random
import configparser

config = configparser.RawConfigParser()
config.read(r'../local.properties')

PHOTOSBASEDIR = config.get('LocalSection', 'local.photo.files.path')
TIMEDELAY = int(config.get('SlideshowConfiguration', 'slideshow.delay'))

result = []
exclude = "@eaDir"
fileType = ".jpeg"
for root, dirs, files in os.walk(PHOTOSBASEDIR):
    dirs[:] = [d for d in dirs if d not in exclude]
    for name in files:
        if fileType in name:
            result.append(os.path.join(root, name))

while True:
    print("Picking photo to cast")
    nextPicture = random.choice(result)  # Picks a photo at random
    print(nextPicture)

    time.sleep(TIMEDELAY)


