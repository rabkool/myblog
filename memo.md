## 环境搭建
#### ubuntu root默认密码修改
```
sudo passwd
```

#### 指令等
- pip工具安装
```
sudo apt-get install python3-pip
```

- django安装
```
pip3 install django
```

- django-mdeditor
```
pip3 install django-mdeditor
```

- markdown安装
```
pi3p install markdown
```

- 查看django版本
```
pip3 show django
```

- 创建项目
```
django-admin startproject 想要名称
```

- 创建应用
```
python manage.py startapp 想要名称
添加应用名到settings.py中的INSTALLED_APPS里
```

- 启动服务
```
python manage.py runserver  (服务端口号可自定义)
python3 manage.py runserver --insecure
python3 manage.py runserver --insecure & (ssh关了进程也不会结束)
```

- 查看服务器启动状态
```
ps -aux | grep python

ps aux | grep -i manage
```

- 关闭服务器
```
sudo kill -9 (端口号)
```

## 雑

1.创建页面
    编辑blog.views
        每一个页面对应一个函数 函数必须返回一个响应
        函数必须存在一个参数 一般定成request
        每一个响应(函数)对应一个URL

2.编辑URL
    编辑urls.py
        每个URL都以url的形式写出
        url函数放在urlpatterns列表中
        url函数三个参数: URL(正则) , 对应方式 , 名称

## 创建模型
1.设计模型

2.模型层定义字段
    创建文件
        命令: python manage.py makemigrations
    运行文件 同步到数据库
        命令: python manage.py migrate
