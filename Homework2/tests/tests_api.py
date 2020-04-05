import pytest


class TestApi():
    
    @pytest.mark.API
    def test_auth(self, api_client, authorization):
        location = api_client.redir_auth(*authorization)
        assert location == 'http://mail.my.com/'

        
    @pytest.mark.API
    def test_create_segmentum(self, api_client, new_data):
        api_client.login()
        assert api_client.create_segmentum(new_data).status_code == 200


    @pytest.mark.API
    def test_delete_segmentum(self, api_client, new_data):
        api_client.login()
        id = api_client.create_segmentum(new_data).json()['id']
        
        assert api_client.delete_segmentum(id) == 204
        