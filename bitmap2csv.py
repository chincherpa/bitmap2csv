#!/usr/bin/env python

'''
Sub faerben()
Application.ScreenUpdating = False
Set Rng = ActiveSheet.UsedRange

For Each cell In Rng
    LArray = Split(cell.Value2, ",")
    b = LArray(0)
    g = LArray(1)
    r = LArray(2)
    cell.Interior.Color = RGB(r, g, b)
Next

Rng.RowHeight = 0.75 '3
Rng.ColumnWidth = 0.06 '0.24

MsgBox "Fertig"
Application.ScreenUpdating = True
End Sub
'''

from __future__ import with_statement
#from PIL import Image
import cv2
from progressbar import ProgressBar
from widgets import SimpleProgress, Percentage, Bar

image = r'C:\Users\x123069\Desktop\D\pys\bitmap2csv\coast_256.bmp'
csv = image.replace(image.split('.')[-1], 'csv')

#im = Image.open(image)
img = cv2.imread(image, 1)
 
#load the pixel info
#pix = im.load()
 
#get a tuple of the x and y dimensions of the image
#width, height = im.size
height, width, _ = img.shape
#height, width = 2000, 3000

pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=height*width).start()

#open a file to write the pixel data
c = 0
with open(csv, 'w+') as f:
 
  #read the details of each pixel and write them to the file
  for x in range(height):
    ltemp = []  
    for y in range(width):
      c += 1
      pbar.update(c)
      r = img[x,y][0]
      g = img[x,y][1]
      b = img[x,y][2]
      rgb = '{0},{1},{2}'.format(r,g,b)
      ltemp.append(rgb)
    zeile = ';'.join(ltemp)
    zeile = zeile + '\n'
    f.write(zeile)

pbar.finish()
print('Done')
