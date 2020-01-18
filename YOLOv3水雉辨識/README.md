# 使用YOLOv3演算法進行水雉辨識

#### 2020年1月18更新: 透過OpenCV執行YOLOv3的方法(基於Python)

[了解詳情](https://github.com/e96031413/OpenCV-YOLOv3-Python-Jacana)

### 完整設定好的darknet

分別為Ubuntu上的pjreddie版本和AlexeyAB版本

* [pjreddie版本](https://drive.google.com/file/d/1D5zT_yOcNYCr4W1wkQGZvg9Lj-2TOJ8R/view?usp=sharing
) - 官方版，含權重、cfg......等檔案870MB。

* [AlexeyAB版本](https://drive.google.com/file/d/1xzXZ1GAUu_j4mTMMV2kcnqKYT_eKIVkl/view?usp=sharing
) - 【推薦】優化版，具有辨識結果影片保存功能、偵測性能比原版好、Boundbox旁包含辨識率數字。含權重、cfg......等檔案463MB。

### 水雉圖片下載

本壓縮檔包含原始圖片1200張、標記好的圖片、標記好的label txt文件......等

* [標記好的圖片](https://drive.google.com/file/d/1Sbxn-v2FOKqiO-PWO0iS12xZ2RxKHK2s/view?usp=sharing
) - 檔案257MB。

### 模型Weights下載

目前有YOLOv3、YOLOv3-tiny兩個版本，持續訓練中~~~

* [yolov3_10000.weights](https://drive.google.com/file/d/1ebXi5TXQh1OUu2_spayXL3VA25hQZTxq/view?usp=sharing) - 水雉的YOLOv3版模型，準確度比Tiny版高，能辨識影片，缺點是FPS性能較低。
* [yolov3-tiny_90000.weights](https://drive.google.com/file/d/1BYgMXw-7eLTFX2851KhbDumWIns3JLkb/view?usp=sharing) - 水雉的YOLOv3 Tiny版模型，較不耗硬體資源，缺點是準確度較低。
* [yolov2-tiny_300000.weights](https://drive.google.com/file/d/1v85WdFMNIEORdk9texFtuFfFmr5q5uqc/view?usp=sharing) - 水雉的YOLOv2 Tiny版模型。


### 訓練模型使用的cfg檔案

* [yolov3.cfg](https://gist.github.com/e96031413/659746b2d213a9574b5898f2393a8b6c) - YOLOv3的cfg檔案（針對單class)

* [yolov3-tiny.cfg](https://gist.github.com/e96031413/bd77222a608999db2e58922f1be35d76) - YOLOv3 Tiny的cfg檔案（針對單class)

* [yolov2-tiny.cfg](https://gist.github.com/e96031413/d703c1a6c35fe3923122ce543a29642f) - YOLOv2 Tiny的cfg檔案（針對單class)

### 自動辨識與成果影片上傳Script

* [auto-predict.sh](https://gist.github.com/e96031413/4d03e70e6f7f4a1c452d1a59ac1a1363) - 將外網FTP所上傳的影片複製到darknet資料夾、針對影片進行辨識、將結果自動上傳到Youtube


### 相關教學文章

* [NVIDIA Jetson TX2學習筆記（三）:執行YOLOv3](https://medium.com/@yanweiliu/nvidia-jetson-tx2%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%B8%89-%E5%AE%89%E8%A3%9Dopencv-c62e2435ad57) - 20191025更新：使用AlexeyAB版本的darknet效果比原版好。在TX2訓練YOLOv3和執行YOLOv3

* [Python影像辨識筆記(九)：分別在Windows和Ubuntu 18.04上安裝並執行YOLOv3（使用GPU）](https://medium.com/@yanweiliu/python%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E7%AD%86%E8%A8%98-%E5%85%AB-%E5%88%86%E5%88%A5%E5%9C%A8windows%E5%92%8Cubuntu-18-04%E4%B8%8A%E5%AE%89%E8%A3%9D%E4%B8%A6%E5%9F%B7%E8%A1%8Cyolov3-%E4%BD%BF%E7%94%A8gpu-d2b77347fde) - 除了在TX2上執行外，我們也能在Windows和Ubuntu系統上執行並訓練YOLOv3喔~

* [Python影像辨識筆記(九之四)：可視化YOLOv3訓練過程中的loss、IOU、avg Recall等的曲線圖](https://medium.com/@yanweiliu/python%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E7%AD%86%E8%A8%98-%E4%B9%9D%E4%B9%8B%E5%9B%9B-%E5%8F%AF%E8%A6%96%E5%8C%96yolov3%E8%A8%93%E7%B7%B4%E9%81%8E%E7%A8%8B%E4%B8%AD%E7%9A%84loss-iou-avg-recall%E7%AD%89%E7%9A%84%E6%9B%B2%E7%B7%9A%E5%9C%96-ef3d36daa5ec) - 透過訓練log的視覺化繪圖，我們來看看什麼時候模型就沒有再繼續優化了！！！

* [Raspberry Pi學習筆記（二十七）：在Pi上執行YOLOv3](https://medium.com/@yanweiliu/raspberry-pi%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%BA%8C%E5%8D%81%E4%B8%83-%E5%9C%A8pi%E4%B8%8A%E5%9F%B7%E8%A1%8Cyolov3-9cf124d5d582) - 為了讓Pi也能辨識水雉，我們來看看如何將YOLOv3模型部署到Pi上吧

* [Raspberry Pi學習筆記（二十八）：在Pi 3B+上安裝OpenVINO環境（搭配第一代Intel® Movidius™ NCS運算棒）](https://medium.com/@yanweiliu/raspberry-pi%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%BA%8C%E5%8D%81%E5%85%AB-%E5%9C%A8pi-3b-%E4%B8%8A%E5%AE%89%E8%A3%9Dopenvino%E7%92%B0%E5%A2%83-%E6%90%AD%E9%85%8D%E7%AC%AC%E4%B8%80%E4%BB%A3intel-movidius-ncs%E9%81%8B%E7%AE%97%E6%A3%92-744ce6709eeb) - 在Pi上跑YOLO好慢喔，能不能加速啊？還沒辨識成功，水雉都飛走了呢！沒問題，我們用Intel的NCS運算棒加速吧~
