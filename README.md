# ApiTestManage
喜欢哒！顺手帮忙点个star呗~~谢谢！！如有疑问可联系qq：362508572   或q群：700387899

前端传送门：https://github.com/pencil1/ApiTestWeb

## Environment
python => 3


## 开发环境
    manage.py


## 生产环境
    gunicorn -c gunicorn_config.py manage:app

### 生产环境下的一些配置
由于懒，直接把flaskapi.conf文件替换nginx下的nginx.conf


### 数据库的迁移

第一次使用：
初始化：

    (venv)  flask db init 这个命令会在项目下创建 migrations 文件夹，所有迁移脚本都存放其中。


创建第一个版本：

    (venv) $ flask db migrate


运行升级

    (venv) $ flask db upgrade

后缀更新：
更新表格的字段 (models.py)
再次运行一下

    flask db migrate -> 相当于commit 更新到/migrate目录
    flask db upgrade -> 数据库会更新


fix issues

    1、修改case manage.py params 'variables' to 'variable'