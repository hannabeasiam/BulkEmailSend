from flask import url_for


class TestPage(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_login_page(self, client):
        """ Login page should respond with a success 200. """
        response = client.get(url_for('page.login'))
        assert response.status_code == 200

    def test_register(self, client):
        """ Register page should respond with a success 200. """
        response = client.get(url_for('page.register'))
        assert response.status_code == 200
