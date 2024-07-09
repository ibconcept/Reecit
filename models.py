from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    items = db.Column(db.Text, nullable=False)
    color = db.Column(db.String(20), nullable=True)
    alignment = db.Column(db.String(20), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Receipt id={self.id}, name='{self.name}', amount={self.amount}>"
