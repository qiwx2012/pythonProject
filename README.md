第一个实战项目
1、使用pip安装开发webApp需要的第三方库
  .异步框架 aiohttp
         pip3 install aiohttp
  .前端模板引擎 jinja2
         pip3 install jinja2
  .MySQL的python异步驱动程序 aiomysql
         pip3 install aiomysql

2、项目目录
awesome-python3-webapp/  <-- 根目录
|
+- backup/               <-- 备份目录
|
+- conf/                 <-- 配置文件
|
+- dist/                 <-- 打包目录
|
+- www/                  <-- Web目录，存放.py文件
|  |
|  +- static/            <-- 存放静态文件
|  |
|  +- templates/         <-- 存放模板文件
|
+- ios/                  <-- 存放iOS App工程
|
+- LICENSE               <-- 代码LICENSE

3、
# pythonProject
