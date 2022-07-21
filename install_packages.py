def check_packages():
    import subprocess
    import sys

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    try: 
        import tkinter
    except:
        install('tk')

    try: 
        import PIL
    except:
        install('pillow')  

    


