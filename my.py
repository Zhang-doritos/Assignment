#from jetson_inference import detectNet
#from jetson_utils import videoSource, videoOutput
import jetson.inference
import jetson.utils

#net = detectNet("ssd-mobilenet-v2", threshold=0.5)
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

image_path = "/home/nvidia/jetson-inference/data/images/object_1.jpg"

img = jetson.utils.loadImage(image_path)

detections = net.Detect(img)

if len(detections) >0:
    detection = detections[0]
    class_id = detections[0].ClassID
    confidence = detections[0].Confidence
    left,top,right,bottom = detections[0].Left, detections[0].Top, detections[0].Right, detections[0].Bottom 
    print(detections[0])

#saveImage("Image_with_detections.jpg", image)



#camera = videoSource("/dev/video0") #'/dev/video0'for V4L2
#display = videoOutput("display://0") #'my_video.mp4'for file

#while display.IsStreaming():
    
    #img = camera.Capture()

   # if img is None: #capture timeout
     #   continue
    
    #detections = net.Detect(img) 
    #print(detections)

    #display.Render(img)
    #display.SetStatus("Object Detection | Network{:.0f}FPS".format(net.GetNetworkFPS()))
