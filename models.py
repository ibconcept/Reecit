#models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    items = db.Column(db.Text, nullable=False)
    color = db.Column(db.String(50), nullable=True)
    alignment = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(100), nullable=True)  # Store the image filename
    pdf_url = db.Column(db.String(200), nullable=True)  # Store URL to the PDF file
    date = db.Column(db.DateTime, default=db.func.now())  # Date field for receipt creation

    def __repr__(self):
        return f'<Receipt {self.id}>'




# from flask_login import UserMixin

# db = SQLAlchemy()

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'