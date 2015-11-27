from cloudroast.images.fixtures import ImagesFixture


class TestRemovePropertyDefinition(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestRemovePropertyDefinition, cls).setUpClass()
        response = cls.images_client.create_namespace(
            namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        response = cls.images_client.create_property('test_namespace',
            name='test_property', type='string', title='Hypervisor Type',
            enum=["xen"])
        assert response.status_code == 201

    @classmethod
    def tearDownClass(cls):
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestRemovePropertyDefinition, cls).tearDownClass()

    def test_remove_property_definition(self):
        response = self.images_client.remove_property_definition (
            'test_namespace', 'test_property')
        self.assertEqual(response.status_code, 204)