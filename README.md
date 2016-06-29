# 代码快捷同步到测试站以及正式站工具.
### 实现机制

* Git
* Python Flask 环境
* supervisor

### 操作示意图1
![image](images/code-deploy.png)

### 操作示意图2
![image](images/code-deploy2.png)



_____

###使用方法

1. 部署一个远程git仓库, 确保各个服务器均能访问.并且与各个服务器配置好 
	* 迁移本地git仓库至远程服务器,可直接将本地服务器仓库的 projectxxx.git 打包传输到远程服务器再解压.所有日志和改动都会被保留下来. 
	* [无密码访问设置](http://blog.csdn.net/haigenwong/article/details/7410914) 
2.  Python 出发git pull 脚本设置
	* 安装python
	* 安装flask
	* [python web 脚本](dogit.py). 
	* 运行 ``python dogit.py``
	* 此时浏览器访问 IP:5000 即可成功使用python 做 同步操作.
3.  supervisor 管控flask 执行.
	```
	gunicorn -w4 -b0.0.0.0:5000 dogit:app &
	# -b 设置 ip 以及端口
	# -w 设置线程数
	# dogit 为需要后台执行的 py文件名
	# :app Flask 声明的变量名称 app = Flask(__name__)
	```
	 
	 