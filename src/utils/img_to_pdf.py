from PIL import Image
import os


BASE_DIR = os.path.dirname(__file__)


class ImgToPdf:
    def __init__(self, **kwargs):
        self.image_list = kwargs.get("img_list")
        self.dest_filename = kwargs.get("dest_filename")
        
        if self.dest_filename is None or self.dest_filename == "":
            self.dest_filename = BASE_DIR
        
    def convert_to_pdf(self):
        img_list = []
        for img in self.image_list:
            tmp_img = Image.open(img)
            tmp_img = tmp_img.convert("RGB")
            img_list.append(tmp_img)
        
        img_list[0].save(self.dest_filename, save_all=True, append_images=img_list[1:])
        
        return self.dest_filename
