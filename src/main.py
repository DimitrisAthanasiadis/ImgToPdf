from utils.img_to_pdf import ImgToPdf
import sys
import os


if __name__ == "__main__":
    a = sys.argv # first arg is program name. all the others are the actual args.

    images_folder_name = sys.argv[1]
    dest_filename = sys.argv[2]
    images = sys.argv[3:]
    
    images_copy = []
    for im in images:
        images_copy.append(os.path.join(images_folder_name, im))

    converter = ImgToPdf(img_list=images_copy, dest_filename=dest_filename)
    dest_path = converter.convert_to_pdf()
    print(dest_path)
