from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/risiti'
# app.static_folder = 'static'  # Set the static folder directly

db = SQLAlchemy(app)

# Define database models
class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Define other fields for the receipt model (e.g., items, amount, date, etc.)

# Define routes
@app.route('/')
def base():
    return render_template('base.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/list_receipts')
def list_receipts():
    receipts = Receipt.query.all()
    return render_template('list_receipts.html')

#  receipts=receipts

@app.route('/new_receipt', methods=['GET', 'POST'])
def new_receipt():
    if request.method == 'POST':
        # Process form data and create a new receipt
        # Example:
        # receipt = Receipt(name=request.form['name'], amount=request.form['amount'])
        # db.session.add(receipt)
        # db.session.commit()
        return redirect(url_for('list_receipts'))
    return render_template('new_receipt.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
