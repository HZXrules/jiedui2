import os
from flask import Flask,render_template,request,redirect,flash,url_for,abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.secret_key='secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path,'data.db') #或者去env里读
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #不设置会得到警告

City_name=['全国','安徽','北京','重庆','福建','甘肃','广东','广西','贵州','海南','河北','河南','黑龙江'
,'湖北','湖南','吉林','江苏','江西','辽宁','内蒙古','宁夏','青海','山东','山西','陕西','上海'
,'四川','天津','西藏','新疆','云南','浙江']

class City(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    today_ip = db.Column(db.Integer,default=0)
    today_sp = db.Column(db.IntegerInteger,default=0)
    today_critical = db.Column(db.IntegerInteger,default=0)
    all_ip = db.Column(db.IntegerInteger,default=0)
    all_cure = db.Column(db.IntegerInteger,default=0)
    all_dead = db.Column(db.IntegerInteger,default=0)

def initdb():
    db.drop_all()
    db.create_all()
    for i in City_name:
        city = City(name=i)
        db.session.add(city)

    db.session.commit()






