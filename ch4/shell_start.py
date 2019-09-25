#
#Example file for working with file system shell methods
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # Make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # Get the path to the file in the current directory
        src = path.realpath("textfile.txt")
        #let make a backup copy by appending "bak" to the name
        dst = src + ".bak"
        
        #copy over the file with permissons, modification time and other info
        #shutil.copy(src,dst)
        #shutil.copystat(src,dst)
        
        #rename the original file
        #os.rename("textfile.txt", "newfile.txt")

        #Now put things into a zip archive
        #root_dir, tail = path.split(src)
        #shutil.make_archive("archive", "zip", root_dir)

        # More fine-grained control over Zip files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

















if __name__ =='__main__':
    main()