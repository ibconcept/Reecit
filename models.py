from app import db

class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    items = db.Column(db.Text, nullable=False)
    color = db.Column(db.String(50), nullable=True)
    alignment = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(100), nullable=True)  # Add this line to store the image filename
    pdf_url = db.Column(db.String(200), nullable=True)  # Store URL to the PDF file
    date = db.Column(db.DateTime, default=db.func.now())  # Add a date field for receipt creation

    def __repr__(self):
        return f'<Receipt {self.id}>'
