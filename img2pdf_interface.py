import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import webbrowser

def callback(url):
    webbrowser.open_new(url)
    
root = tk.Tk()

root.iconbitmap(r'C:\Users\imobles\Desktop\scripts\img2pdf\favicon.ico')



canvas1 = tk.Canvas(root, width=550, height=550, bg='gray95', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Conversor de Imagens para PDF')
label1.config(font=('helvetica', 20))
canvas1.create_window(250,40, window=label1)

footer = tk.Label(root, text='© Feito por Rafael Ribeiro de Lima', font=12, cursor='hand2')
footer.pack(side='bottom')
footer.bind("<Button-1>", lambda e: callback("https://www.linkedin.com/in/rafael-ribeiro-de-lima/"))



def getJPG():
    global image_list

    image_list = []

    import_file_path = list(filedialog.askopenfilenames())
    for file in import_file_path:
        try: 
            image = Image.open(file)
            im = image.convert('RGB')
            image_list.append(im)
        except:
            pass

    


browseButton_JPG = tk.Button(root, text="      Selecione as imagens desejadas     ", command=getJPG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 200, window=browseButton_JPG)


def convertToPNG():
    global image_list

    im_0 = image_list[0]
    image_list = image_list[1:]     
    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    im_0.save(export_file_path, save_all=True, append_images=image_list)
    image_list = []


saveAsButton_PNG = tk.Button(text="            Converter para PDF            ", command=convertToPNG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 280, window=saveAsButton_PNG)

root.mainloop()