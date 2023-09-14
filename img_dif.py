from PIL import Image, ImageChops, ImageDraw

def diff_images(img1_path, img2_path, output_path):
    # Open the two images
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # Ensure the images are the same size
    if img1.size != img2.size:
        print("The images have different sizes.")
        return

    # Compute the difference
    diff = ImageChops.difference(img1, img2)

    # Highlight differences in red
    diff = diff.convert("RGB")
    d = ImageDraw.Draw(diff)
    width, height = diff.size
    for x in range(width):
        for y in range(height):
            r, g, b = diff.getpixel((x, y))
            if r > 0 or g > 0 or b > 0:
                d.point((x, y), fill=(255, 0, 0))

    # Save the difference image
    diff.save(output_path)
    print(f"Difference image saved as {output_path}")

if __name__ == "__main__":
    img1_path = input("Enter the path to the first image: ")
    img2_path = input("Enter the path to the second image: ")
    output_path = input("Enter the path to save the difference image: ")

    diff_images(img1_path, img2_path, output_path)
