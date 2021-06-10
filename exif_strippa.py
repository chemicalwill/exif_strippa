#!/usr/bin/env python
"""
exif_strippa.py - strips EXIF data from all .jpg images in a given directory
and saves the scrubbed pictures in a subdirectory "tagless"
"""

from glob import glob
import os
from pathlib import Path

from exif import Image
import pyinputplus as pyip


def main():
    folder = pyip.inputFilepath(prompt="Enter the photo directory: ", mustExist=True)
    os.chdir(folder)

    try:
        os.mkdir("tagless")
    except FileExistsError:
        pass

    else:
        for photo in glob(f"{folder}/*.jpg"):
            p = Path(photo)
            with open(photo, "rb") as image_file:
                image_obj = Image(image_file)
                image_obj.delete_all()
            with open(f"tagless/scrubbed_{p.stem}.jpg", "wb") as new_image_file:
                new_image_file.write(image_obj.get_file())


if __name__ == "__main__":
    main()
