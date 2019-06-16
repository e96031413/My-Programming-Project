# 使用IBMCloud-Annotations訓練影像辨識模型(結合iOS和Android的影像辨識APP)

Medium文章連結：https://pse.is/J58TS

![img](https://cdn-images-1.medium.com/max/1440/1*aH2KnNWk_ropqZkehXui1g.png)

IBM Cloud-Annotations





![img](https://cdn-images-1.medium.com/max/1440/1*x8SyN5E3Y-9WJmCLHwMb-g.png)

APP





![img](https://cdn-images-1.medium.com/max/1440/1*V3fdxW-ylt7oivvXN_fAiQ.png)

IBM的訓練平台



### 官方教學

[**Introduction**
*Create custom models from Cloud Annotations for mobile, IoT and web.*cloud-annotations.github.io](https://cloud-annotations.github.io/training/classification/cli/index.html)

### 注意事項

**零、如何準備圖片？**

```
選項1：到 ImageNet下載
選項2：用Google搜尋圖片進行批量下載
-----(1)使用瀏覽器套件 圖片助手(ImageAssistant) 批量圖片下載器
-----(2)於Google圖片上搜尋關鍵字
-----(3)批量下載回圖片
選項3：自己拍照
下載回來後請先自行將圖片尺寸改為224px*224px
```

**一、圖片分為三部份**

```
以水雉為例
(！！！！重要，沒有三個標籤會失敗！！！！)
需要建立
1水雉
2不是水雉
3其他鳥類
總共三種標籤
(！！！！重要，沒有三個標籤會失敗！！！！)
例如:
1.水雉的就標記為水雉
2.其他鳥類只要放上鳥的圖片即可
3.其他物件的就標記附近的背景或其他圖片
(！！！！重要！！！！)
水雉和其他鳥類的圖片數量保持一樣多
20190616-20:53測試
35張水雉配上35張其它鳥類
41張其它圖片
(！！！！重要！！！！)
```

**二、首次訓練時直接**`**cacli train**`**就好**

```
如果想要重新訓練別種圖片怎麼辦？
在官方教學第五個步驟，Training a model中，必須要cacli init完，再進行cacli train 的動作，才能重新訓練
```

**三、**`**cacli train**`**需要花一些時間，請耐心等候**

**四、**`**cacli download <model_id>**`**，請記好自己的model_id才能將訓練完的模型下載回電腦**

**五、建立**[**iOS**](https://github.com/cloud-annotations/classification-ios/)**或**[**Android APP**](https://github.com/cloud-annotations/classification-android/)

------

[**How to Label Data — Create ML for Object Detection**
*The new Create ML app just announced at WWDC 2019, is an incredibly easy way to train your own personalized machine…*hackernoon.com](https://hackernoon.com/how-to-label-data-create-ml-for-object-detection-82043957b5cb)