
import os
import shutil


class RearrangeFile(object):

    def __init__(self):
        self.folder_path = os.getcwd()
        self.list_of_all_files = os.listdir(self.folder_path)

    def check_pdf_folder_existance(self, foldername):
        if os.path.exists(foldername):
            pass
        else:
            os.mkdir(foldername)
        return foldername

    def check_jpeg_folder_existance(self, foldername):
        if os.path.exists(foldername):
            pass
        else:
            os.mkdir(foldername)
        return foldername

    def move_files(self):
        for i in range(len(self.list_of_all_files)):
            if self.list_of_all_files[i].endswith(".pdf"):
                shutil.move(
                    self.folder_path + "/" + self.list_of_all_files[i],
                    self.folder_path + "/pdfs",
                )
            elif self.list_of_all_files[i].endswith(".jpg"):
                shutil.move(
                    self.folder_path + "/" + self.list_of_all_files[i],
                    self.folder_path + "/jpgs",
                )
            else: 
                pass

if __name__ == "__main__":

    re = RearrangeFile()
    pdffoldername = re.check_pdf_folder_existance("pdfs")
    jpegfoldername = re.check_jpeg_folder_existance("jpgs")
    re.move_files()
