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

## 公告
如果你**退出登录**或者**重新登录微信**，Cookie是会变更的，是**需要重新抓包获取新的Cookie**，除非你电脑不关机，或者关机后微信不登录，Cookie才不会变，其实更**建议你们从手机抓包软件抓取微信Cookie**，因为手机微信一般不会退出，所以Cookie不容易失效，但是电脑抓简单一点
## 支持的签到模式  
- ✅ 二维码签到（验证通过）
- ✅ GPS签到  （验证通过）
- 🚧 密码签到  

## 功能
- ✅ 定时检测GPS签到任务
- ✅ 24小时无人值守
- ✅ 通过自定义经纬度完成定位签到  
## 即将加入
- [ ] 定时开启
- [ ] 保存配置文件

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
    - X(填写纬度，格式x.x.x)  
    - Y(填写经度，格式y.y.y)
    - ACC(未知参数，可能是海拔)  
    - SearchTime(检索间隔，建议>＝60s)  
    - MyCookie(填写你的Cookie，下面有教程)
    - token(填写PUSHPLUS的Token，不使用请留空)
   
3.程序将执行**无限循环**用于检索签到任务，如需**停止请手动关闭** 
## 如何获取Cookie和班级ID
需要使用抓包软件（Fiddler,HttpCanary,抓包精灵）从微信抓取Cookie  

1.下载抓包软件  

2.打开抓包软件开启抓包  

3.从微信电脑版进入班级魔方签到界面  


使用Fiddler抓取演示：  
1.打开Fiddler  
2.进入图中1的签到界面  
3.找到图中2的链接，双击进入  
4.点击图中3的数据  
5.图中4的Cookie：后的部分就是你的Cookie  
6.图中5的数字就是你的班级ID  
![Screenshot 2024-03-28 024226](https://github.com/JasonYANG170/AutoCheckBJMF/assets/39414350/6453fc70-f8a9-4336-8778-21a642424732)




## 已知问题
#### 1.使用浏览器获取的Cookie不稳定会失效，建议用户从微信抓取Cookie
#### 2.班级魔方屏蔽了海外IP，请使用中国IP的设备运行，否则会出现连接超时。




