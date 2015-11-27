from cloudroast.images.fixtures import ImagesFixture


class TestUpdateNamespace(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestUpdateNamespace, cls).setUpClass()
        response = cls.images_client.create_namespace(
            namespace='test_namespace', description='foo')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]

    @classmethod
    def tearDownClass(cls):
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestUpdateNamespace, cls).tearDownClass()

    def test_update_namespace(self):
        response = self.images_client.get_namespace('test_namespace')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.entity.description, 'foo')
        response = self.images_client.update_namespace(
            'test_namespace', description='bar')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.entity.namespace, 'test_namespace')
        self.assertEqual(response.entity.description, 'bar')
        response = self.images_client.get_namespace('test_namespace')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.entity.description, 'bar')
