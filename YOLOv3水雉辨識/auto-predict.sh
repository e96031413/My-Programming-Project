cp /home/e96031413/PiToTX2/video/*.mp4 /home/e96031413/AlexeyAB/darknet/data/bird/video/
cp -a /home/e96031413/PiToTX2/image/. /home/e96031413/AlexeyAB/darknet/data/bird/image
#./darknet detector test cfg/voc.data cfg/yolov3.cfg yolov3_10000.weights data/bird/image/bird.jpg | tee predict_img_result.txt | sleep 1s ; kill $!
./darknet detector demo cfg/voc.data cfg/yolov3.cfg yolov3_10000.weights data/bird/video/test.mp4 -out_filename detect-result.avi | sleep 120s ; kill $!
youtube-upload --title="video from tx2" detect-result.avi
