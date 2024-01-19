from extension import db​

from flask_admin import Admin​

from flask_admin.contrib.sqla import ModelView​

from flask import Flask, render_template, url_for, redirect, request​

from models import User, Post​

​

admin = Admin()​

​

class PostView(ModelView):​

    can_delete = False​

    form_columns = ["title", "body", "user"]​

    column_list = ["title", "body", "user"]​

​

admin.add_view(ModelView(User, db.session))​

admin.add_view(PostView(Post, db.session))​

​

app = Flask(__name__)
app = Flask(__name__)​

​

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'​

app.config['SECRET_KEY'] = 'this is a secret key '​



db.init_app(app)​

admin.init_app(app)​


if __name__ == "__main__":​

    with app.app_context():​

        db.create_all()​

    app.run(debug=True)​​

​