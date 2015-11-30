from cloudroast.images.fixtures import ImagesFixture


class TestCreateProperty(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestCreateProperty, cls).setUpClass()
        response = cls.images_client.create_namespace(namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        cls.properties_to_delete = []

    @classmethod
    def tearDownClass(cls):
        cls.images_client.remove_property_definition(
            'test_namespace', name='test_property')
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestCreateProperty, cls).tearDownClass()

    def test_create_properties(self):
        response = self.images_client.create_property(
            'test_namespace', name='test_property', type='string',
            title='Hypervisor Type', enum=["xen"])
        self.assertEqual(response.status_code, 201)
        property = response.entity
        self.assertEqual(property.name, 'test_property')
        self.properties_to_delete.append('test_property')



