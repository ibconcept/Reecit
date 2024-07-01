import pytest
import sys
import os

# Add the parent directory of the script to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Receipt

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory SQLite database for testing
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
        db.drop_all()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data  # Check if the HTML template is rendered

def test_list_receipts(client):
    response = client.get('/receipts')
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data  # Check if the HTML template is rendered

def test_new_receipt_get(client):
    response = client.get('/receipts/new')
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data  # Check if the HTML template is rendered

def test_new_receipt_post(client):
    response = client.post('/receipts/new', data={'name': 'Test Receipt', 'amount': '100'})
    assert response.status_code == 302  # Check for redirect
    assert response.headers['Location'] == '/receipts'  # Check the redirect location

def test_generate_pdf(client):
    response = client.post('/generate_pdf', data={
        'color': 'blue',
        'num_rows': '5',
        'num_cols': '3',
        'address': '123 Test St.'
    })
    assert response.status_code == 302  # Check for redirect
    assert response.headers['Location'] == '/receipts'  # Check the redirect location

if __name__ == '__main__':
    pytest.main()
