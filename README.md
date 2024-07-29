# ImagePixelGrabber
A small Python software where it helps user to resize a PNG image to 64x64 resolution, along an export of RGB/RGBA array inside a new text file ColorValue.txt. 

This is purposely for a [Roblox game](https://www.roblox.com/games/11442061911/image-png) where you can upload any images in 64x64 resolution without being check by the moderation bot. 

Note that you cannot do anything in this game except see your given image displaying as 64 x 64 resolution, this is for education purposes, therefore any images you send, never be saved at all, nor be shown in public.

# Installation
I am currently developing a website specifically for this, just for usability sake. For now, you can follow the instruction below.

To get the file, you need to either [clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository):

```
https://github.com/QwertyAndrew/ImagePixelGrabber.git
```

Or download as a ZIP:

![](/ImageForREADME/downloadViaZIP.gif)

You need Python, so make sure to [download Python](https://www.python.org/downloads/) first.

You also need to install pip, so type this in the terminal, execute them in order.

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

```
python get-pip.py
```

Lastly, you need to install Pillow, therefore you need to type this inside the terminal.

```python
pip install Pillow
```

Once installed, you are ready.

# Usage
1. Implement a PNG, JPG, or JPEG file inside the folder. Don't worry, it can be in any resolution.

![](/ImageForREADME/ImageInFolder.jpg)

2. Open the Python file.
3. As long as it's a valid file format, the image itself will be resized to 64x64 resolution.

![](/ImageForREADME/Success.jpg)

4. Wait until the console prints "Success", there will be a new text file, contains an array of color value from the resized image. There will also be a compressed image inside the folder for you to preview at.

![](/ImageForREADME/ColorValueTXT.jpg)

5. To implement the color value to the game, create a new [Pastebin](https://pastebin.com), paste the color array inside. Remember to set it public, and upload.

![](/ImageForREADME/Pastebin.jpg)

6. Copy the ID of your Pastebin, you can even use the example ID below.

![](/ImageForREADME/PastebinID.jpg)

7. Simply paste the ID to the texbox in the game.
8. Your image is now in the game.

![](/ImageForREADME/UploadImage.gif)

# Troubleshooting
I will update the game so that it can detect potential errors for the users instead of "Invalid ID". So for now, this section will be empty.

# Potential Issues (that I might fix later)
1. If the script is placed in a directory without "write" permissions, it may fail.
2. The script will keep printing a message and clearing the screen if no image provided, not really user-friendly lol.
3. The script assumes that the image file name won't exceed OS limits for file names.
4. If the image dimensions are smaller than 64x64 after cropping, the resizing system will go crazy.
5. This script is not Unix-based friendly, only Windows for now.

## License

[MIT](https://choosealicense.com/licenses/mit/)