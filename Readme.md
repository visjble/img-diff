Image Difference Tool
This tool allows you to compare two images and visualize their differences by highlighting them in red. It uses the Python Imaging Library (PIL) to process and compare images.

Prerequisites
Python 3.x
PIL (Pillow)
You can install Pillow using pip:

bash
Copy code
pip install Pillow
Usage
Run the script:
bash
Copy code
python image_diff.py
You will be prompted to enter the paths for:

The first image
The second image
The output image (where the difference will be saved)
If the two images have different sizes, the script will notify you and exit. Otherwise, it will generate an image highlighting the differences in red and save it to the specified output path.

Functionality
The main function, diff_images(img1_path, img2_path, output_path), takes in the paths of two images and an output path. It then:

Opens the two images.
Checks if they are of the same size.
Computes the difference between the two images.
Highlights any differences in red.
Saves the resulting difference image to the specified output path.
Example
If you have two images, image1.png and image2.png, and you want to save the difference as diff.png, you would provide these paths when prompted by the script. The resulting diff.png will show the differences between the two images highlighted in red.

This README provides a brief overview of the tool, its prerequisites, and how to use it. You can expand upon it or customize it further based on additional features or changes you make to the code.
