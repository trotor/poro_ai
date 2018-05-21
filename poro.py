#Pillow suositeltu tuon PIL:n tilalle truetype supportin takia
#pip install pillow
#
# Porotilanne, Tero Ronkko, tero.ronkko@gmail.com 2015-2018
# Fetches images from Liiikennevirasto roadcam, eventually another tool will be used to detech reindeer from images.
#
#python 3.4 Translation

# HIstory:
# 21.5.2018 Github ja siistitään - tehdään AI toteutus
# 28.6.2016 Condaversion

# TODO: Englishsss


version = "1.1"

try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve
import shutil,datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import filecmp
import os
import  time
import random
print (" Porotilanne.py v" + version+ " by T.Ronkko, tero.ronkko@gmail.com");
print ("---------------------------------");
print


#http://137.116.198.92/tilannekuva-ws/cameras?imageId=C1456501201511260838
#http://weathercam.digitraffic.fi/C1456501.jpg
def haeporoja():
    global s
    #Haetaan uusin vÃÂ¤liaikaiseen
    tmpporo = 'images\\tmpporo.jpg'
    urlretrieve('http://weathercam.digitraffic.fi/C1456501.jpg', 
                tmpporo)

    #sit uusin porofile:
    uusinporo = 'images\\latestporo.jpg'
    #TÃÂ¤hÃÂ¤n filen testaus

    if not os.path.isfile(uusinporo):
        print ("First run")
        shutil.copy(tmpporo, uusinporo)


    
    if filecmp.cmp(tmpporo, uusinporo):
        print (datetime.datetime.now().strftime("%d.%m.%Y %H:%M - Sama kuva"));
    else:
        finalname = datetime.datetime.now().strftime("images\\poro%Y%m%d%H%M.jpg");
        print (datetime.datetime.now().strftime("%d.%m.%Y %H:%M - Uusi kuva " + finalname));
        #print ("Tallennetaan nimellÃ¤: " + finalname)
        img = Image.open(uusinporo)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("C64_Pro-STYLE.ttf", 10)
        sdatestamp = datetime.datetime.now().strftime("Porotilanne %d.%m.%Y %H:%M");
        draw.text((0, 12),sdatestamp,(255,255,255),font=font)
        img.save(finalname)
        shutil.copy(tmpporo, uusinporo)
        

#shutil.copy(tmpporo, finalname)

while True:
    #print ("Aloitetaan")
    haeporoja();
    time.sleep(300 + random.randint(0,120));


