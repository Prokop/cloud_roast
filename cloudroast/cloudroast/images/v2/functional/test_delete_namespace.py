from cloudroast.images.fixtures import ImagesFixture


class TestDeleteNamespace(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestDeleteNamespace, cls).setUpClass()
        response = cls.images_client.create_namespace(namespace='test_namespace')
        assert response.status_code == 201

    def test_delete_namespace(self):
        response = self.images_client.delete_namespace('test_namespace')
        self.assertEqual(response.status_code, 204)

