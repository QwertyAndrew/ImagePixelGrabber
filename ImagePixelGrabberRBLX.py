import time
import os

from PIL import Image

# Get the directory of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    try:
        # Get a list of all files in the script directory
        files = os.listdir(script_dir)
        
        # Check if any file has a PNG
        png_files = [file for file in files if file.lower().endswith('.png')]
        if not png_files:
            print("To proceed, please make sure you have a PNG image file in this folder :D")
            time.sleep(5)
            os.system('cls')
            continue  # Continue to the next iteration of the loop until there is a PNG file in the folder
        
        # Get the first PNG file found
        image_filename = png_files[0]
        image_path = os.path.join(script_dir, image_filename)
        
        # Load the image
        original_img = Image.open(image_path)
        
        # Resize the image to 64x64 pixels
        final_image = original_img.resize((64, 64), resample=Image.NEAREST)
        
        # Get pixel values
        pixel_val = list(final_image.getdata())
        
        # Create a new text file "ColorValue.txt" in the script directory
        output_file = os.path.join(script_dir, "ColorValue.txt")
        with open(output_file, "w") as fp:
            fp.write("[")
            for i in range(len(pixel_val) - 1):
                # Unpack pixel values based on whether the image is RGBA or RGB
                if len(pixel_val[i]) == 4:
                    r, g, b, a = pixel_val[i]
                    fp.write(f"[{r}, {g}, {b}, {a}], ")  # RGBA format
                else:
                    r, g, b = pixel_val[i]
                    fp.write(f"[{r}, {g}, {b}], ")  # RGB format
            
            # handle last pixel to avoid extra comma
            if len(pixel_val[-1]) == 4:
                r, g, b, a = pixel_val[-1]
                fp.write(f"[{r}, {g}, {b}, {a}]")
            else:
                r, g, b = pixel_val[-1]
                fp.write(f"[{r}, {g}, {b}]")
            
            fp.write("]")
        
        print("Success! This terminal will close in 5 seconds.")
        # Display the image
        final_image.show()
        time.sleep(5)
        break  # Exit the while loop when successful
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(5)
        break  # Exit the while loop when failed
