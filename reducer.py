from PIL import Image
import math
import os

print("Getting Photos...")
photos = os.listdir()
photos.remove("reducer.py")
os.mkdir("Fotos")
total = len(photos)
cntr = 0
print(f"Total: {total}")
print("Starting Conversion...")

for photo in photos:
    photo.replace(".jpg","")
    cntr += 1
    foo = Image.open(photo)
    x,y = foo.size
    x2 = int(x*0.7)
    y2 = int(y*0.7)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save(f"Fotos/{photo}.jpg",optimize=True,quality=45)
    print(f"{int(cntr/total*100)}%\r",end="",flush=True)
print("Done!")
