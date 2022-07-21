# Ma'am can you check the code by running it coz I am getting that Cv2 error that i was getting in last class also So..
import os
import cv2
path = "Images/"

images = []
for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in ['.png']:
        file_name=path+file
        images.append(file_name)
count = len(images)
frame = cv2.imread(images[0])
height,width,channels = frame.shape
size =(width,height)

out = cv2.VideoWriter("ProjectVideo.avi",cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0,count):
    print(images[i])
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("Done..")

 