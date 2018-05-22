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

station = "C14565";
cameraid = "C1456501";
version = "1.1"
from dateutil import parser
try:
    from urllib.request import urlretrieve
    from urllib.request import urlopen;
except ImportError:
    from urllib import urlretrieve
    from urllib import urlopen;
import shutil,datetime
import urllib;
import json;
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import dateutil
import filecmp
import os
import  time
import random
print (" Porotilanne.py v" + version+ " by T.Ronkko, tero.ronkko@gmail.com");
print ("---------------------------------");
print

#Kelikamerat
#http://tie.digitraffic.fi/api/v1/data/camera-data

#Camera ID C1456501

#https://tie.digitraffic.fi/api/v1/data/camera-data/C14565

#http://137.116.198.92/tilannekuva-ws/cameras?imageId=C1456501201511260838
#http://weathercam.digitraffic.fi/C1456501.jpg

def haeporoja():
    url = "https://tie.digitraffic.fi/api/v1/data/camera-data/" + station
    response = urlopen(url)
    data = json.loads(response.read())
    timetaken = "";
    #print (data['cameraStations'][0]['cameraPresets'])
    bSuccess = False;
    for camera in data['cameraStations'][0]['cameraPresets']:
        if (camera['id'] == cameraid):
            #print (camera)
            timetaken = camera['measuredTime']
            bSuccess = True;
    if (not bSuccess):
        print("Couldn't fetch info...")
        return;
    #Timestamp: 2018-05-22T09:49:49+03:00
    datetime_object = dateutil.parser.parse (timetaken)#datetime.datetime.strptime(timetaken, "%Y-%m-%dT%H:%M:%S")
    #print (datetime_object.strftime("%d.%m.%Y %H:%M is most recent image (from response)"))
    

    #return;
    global s
    #Haetaan uusin vÃÂ¤liaikaiseen
    #  tmpporo = 'images\\tmpporo.jpg'
    # TODO: Make this dynamic too from json above...
    #   urlretrieve('http://weathercam.digitraffic.fi/C1456501.jpg', 
    #               tmpporo)

    #sit uusin porofile:
    #TÃÂ¤hÃÂ¤n filen testaus

    #    if not os.path.isfile(uusinporo):
    #        print ("First run")
    #        shutil.copy(tmpporo, uusinporo)

    finalname = datetime_object.strftime("images\\poro%Y%m%d%H%M.jpg");

    #TODO Make this compare if one with current name exists...
    if os.path.isfile(finalname):
        print (datetime.datetime.now().strftime("%d.%m.%Y %H:%M - Image exists: " + finalname));
    else:
        uusinporo = 'images\\latestporo.jpg'
        urlretrieve('http://weathercam.digitraffic.fi/C1456501.jpg', 
                uusinporo)
    
        print (datetime_object.strftime("%d.%m.%Y %H:%M - New image: " + finalname));
        #print ("Tallennetaan nimellÃ¤: " + finalname)
        img = Image.open(uusinporo)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("C64_Pro-STYLE.ttf", 10)
        sdatestamp = datetime_object.strftime("Porotilanne %d.%m.%Y %H:%M");
        draw.text((0, 12),sdatestamp,(255,255,255),font=font)
        img.save(finalname)
        #shutil.copy(tmpporo, uusinporo)
        

#shutil.copy(tmpporo, finalname)

while True:
    #print ("Aloitetaan")
    haeporoja();
    time.sleep(300 + random.randint(0,120));


