import os
from PIL import Image, ImageOps
from src.settings import config


def get_image_paths(directory):
    """
    Returns a list of file paths for all images in the given directory.

    Parameters:
    directory (str): Path to the directory to scan for images.

    Returns:
    list: A list of paths to the images in the directory.
    """
    image_extensions = ['.png', '.jpg', '.jpeg', '.webp']
    return [os.path.join(directory, file) for file in os.listdir(directory)
            if os.path.splitext(file)[1].lower() in image_extensions]

def xray_effect(image_path, output_dir):
    """
    Applies an X-ray effect to the provided image and saves it to the output directory.

    Parameters:
    image_path (str): The path to the input image.
    output_dir (str): The directory where the X-ray effect image will be saved.
    """
    try:
        with Image.open(image_path) as img:
            inverted_image = ImageOps.invert(img)
            grayscale_image = inverted_image.convert("L")
            contrasted_image = ImageOps.autocontrast(grayscale_image)

            output_path = os.path.join(output_dir, get_output_filename(image_path))
            contrasted_image.save(output_path)
            return f"X-ray effect image saved as {output_path}"
    except Exception as e:
        return f"An error occurred: {e}"

def get_output_filename(input_path):
    """
    Generates the output filename for the X-ray effect image based on the input image path.

    Parameters:
    input_path (str): The path to the input image.

    Returns:
    str: The output filename for the X-ray effect image.
    """
    base_name = os.path.basename(input_path)
    name, ext = os.path.splitext(base_name)
    return f"{name}_x-ray{ext}"

def main(input_dir, output_dir):
    """
    Main function to apply X-ray effect to all images in the input directory and save them to the output directory.

    Parameters:
    input_dir (str): Path to the directory containing input images.
    output_dir (str): Path to the directory where the X-ray effect images will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_paths = get_image_paths(input_dir)
    for path in image_paths:
        print(xray_effect(path, output_dir))


if __name__ == '__main__':
    main(config.APP_PATH_INPUT_IMAGES, config.APP_PATH_OUTPUT_IMAGES)
