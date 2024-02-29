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
- [x] 二维码签到
- [x] GPS签到
- [x] 密码签到 

## 功能
- [x] 定时检测GPS签到任务
- [x] 24小时无人值守
- [x] 通过自定义经纬度完成定位签到 

如您使用其他以时间结算的加速器请向我提出issues
## 使用教程
1.下载ZIP或Clone到本地。 

2.自行安装python，pip，然后在控制台输入以下命令安装python依赖包  

    - pip install requests  
    - pip install beautifulsoup4

3.主机用户可直接点击main.py运行即可  
*本地服务器用户及GitHub Actions用户请自行修改main.py注释

2.填写以下变量  

    - ClassID(填写班级ID)  
    - X(填写纬度)  
    - Y(填写经度)
    - ACC(未知参数，可能是高度)  
    - SearchTime(查询时长，建议>60s)  
    - MyCookie(填写你的Cookie)
    - token(填写PUSHPLUS的Token，不使用推送请在main.py中注释88及89行代码)
   
3.程序将执行无限循环用于检索签到任务，如需停止请手动关闭 
## 已知问题
测试中发现班级魔方似乎屏蔽了海外IP，Github Actions及部分海外IP可能遇到连接超时，请使用代理程序或使用中国IP设备



