from .models import Post
from gcm import *
from lxml import html
import requests
import time
    

    
    
class Push(object):
    def Push(message, posts):
        
        page = requests.get('http://rooster.vanlodenstein.nl/vla/lk_flat1.htm?')
        tree = html.fromstring(page.content)
        roostertable = tree.xpath('//table[@class="inpage"]/tr')
        res =""
        
        rows =[]
        
        for row in roostertable:
            nrow = []
            
            for data in row:
                nrow.append(str(data.text))
                #print(str(data.text))
            rows.append(nrow)
            #print('end row ------')
        
            
        
        
        
        gcm = GCM("AIzaSyAbEgL9oCCxYrwaFySj0E_4k4Luxduj18w")
        for post in posts:
            datamsg = ""
            for row in rows:
                
                if (row.__len__() == 0):
                    continue
                elif (row.__len__()>2 ):
                    if (row[1].lower() == 'uur'):
                        continue
                    
                if(post.klas.lower() not in row[0].lower()):
                    continue
                returnstring = ""
                
                for data in row:
                    returnstring += data + "  "
                
                if(row.__len__()==7):
                    if(row[6].lower()=='x'):
                       datamsg += 'Het lijkt erop dat je vrij hebt:' + returnstring + '\n'
                    else:
                       datamsg +='Roosterwijziging' + returnstring + '\n'
            
            data = {'Bericht' : datamsg}
            reg_id = post.regid
            gcm.plaintext_request(registration_id=reg_id, data=data)
        return 'Done'
        
         
    