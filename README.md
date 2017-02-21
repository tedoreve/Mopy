# Mopy
![](Moppy.jpg)

This is a python code package used to fuck the network. The below shows the instructions of three files, respectively. Because the bili.py is only related to a Chinese website, there is only Chinese instruction for it.

##LAN net.py

##Mozila net.py

##bili.py
1. 程序作用：
将B站视频地址和播放时间按顺序导入，运行后就会开启洗脑列表循环，所有列表中的视频都会重复以下流程
在网页中打开->网页最大化->视频最大化->视频按照播放时间播放结束->关闭上一个视频，开始下一个视频
最后一个视频结束后会自动跳转到第一个再循环播放
2. 前期准备：
安装python3，推荐使用anaconda最新版本,不然其他依赖包要自己装->安装selenium，可以使用pip，如果安装了anaconda,可以直接使用conda install -c conda-forge selenium=3.0.2->如果使用Firefox,下载geckodriver.exe（自行搜索），并将其所在路径加入环境变量PATH。如果使用Chrome，下载chromedriver.exe，然后同上。Chrome没有测试过，推荐使用Firefox.
3. 使用说明：
打开命令行->进入bili.py所在目录->输入python bili.py，如果安装anaconda,可以直接在编辑器中运行。
在urllist中输入视频地址，timelist中对应输入想要播放的时间，如果比视频时间短，那就只播放前面部分，如果比视频时间长，那视频播放完了会停止播放，等到时间过去再播放下一个视频。
t可以控制从第几个视频开始播放，t=0即从第一个视频开始播放，t=10即从第11个视频开始播放。
driver.set_page_load_timeout(5)中的‘5’是可忍受的页面加载时间，单位（s），如果网速太慢，要调高这个数值，推荐5——20。

* 视频教程：http://www.bilibili.com/video/av8737418/
