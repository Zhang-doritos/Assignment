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


