#app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from forms import ReceiptForm
from models import db, Receipt
from datetime import datetime
from config import Config  # Import Config class from config.py

def create_app():
    """Application factory function."""
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    db.init_app(app)

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

            # Create a new receipt
            receipt = Receipt(
                name=name,
                amount=amount,
                items=items,
                color=color,
                alignment=alignment,
                date=datetime.utcnow()  # Use current datetime for 'date' field
            )
            db.session.add(receipt)
            db.session.commit()

            flash('Receipt created successfully!', 'success')
            return redirect(url_for('render_receipt', receipt_id=receipt.id))

        return render_template('new_receipt.html', form=form)

    @app.route('/receipt/<int:receipt_id>')
    def render_receipt(receipt_id):
        """Render the receipt to a new HTML route."""
        receipt = Receipt.query.get_or_404(receipt_id)
        return render_template('receipt.html', receipt=receipt)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
