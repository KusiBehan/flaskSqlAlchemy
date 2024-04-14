import os

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskSqlAlchemy.db'
#app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(app.instance_path, 'users.db')
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]


user1 = User(id=1, username="mockuser1", email="mock@gmail.com")
user2 = User(id=2, username="mockuser2", email="test@gmail.com")
user3 = User(id=3, username="mockuser3", email="outlook@gmail.com")
user4 = User(id=4, username="mockuser4", email="apple@gmail.com")

userList = [user1, user2, user3, user4]

with app.app_context():
    db.create_all()
    db.session.add_all(userList)
    db.session.commit()

app.run(host='0.0.0.0', debug=True)
@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("user/list.html", users=users)
