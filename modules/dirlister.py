import os

def run(**args):
    print "[*] In derlister module."
    files = os.listdir(".")

    return str(files)
