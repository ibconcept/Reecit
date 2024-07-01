from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Receipt  # Import the database and models
from fpdf import FPDF  # Import FPDF for PDF generation
import os
from forms import ReceiptForm

app = Flask(__name__)
app.config.from_object('config.Config')  # Load configuration from config.py
db.init_app(app)

# Helper function to check file extensions
def allowed_file(filename):
    """Check if the file has an allowed extension."""
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Define routes
@app.route('/')
@app.route('/index')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/list_receipts')
def list_receipts():
    """Render the list of receipts."""
    receipts = Receipt.query.all()
    return render_template('list_receipts.html', receipts=receipts)

@app.route('/new_receipt', methods=['GET', 'POST'])
def new_receipt():
    """Handle form submission and receipt creation."""
    form = ReceiptForm()

    if form.validate_on_submit():
        # Extract data from the form
        name = form.name.data
        amount = form.amount.data
        items = form.items.data
        color = form.color.data
        alignment = form.alignment.data
        image = form.image.data

        # Process the uploaded image
        filename = None
        if image and allowed_file(image.filename):
            filename = image.filename
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Create a new receipt
        receipt = Receipt(
            name=name,
            amount=amount,
            items=items,
            image=filename,
            color=color,
            alignment=alignment
        )
        db.session.add(receipt)
        db.session.commit()

        # Generate the PDF
        pdf_filename = f'receipt_{receipt.id}.pdf'
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename)
        generate_pdf(receipt, pdf_path)

        # Update the receipt with the PDF URL
        receipt.pdf_url = url_for('static', filename=f'uploads/{pdf_filename}')
        db.session.commit()

        flash('Receipt created successfully! PDF generated.', 'success')
        return redirect(url_for('list_receipts'))

    return render_template('new_receipt.html', form=form)

def generate_pdf(receipt, path):
    """Generate a PDF for the receipt."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Receipt ID: {receipt.id}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Name: {receipt.name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Amount: ${receipt.amount:.2f}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Date: {receipt.date.strftime('%Y-%m-%d')}", ln=True, align='L')
    pdf.cell(200, 10, txt="Items:", ln=True, align='L')
    pdf.multi_cell(0, 10, receipt.items)
    
    if receipt.image:
        pdf.image(os.path.join(app.config['UPLOAD_FOLDER'], receipt.image), x=10, y=pdf.get_y(), w=50)  # Adjust image placement if needed

    pdf.output(path)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True, port=5000)  # Run the app in debug mode on port 5000
