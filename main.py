from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_wkhtmltopdf import Wkhtmltopdf 
# module_for pdf is this one above here

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/risiti'
# app.config['WKHTMLTOPDF_CMD'] = '/path/to/wkhtmltopdf'  # Set path to wkhtmltopdf binary
# app.static_folder = 'static'  # Set the static folder directly

db = SQLAlchemy(app)
# pdf = Wkhtmltopdf(app)

# Define database models
class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Define other fields for the receipt model (e.g., items, amount, date, etc.)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receipts')
def list_receipts():
    receipts = Receipt.query.all()
    return render_template('receipts.html', receipts=receipts)

@app.route('/receipts/new', methods=['GET', 'POST'])
def new_receipt():
    if request.method == 'POST':
        # Process form data and create a new receipt
        # Example:
        # receipt = Receipt(name=request.form['name'], amount=request.form['amount'])
        # db.session.add(receipt)
        # db.session.commit()
        return redirect(url_for('list_receipts'))
    return render_template('new_receipt.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Extract form data for receipt customization
    # Example:
    # color = request.form['color']
    # num_rows = int(request.form['num_rows'])
    # num_cols = int(request.form['num_cols'])
    # logo = request.files['logo']  # Assuming logo is uploaded as a file
    # address = request.form['address']
    
    # Generate HTML content for the receipt
    # Example:
    # html_content = render_template('receipt_template.html', color=color, num_rows=num_rows, num_cols=num_cols, address=address)
    
    # Generate PDF from HTML content
    # pdf_data = pdf.html_to_pdf(html_content)
    
    # Save PDF data to a file or return as a response
    # Example:
    # with open('receipt.pdf', 'wb') as f:
    #     f.write(pdf_data)
    
    # return jsonify({'success': True})  # Return JSON response if needed
    return redirect(url_for('list_receipts'))  # Redirect to the list of receipts

if __name__ == '__main__':
    app.run(debug=True, port=5000)
