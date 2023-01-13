
"""

Converts all images in current directory into PNG format
and formats name of image to <current_directory_name>_<image_count>.png
EX. Thanksgiving2022_01.png, Thanksgiving2022_02.png, etc..

Counts already converted images so if new images are added to the directory
the filenames remain consistent.

If the higest filename count doesn't match the total image count (A picture was deleted),
all the images will be reformatted to keep count consistent. (Order not guaranteed to be maintained)

Designed as a command line tool, add to appropriate path to use.

"""


from PIL import Image
import os


class Convert_to_PNG():

    def __init__(self):
        self.curr_dir = os.listdir(os.getcwd())
        self.folder_name = os.path.basename(os.getcwd())
        pic_info = self.get_pic_info()
        self.formatted_pic_count = pic_info[0]
        self.max_pic_num = pic_info[1]

    def get_pic_info(self):
        formatted_pic_count = 0
        highest_pic_number = 0
        for image in self.curr_dir:
            if image.startswith(self.folder_name):
                formatted_pic_count += 1
                image_num = image.replace(
                    self.folder_name + '_', '').replace('.png', '')
                highest_pic_number = max(highest_pic_number, int(image_num))

        return [formatted_pic_count, highest_pic_number]

    def convert_to_temp_names(self):
        count = 1
        for image in self.curr_dir:
            if image.startswith(self.folder_name):
                new_pic = f'Temp_{count}.png'
                if (image.endswith(".png") or image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".webp")):
                    pic = Image.open(image)
                    pic.save(new_pic, format="png", lossless=True)
                    os.remove(image)
                    count += 1

    def convert(self):
        if self.formatted_pic_count == len(self.curr_dir):
            print("Nothing to convert")
            return

        print("Starting conversion")

        count = self.formatted_pic_count + 1
        if self.formatted_pic_count != self.max_pic_num:
            self.convert_to_temp_names()
            count = 1

        for image in self.curr_dir:
            if not image.startswith(self.folder_name):
                new_pic = f'{self.folder_name}_{count}.png'
                if (image.endswith(".png") or image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".webp")):
                    pic = Image.open(image)
                    pic.save(new_pic, format="png", lossless=True)
                    os.remove(image)
                    count += 1

        print("Conversion complete")


if __name__ == '__main__':
    Convert_to_PNG().convert()
