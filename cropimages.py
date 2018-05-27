from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os;

dir = r"images\\"
cropdir = r"crop\\"

def cropkuva(kuva):
    filu = os.path.join(dir, file)
        
    im = Image.open(filu)#.convert('L')
    w, h = im.size
    im = im.crop((1, h-300, w-(w-400)+1, h))
    im = im.resize( (200, 150), Image.ANTIALIAS)
    kuvafile = os.path.join(cropdir, kuva); 
    im.save(kuvafile)
    print ( "Saved cropimage: " + kuvafile)
    
for file in os.listdir(dir):
    if file.endswith(".jpg"):
        filu = os.path.join(dir, file)
        cropkuva(file)
        #break;