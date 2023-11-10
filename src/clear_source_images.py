import os
import shutil


os.chdir("./src")

if os.path.exists("source_images"):
    shutil.rmtree("./source_images", ignore_errors=True)
    os.mkdir("source_images")
    print("Successful!")

else:
    print("Something was wrong!")
