import json

from django.contrib.auth import get_user_model
from django.test import Client, TestCase



class ClientTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.userModel = get_user_model()

    def test_authenticate_rejects_get_requests(self):
        response = self.client.get('/api/authenticate/')

        assert response.status_code == 405

    def test_authenticate_accepts_post_requests(self):
        client = self.userModel.objects.create_user(
            email='drgalindo@galindo.com.mx',
            first_name='Memo',
            last_name='Gonzalez',
            password='drAwe$ome'
        )
        response = self.client.post(
            '/api/authenticate/',
            json.dumps({
                "email": "drgalindo@galindo.com.mx",
                "password": "drAwe$ome"}),
            content_type='application/json')

        assert response.status_code == 200

    def test_authenticate_rejects_bad_credentials(self):
        response = self.client.post(
            '/api/authenticate/',
            json.dumps({"email": "x@x.xx", "password": "Nope"}),
            content_type='application/json')

        assert response.status_code == 403
