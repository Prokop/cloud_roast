from cloudroast.images.fixtures import ImagesFixture


class TestGetNamespace(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetNamespace, cls).setUpClass()
        response = cls.images_client.create_namespace(namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]

    @classmethod
    def tearDownClass(cls):
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestGetNamespace, cls).tearDownClass()

    def test_get_namespace(self):
        response = self.images_client.get_namespace('test_namespace')
        self.assertEqual(response.status_code, 200)
        namespace = response.entity
        self.assertEqual(namespace.namespace, 'test_namespace')
