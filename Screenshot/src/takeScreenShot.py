# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-03-18 22:29:55
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-04-28 02:24:33

from datetime import datetime

from PIL import ImageGrab

def takeScreenshot():
    
    fileName = "Screenshot-" + datetime.strftime(datetime.now(), "%Y.%m.%d-%H.%M.%S")
    
    screenshot = ImageGrab.grab()
    screenshot.save(fileName + ".png", "PNG") # screenshot.save(fileName, format="PNG")

def main():
    takeScreenshot()


if __name__ == "__main__":
    main()
