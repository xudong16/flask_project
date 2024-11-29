from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库连接字符串，这里使用SQLite数据库，文件名为hr_management.db
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///hr_management.db'
# 关闭对模型修改的追踪，减少内存消耗，一般在生产环境推荐这样设置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)