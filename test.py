from aip import AipFace
from picamera import PiCamera
import urllib.request
import RPi.GPIO as GPIO
import base64
import time
# import bluetooth

from bluetooth_test import bt_open,servo_init,bt_close


#百度人脸识别API账号信息
APP_ID = '19607076'
API_KEY = 'fKbkSXWKRRWHq1TSCn9ONZae'
SECRET_KEY ='gSC6XuHsxBL0Eo2RGU3WKIdto2Mfgcsc'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)#创建一个客户端用以访问百度云
#图像编码方式
IMAGE_TYPE='BASE64'
camera = PiCamera()#定义一个摄像头对象
#用户组
GROUP = '00'
 
#照相函数
def getimage():
    camera.resolution = (1024,768) # set size
    camera.start_preview() # open camera
    time.sleep(2) # wait for 2 seconds 
    camera.capture('faceimage.jpg')#takes picture and store it 
    time.sleep(2)
# convert image format
def transimage():
    f = open('faceimage.jpg','rb')
    img = base64.b64encode(f.read())
    return img
# upload and compare to database
def go_api(image):
    result = client.search(str(image, 'utf-8'), IMAGE_TYPE, GROUP); # search from database
    if result['error_msg'] == 'SUCCESS': # if succeed
        name = result['result']['user_list'][0]['user_id'] # get name
        score = result['result']['user_list'][0]['score'] #get a score of similarity
        if score > 80: # if similarity > 80
            if name == 'the_rock':
                print("Welcomes%s !" % name)
                time.sleep(1)
            if name == 'Tom_Crews':
                print("Welcomes%s !" % name)
                time.sleep(3)
            if name == "yangmi":
                print("Welcomes%s !" % name)
                time.sleep(3)
            if name == "yushu":
                print("Welcomes%s !" % name)
                
        else:
            print("Sorry, I don't recognize you！")
            name = 'Unknow'
            return 0
        curren_time = time.asctime(time.localtime(time.time())) # get the current time
 
        # save the record to Log.txt file
        f = open('Log.txt','a')
        f.write("Person: " + name + "     " + "Time:" + str(curren_time)+'\n')
        f.close()
        return 1
    if result['error_msg'] == 'pic not has face':
        print('Not recognize a human face')
        time.sleep(3)
        return -1
    else:
        print(result['error_code']+' ' + result['error_code'])
        return 0
# main
if __name__ == '__main__':
    
    # while True:
        
        print('准备开始，请面向摄像头 ^_^')

        if True:
            getimage() # take photo
            img = transimage()  #转换照片格式
            res = go_api(img)   #将转换了格式的图片上传到百度云
            if(res == 1):   #是人脸库中的人
                print("Welcome home, the door is open")
            elif(res == -1):
                print("I don't see you, door is closing")
                time.sleep(1)  
            else:
                print("Closing door")
            time.sleep(3)
            print('Done.')
            time.sleep(5)