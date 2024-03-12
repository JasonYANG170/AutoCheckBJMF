<div align="center">
    <h1>AutoCheckBJMF 班级魔方自动签到</h1>
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

如遇问题，请向我提出issues
## 使用教程
#### 普通用户
1.在releases下载exe程序后点击运行即可
#### 服务器用户
1.下载ZIP或Clone到本地。  
2.自行安装python，pip，然后在控制台输入以下命令安装python依赖包  

    - pip install requests  
    - pip install beautifulsoup4

3.请自行修改main.py注释
#### Github Action用户
1.已经提供了yml配置文件  
2.修改main.py  
2.在仓库Setting～Secrets中添加配置信息即可  
## 配置信息
2.填写以下变量  

    - ClassID(填写班级ID)  
    - X(填写纬度)  
    - Y(填写经度)
    - ACC(未知参数，可能是海拔)  
    - SearchTime(查询时长，建议>60s)  
    - MyCookie(填写你的Cookie，下面有教程)
    - token(填写PUSHPLUS的Token，不使用推送请在main.py中注释88及89行代码)
   
3.程序将执行**无限循环**用于检索签到任务，如需**停止请手动关闭** 
## 如何获取Cookie和班级ID
需要使用抓包软件（Fiddler,HttpCanary,抓包精灵）从微信抓取Cookie  

1.下载抓包软件  

2.打开抓包软件开启抓包  

3.从微信电脑版进入班级魔方签到界面  


使用Fiddler抓取演示：  
1中结尾的98969为班级ID，  
2中的即是我们要用到的Cookie.  
![屏幕截图 2024-03-11 120501](https://github.com/JasonYANG170/AutoCheckBJMF/assets/39414350/c695c890-de8d-4a4f-aee4-a892b5ab7c29)


## 已知问题
#### 1.使用浏览器获取的Cookie不稳定会失效，建议用户从微信抓取Cookie
#### 2.班级魔方屏蔽了海外IP，请使用中国IP的设备运行，否则会出现连接超时。




