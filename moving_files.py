# Import libraries
import shutil as sh
import os
import random


def main():
    def clean_name():
    """ Function which assigns clear names to the files in output folder """
    for foldername, subfolder, filename in os.walk("C://Users//Lohith//backup"):
        i = 0
        for file in filename:
            bc_name = "_" + str(i) + ".jpg"
            sh.move(os.path.join(foldername, file),
                    os.path.join(foldername, "training_image" + bc_name))
            i += 1

    for foldername, subfolder, filename in os.walk("C://Users//Lohith"):
        for file in filename:
            # .jpg module
            if file.endswith(".jpg"):
                if file in filename:
                    # allocate a random number to the file if it is repeating
                    bc_name = file + str(random.random()) + ".jpg"
                    sh.move(os.path.join(foldername, file),
                            os.path.join(foldername, bc_name))
                    sh.copy(os.path.join(foldername, bc_name),
                            "C://Users//Lohith//backup")
                else:
                    sh.copy(os.path.join(foldername, file),
                            "C://Users//Lohith//backup")
            # jpeg module
            elif file.endswith(".jpeg"):
                if file in filename:
                    # allocate a random number to the file if it is repeating
                    bc_name = file + str(random.random()) + ".jpg"
                    sh.move(os.path.join(foldername, file),
                            os.path.join(foldername, bc_name))
                    sh.copy(os.path.join(foldername, bc_name),
                            "C://Users//Lohith//backup")
                else:
                    sh.copy(os.path.join(foldername, file),
                            "C://Users//Lohith//backup")

    clean_name()


if __name__ == '__main__':
    main()
