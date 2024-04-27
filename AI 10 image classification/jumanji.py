import os
os.chdir('C:/Users/ADMIN/Desktop/gitfolder/AI 10 image classification/images/Harry_Potter')
i=1
for file in os.listdir():
    src= file
    dst="Jumanji"+str(i)+".png"
    os.rename(src,dst)
    i+=1
