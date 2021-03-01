from PyPDF2.pdf import PdfFileReader, PdfFileWriter
from wand.image import Image
from wand.color import Color
from PIL import Image as im
import os

path = u"./drones"
files= os.listdir(path)
s = []
count = 0
for f in files:
     if not os.path.isdir(f):
        print(f)
        input1 = PdfFileReader(open(path+"/"+f, "rb"))
        output = PdfFileWriter()

        numPages = input1.getNumPages()
        print("document has %s pages." %(numPages))

        for i in range(numPages):
            page = input1.getPage(i)
            print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
            page.trimBox.lowerLeft = (0, 0)
            page.trimBox.upperRight = (125, 225)
            page.cropBox.lowerLeft = (80, 100)
            page.cropBox.upperRight = (200, 260)
            output.addPage(page)

        count += 1
        outputStream = open(path+"_out_pdf/"+str(count)+".pdf", "wb")
        output.write(outputStream)
        outputStream.close()

        with Image(filename=path+"_out_pdf/"+str(count)+".pdf", resolution=(200, 200)) as img:
            img.background_color = Color('white')
            img.format = 'jpeg'
            img.save(filename=path+"_out/"+str(count)+"_whole.jpg")

        im_jpg = im.open(path+"_out/"+str(count)+"_whole.jpg")
        # left param is x axis,width,and right is y axis,height
        im_jpg = im_jpg.crop((220, 1610, 565, 2080))
        im_jpg.save(path+"_out_jpg/"+str(count)+".jpg")
print("OK")
a = input()
