import time
import os

from PIL import Image

# get the directory of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    try:
        # get a list of all files in the script directory
        files = os.listdir(script_dir)
        
        # check if any file has a PNG extension
        png_files = [file for file in files if file.lower().endswith('.png')]
        if not png_files:
            print("Sorry, but no PNG image file is found. Please try again.")
            time.sleep(5)
            continue  # continue to the next iteration of the loop until there is a png file in the folder
        
        # get the first PNG file found
        image_filename = png_files[0]
        image_path = os.path.join(script_dir, image_filename)
        
        # load the image
        original_img = Image.open(image_path)
        
        # resize the image to 64x64 pixels
        final_image = original_img.resize((64, 64), resample=Image.NEAREST)
        
        # get pixel values
        pixel_val = list(final_image.getdata())
        
        # create a new text file "ColorValue.txt" in the script directory
        output_file = os.path.join(script_dir, "ColorValue.txt")
        with open(output_file, "w") as fp:
            fp.write("[")
            for i in range(len(pixel_val) - 1):
                r, g, b, a = pixel_val[i]
                fp.write(f"[{r}, {g}, {b}, {a}], ")
            
            r, g, b, a = pixel_val[-1]
            fp.write(f"[{r}, {g}, {b}, {a}]")
            fp.write("]")
        
        print("Success")
        # display the image
        final_image.show()
        time.sleep(5)
        break  # exit the while loop when successful
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(5)
        break  # exit the while loop when failed
