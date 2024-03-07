<div align="center">
    <h1>AutoCheckBJMF 班级魔方自动GPS签到</h1>
    <img src="https://img.shields.io/github/license/JasonYANG170/AutoCheckBJMF?label=License&style=for-the-badge">
    <img src="https://img.shields.io/github/commit-activity/w/JasonYANG170/AutoCheckBJMF?style=for-the-badge">
<img src="https://img.shields.io/github/languages/count/JasonYANG170/AutoCheckBJMF?logo=python&style=for-the-badge">
	<br>
    	<a href="https://discord.com/invite/az3ceRmgVe"><img alt="Discord" src="https://img.shields.io/discord/978108215499816980?style=social&logo=discord&label=echosec"></a>
  <br>

这是一项基于Python语言的班级魔方GPS自动签到Script
  
<br>

</div>

## 支持的签到模式  
- ✅ 二维码签到（验证通过）
- ✅ GPS签到  （验证通过）
- 🚧 密码签到  

## 功能
- ✅ 定时检测GPS签到任务
- ✅ 24小时无人值守
- ✅ 通过自定义经纬度完成定位签到 

如您使用其他以时间结算的加速器请向我提出issues
## 使用教程
#### 普通用户
1.在releases下载exe程序后点击运行即可
#### 服务器用户
1.下载ZIP或Clone到本地。 

2.自行安装python，pip，然后在控制台输入以下命令安装python依赖包  

    - pip install requests  
    - pip install beautifulsoup4

3.请自行修改main.py注释
## 配置信息
2.填写以下变量  

    - ClassID(填写班级ID)  
    - X(填写纬度)  
    - Y(填写经度)
    - ACC(未知参数，可能是高度)  
    - SearchTime(查询时长，建议>60s)  
    - MyCookie(填写你的Cookie，下面有教程)
    - token(填写PUSHPLUS的Token，不使用推送请在main.py中注释88及89行代码)
   
3.程序将执行**无限循环**用于检索签到任务，如需**停止请手动关闭** 
## 如何获取Cookie和班级ID


有能力的我建议用抓包软件抓取微信的Cookie会更稳定一点


#### 1.使用微信电脑版进入班级魔方小程序，点击右上角地球图标使其在浏览器中打开
![屏幕截图 2024-02-29 183418](https://github.com/JasonYANG170/AutoCheckBJMF/assets/39414350/2998676c-50bc-4215-b93d-ca9de8929957)
#### 2.请先在浏览器中通过微信扫码登录，然后进入签到界面  
##### 2.1 按下电脑F12按键进入控制台，在控制台顶部选择网络选项卡
##### 2.2 刷新当前页面，找到名为punchs的活动
##### 2.3 下滑找到Cookie，右边的一大串就是你的Cookie
##### 2.4 Cookie下方的Referer中，末尾一串段数字就是你的班级ID
![屏幕截图 2024-02-29 183745](https://github.com/JasonYANG170/AutoCheckBJMF/assets/39414350/0542e5f1-2ef0-4dae-a8b5-adaaa0e8274a)

## 已知问题
#### 1.使用浏览器获取的Cookie不稳定会失效，建议用户从微信抓取Cookie
#### 2.班级魔方屏蔽了海外IP，请使用中国IP的设备运行，否则会出现连接超时。
测试中发现班级魔方似乎屏蔽了海外IP，Github Actions及部分海外IP可能遇到连接超时，请使用代理程序或使用中国IP设备



