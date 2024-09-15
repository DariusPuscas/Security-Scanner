import pytest
from app import app, db, Vulnerability


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # test database
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_add_vulnerability(client):
    response = client.post('/vulnerabilities/new', data={
        'url': 'https://example.com',
        'description': 'Test vulnerability',
        'status': 'Unresolved'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Vulnerability added successfully' in response.data


def test_update_vulnerability(client):
    # Add vulnerability first
    vulnerability = Vulnerability(url="https://test.com", description="Initial description", status="Unresolved")
    db.session.add(vulnerability)
    db.session.commit()

    # Update the vulnerability
    response = client.post(f'/vulnerabilities/update/{vulnerability.id}', data={
        'status': 'Resolved',
        'assigned_to': 'admin'
    }, follow_redirects=True)

    assert response.status_code == 200
    updated_vuln = Vulnerability.query.get(vulnerability.id)
    assert updated_vuln.status == 'Resolved'
    assert updated_vuln.assigned_to == 'admin'
