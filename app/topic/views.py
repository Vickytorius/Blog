#导入topic蓝图程序用于声明路由
from flask import *

from . import topic

@topic.route('/')
def topic_index():
    # return render_template("index.html")
    pass