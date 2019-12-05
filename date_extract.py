from flask import Flask,request
import base64
import json
from PIL import Image
import pytesseract
import re
from dateutil.parser import parse 

app =Flask(__name__)
def date_extraction(img_open):
    pass
    img=Image.open(img_open)
    dct=dict()
    text=pytesseract.image_to_string(img,lang="eng")
    print(text)
    #print(parse(text).strftime("%Y%m%d"))
    date=re.findall(r'(?:\d{1,2})?[\',-\.\/](?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?(?:\d{2},)?.?(?:\d{2,4})',text)
    if date is not None:
	dct={'date':date}
    else:
	dct={'date':null}
    data=json.dumps(dct)
    return data
        
#this is the link to post image
@app.route('/post_image',methods=['POST'])
def detect_and_return():
        #getting the data in json
        data =  request.get_json()
        #double check for json
        dic  = json.loads(data)
        #extracting base64encoded image string
        img_str = dic["img"]
        #decoding string into binary file
        decoded_string =base64.b64decode(img_str)
        #writing image
        img_open = open('img.jpg','wb')
        img_open.write(decoded_string)
        img_open.close()
        #calling the function
        return date_extraction(img_open)
@app.route('/')
def home()
        return "hello"
        
if __name__=='__main__':
        app.run(port=9991)
