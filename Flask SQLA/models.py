from extension import db​

​

class User(db.Model):​

 id = db.Column(db.Integer, primary_key=True)​

 name = db.Column(db.String(50))​

 email = db.Column(db.String(120), unique=True, nullable=False)​

 password = db.Column(db.String(255), nullable=False)​

 posts = db.relationship("Post", back_populates="user")​

​

 def __str__(self):​

    return self.name​

​

class Post(db.Model):​

  id = db.Column(db.Integer, primary_key=True)​

  title = db.Column(db.String(100))​

  body = db.Column(db.Text)​

  user_id = db.Column(db.ForeignKey("user.id"), nullable=False)​

  user = db.relationship("User", back_populates="posts")​