import cv2 
import dropbox
import time
import random

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject =cv2.VideoCapture(0)
    result=True 
    while(result):
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        result=False
    return imageName
    print("you have been caught")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token="sl.AxiH4Qk6YVFJLcqwzaOOTNsbcBbNW2bCdCgWXvPS0GBE3xtG4Hosmoh2LTg-gQJktDcV-6iu8aMNlN6I8--pXk2DRIjHEltAU9xnUYcD_YXji_n81qqKjmir7ymYUNJF5JTBDXo"
    file=img_counter
    file_from=file
    file_to="/newfolder1/"+(imageName)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)
main()