# 微信小游戏跳一跳

## 游戏原理 
每次需要通过点击屏幕来控制小人跳到下一个砖块，点击时间的长短会控制小人跳的远近，跳到砖块正中心有额外的bonus, 有些特殊的砖块会有额外的bonus，像音乐盒，便利店这样的。
![](./pictures/s1o.png)

## 算法原理
当前帧画面作为输入，提取小人和目的方块的位置，计算这两个位置之间的距离，然后转换成点击屏幕的时间，然后点击，循环。  
![](./pictures/s1line.jpg)

### 环境配置
- Python2.7
- [Adb 驱动](http://www.mz6.net/news/2016-03-07/4506.html)
- [opencv3.2](https://opencv.org/)
- [安卓手机](https://item.jd.com/4157994.html)

### 操作说明
插入手机，确保`Adb工具`已经连接上手机，即`ada devices`能找到设备id，运行`main.py`，然后看着它玩即可。

### 文件说明
- `location.py` ： `get_dist()`负责检测小人坐标`person_cor`，目的砖块`dst_cor`；`dist2time`负责把小人和目的砖块之前的距离转化成时间。
- `main.py`： `jump()`和`get_screen()`封装了`Adb`的工具，完成截取手机屏幕和按指定时长点击屏幕2个动作。

##  Tips:
1. 由于各个手机分辨率的不同，`get_dist()`中一开始的`resize`*可能*要调整，裁剪的目的是截取画面中间信息，去掉上下多余的部分，最后要保证是一个320x275的图像，否则`dist2time()`中的系数也要调整。
>    img = cv2.resize(img, (288, 512), fx=0,  fy =0, interpolation = cv2.INTER_CUBIC)  
>    img = img[100:450, 20:275]
![](./pictures/img1.jpg)           ![](./pictures/img2.jpg)

2. 有几种情况目的地检测会失效
	- 目的砖块过小，在检测和控制两方面的误差下，可能会跳不上去。  
	![](./pictures/far.jpg)	
	- 在特定的背景和砖块颜色下，会检测不到砖块，目的砖块坐标也会失效。
	
3. 在控制方面，参考了@[wangshub](https://github.com/wangshub/wechat_jump_game)的做法,用adb来控制。我和[冬强](https://github.com/cdq4817)最开始是打算用机械臂来完成，机械臂如下图，硬件方面的控制调试组装都是冬强完成的，后续等他回来我们可能会完成这个用硬件实现的跳一跳。
![](./pictures/control.jpg)。 苹果手机的控制我不熟悉，可以参考[wangshub](https://github.com/wangshub/wechat_jump_game)的做法。

4. 鉴于*Tips2*，所以你能玩到多少分全凭运气，是从几十到几千的均匀分布。