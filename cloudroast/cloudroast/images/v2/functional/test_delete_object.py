from cloudroast.images.fixtures import ImagesFixture


class TestDeleteObject(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestDeleteObject, cls).setUpClass()
        response = cls.images_client.create_namespace(
            namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        response = cls.images_client.create_object(
            'test_namespace', name='test_object',
            properties={"quota:cpu_period": {"description":
            "A period with value 0 means no value.","maximum": 1000000,
            "minimum": 1000,"title": "Quota: CPU Period","type": "integer"}},
            required=['1'])
        assert response.status_code == 201

    @classmethod
    def tearDownClass(cls):
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestDeleteObject, cls).tearDownClass()

    def test_delete_object(self):
        response = self.images_client.delete_objects_definition(
            'test_namespace', 'test_object')
        self.assertEqual(response.status_code, 204)