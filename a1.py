from PIL import Image 

import pytesseract as pt 

import os 

      

pt.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tesseract.exe'

# path for the folder for getting the raw images 

path ="C:\\Users\\Mohammad Uzair\\Desktop\\pics\\New"



# path for the folder for getting the output 

tempPath ="C:\\Users\\Mohammad Uzair\\Desktop\\text"



# iterating the images inside the folder 

for imageName in os.listdir(path): 

          

    inputPath = os.path.join(path, imageName) 

    img = Image.open(inputPath) 



    # applying ocr using pytesseract for python 

    text = pt.image_to_string(img, lang ="eng") 



    # for removing the .jpg from the imagePath 

    imagePath = path[0:-4] 



    fullTempPath = os.path.join(tempPath, 'time_'+imageName+".txt") 

    print(text) 



    # saving the  text for every image in a separate .txt file 

    file1 = open(fullTempPath, "w") 

    file1.write(text) 

    file1.close()  

  
