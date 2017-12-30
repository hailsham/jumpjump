# 微信小游戏跳一跳

## 游戏原理
![](file:///C:UsersArexyDesktop/tiaotiaotiao/s1.png)
每次需要通过点击屏幕来控制小人跳到下一个砖块，点击时间的长短会控制小人跳的远近，跳到砖块正中心有额外的bonus, 有些特殊的砖块会有额外的bonus，像音乐盒，便利店这样的。

## 算法原理
>当前帧画面作为输入，提取小人和目的方块的位置，计算这两个位置之间的距离，然后转换成点击屏幕的时间，然后点击，迭代。

### 环境配置
- Python2.7
- Adb 驱动
- opencv3.2
- 三星S7Edge

### 操作说明
插入手机，确保`Adb工具`已经连接上手机，即`ada devices`能找到设备id，运行`main.py`，然后看着它玩即可。

### 文件说明
- `location.py` ： `get_dist()`负责检测小人坐标`person_cor`，目的砖块`dst_cor`；`dist2time`负责把小人和目的砖块之前的距离转化成时间。
- `main.py`： `jump()`和`get_screen()`封装了`Adb`的工具，完成截取手机屏幕和按指定时长点击屏幕2个动作。

##  Tips:
1. 有几种情况目的地检测会失效
