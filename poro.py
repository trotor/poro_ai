#pip install pillow
#
# Porotilanne, Tero Ronkko, tero.ronkko@gmail.com 2015-2018
# Fetches images from Liiikennevirasto roadcam, eventually another tool will be used to detech reindeer from images.
#
#python 3.4 Translation

# HIstory:
# 21.5.2018 Github and cleanup
# 28.6.2016 Condaversion
# 4.7.2018 Error catching
# 24.11.2019 Urllib to requests for proxy


version = "1.2.1"
from dateutil import parser
import urllib2
import shutil,datetime
import requests;
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

station = "C14565";
cameraid = "C1456501";

def haeporoja():
    url = "https://tie.digitraffic.fi/api/v1/data/camera-data/" + station
    response = requests.get(url)
    try:
        data = json.loads(response.text)
    
        timetaken = "";
        bSuccess = False;
        if ('cameraStations' in data):
            for camera in data['cameraStations'][0]['cameraPresets']:
                if (camera['id'] == cameraid):
                    #print (camera)
                    timetaken = camera['measuredTime']
                    bSuccess = True;
        if (not bSuccess):
            print("Couldn't fetch info...")
            return;
        #Timestamp: 2018-05-22T09:49:49+03:00
        datetime_object = dateutil.parser.parse (timetaken)
        

        global s
       

        finalfilename = datetime_object.strftime("poro%Y%m%d%H%M.jpg");
	finalname = "images" + os.path.sep + finalfilename;

        if os.path.isfile(finalname):
            print (datetime.datetime.now().strftime("%d.%m.%Y %H:%M - Image exists: " + finalname));
        else:
            r = requests.get('http://weathercam.digitraffic.fi/C1456501.jpg')
            if r.status_code == 200:
                with open(finalname, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                    f.close; 
            print (datetime_object.strftime("%d.%m.%Y %H:%M - New image: " + finalname));
            img = Image.open(finalname)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("C64_Pro-STYLE.ttf", 10)
            sdatestamp = datetime_object.strftime("Porotilanne %d.%m.%Y %H:%M");
            draw.text((0, 12),sdatestamp,(255,255,255),font=font)
            img.save(finalname)
    except:
        print("Couldn't fetch, trying again later...");
        return;
while True:
    haeporoja();
    time.sleep(300 + random.randint(0,120));


