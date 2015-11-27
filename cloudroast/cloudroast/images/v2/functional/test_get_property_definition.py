from cloudroast.images.fixtures import ImagesFixture


class TestGetPropertyDefinition(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetPropertyDefinition, cls).setUpClass()
        response = cls.images_client.create_namespace(
            namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        response = cls.images_client.create_property('test_namespace',
            name='test_property', type='string', title='Hypervisor Type',
            enum=["xen"])
        assert response.status_code == 201
        cls.properties_to_delete = []

    @classmethod
    def tearDownClass(cls):
        for property in cls.properties_to_delete:
            cls.images_client.remove_property_definition(
            'test_namespace', name=property)
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestGetPropertyDefinition, cls).tearDownClass()

    def test_get_property_definition(self):
        response = self.images_client.get_property_definition(
            'test_namespace', 'test_property')
        self.assertEqual(response.status_code, 200)
        self.properties_to_delete.append('test_property')