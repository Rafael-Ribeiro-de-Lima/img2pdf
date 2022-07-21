from PIL import Image
import os
from os import listdir
from os.path import isfile, join

print("Coloque o caminho para a pasta com as imagens: ")
path = input(r'')
name = os.path.basename(path)

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))] 
image_list = []


for file in onlyfiles:
    try: 
        image = Image.open(path+"\\"+file)
        im = image.convert('RGB')
        image_list.append(im)
    except:
        pass

im_0 = image_list[0]
image_list = image_list[1:]     
file = '\\Apresentação - '+name+'.pdf'
im_0.save(path+file, save_all=True, append_images=image_list)

print('Apresentação criada em ' + path)
input('Digite enter para sair.')

