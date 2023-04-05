from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)

    def __repr__(self):
        return f'{self.name} Author ID:{self.id}'

    @validates('name')
    def validate_name(self, key, name):
        names_list = db.session.query(Author.name).all()
        if not name:
            raise ValueError('Name field must be filled out')
        elif name in names_list:
            raise ValueError('Name must be unique')
        return name

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError('Phone number must have a length of 10')
        return phone_number
        

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)

    def __repr__(self):
        return f'Post title:{self.title}'

    @validates('title')
    def validate_title(self, key, title):
        clickbait = ["Won't Belive", "Secret", "Top", "Guess"]
        if not title:
            raise ValueError('Post must have a title')
        elif not any(bait in title for bait in clickbait):
            raise ValueError('Post has no clickbait')
        return title

    @validates('content')
    def validate_content(self, key, content):
        if len(content) <= 250:
            raise ValueError('Content must be greated than 250 characters long')
        return content

    @validates('summary')
    def vaildate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError('Summary exceeds 250 characters')
        return summary
    
    @validates('category')
    def validate_category(self, key, category):
        categories = ['Fiction', 'Non-Fiction']
        if category not in categories:
            raise ValueError('Invalid category')
        return category