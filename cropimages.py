#
# Crop poro 
# Simple batch cropper, Tero Ronkko 2018
#
# Create dataset directory with equal directorynames and then call iteratedir(dir)
#

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os;

dir = r"images\\"
cropdir = r"dataset\\"

def cropkuva(kuva):
    #filu = os.path.join(dir, file)       
    im = Image.open(kuva)#.convert('L')
    w, h = im.size
    im = im.crop((1, h-300, w-(w-400)+1, h))
    im = im.resize( (200, 150), Image.ANTIALIAS)
    kuvafile = os.path.join(cropdir, kuva); 
    im.save(kuvafile)
    print ( "Saved cropimage: " + kuvafile)
    
def iteratedir ( polku):    
    #print ("Handling: " + polku);
    for file in os.listdir(polku):
        filu = os.path.join(polku, file)            
        #print (" Filu: " + filu)
        if filu.endswith(".jpg"):
            cropkuva(filu)
            #break;
        if (os.path.isdir(filu)):                  
            iteratedir( filu + "\\");

for file in os.listdir(dir):
    iteratedir(r"images\\");
    iteratedir(r"training_set\\");
    iteratedir(r"test_set\\");
    
            