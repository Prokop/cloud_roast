from cloudroast.images.fixtures import ImagesFixture


class TestDeleteResourceTypeAssociation(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestDeleteResourceTypeAssociation, cls).setUpClass()
        response = cls.images_client.create_namespace(
            namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        response = cls.images_client.create_resource_type_association(
            'test_namespace', name='test_resource_type_association')
        assert response.status_code == 201

    @classmethod
    def tearDownClass(cls):
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestDeleteResourceTypeAssociation, cls).tearDownClass()

    def test_delete_resource_type_association(self):
        response = self.images_client.delete_resource_type_association(
            'test_namespace', 'test_resource_type_association')
        self.assertEqual(response.status_code, 204)