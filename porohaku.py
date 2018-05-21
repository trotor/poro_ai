
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageMath
import numpy
import os

polku = 'images\\'
taakuva = ''
edellinenkuva =''
for fn in os.listdir(polku):
    #print ("filu: " + fn);
    if os.path.isfile(polku+fn):
        if (len(taakuva)<2):
            edellinenkuva = polku+fn                    
            taakuva = polku+fn
        edellinenkuva = taakuva
        taakuva = polku+fn
        imtaa = Image.open(taakuva)
        imtaa = imtaa.convert('L');
        #Tää pitää kokeilla varmoilla kuvilla ja lisätä neuroverkko
        
        imedellinen = Image.open(edellinenkuva)
        imedellinen = imedellinen.convert('L')
        comp = ImageMath.eval("convert(a - b, 'L')", a=imtaa, b=imedellinen)
        dcomp = list(comp.getdata());
        karvo = numpy.mean(dcomp)
        lista = numpy.where (dcomp > (karvo*20))
        
        print (fn + " " + str(len(lista[0])));

print (edellinenkuva)
print (taakuva)
#print comp.histogram();
print ("Done")

#comp.show()
        
