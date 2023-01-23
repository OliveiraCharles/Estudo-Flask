from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)  # Não armazenar senhas em plaintext
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    # Construtor
    def init(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email


def __repr__(self):
    return "<User %r>" % self.username


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.Column(db.relationship('User', foreign_keys=user_id))

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.Model):
    __tablename__ = 'follow'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    folower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=folower_id)
