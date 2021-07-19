import cv2

def captureImage() :
    #initialized cv2 - webcam
    videoObject = cv2.VideoCapture(0)
    result = True
    while(result) :
        #reading the frames while the camera is on
        ret, frame = videoObject.read()

        #To save an image to any storage device
        cv2.imwrite("C:/Users/balaj/Desktop/Coding/Class 101/pic1.jpg", frame)
       
        #Stopping the loop
        result = False

    #Closes the webcam
    videoObject.release()
    #closes all the windows & process happening while the webcam is on
    cv2.destroyAllWindows()

captureImage()

#while(condition){
    #//Statement block
#}