from cloudroast.images.fixtures import ImagesFixture


class TestUpdatePropertyDefinition(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestUpdatePropertyDefinition, cls).setUpClass()
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
        super(TestUpdatePropertyDefinition, cls).tearDownClass()

    def test_update_property_definition(self):
        response = self.images_client.get_property_definition(
            'test_namespace', 'test_property')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.entity.title, 'Hypervisor Type')
        response = self.images_client.update_property_definition(
            'test_namespace',  name='test_property', type='string',
            title='Not Hypervisor Type', enum=["xen"])
        self.assertEqual(response.status_code, 200)
        response = self.images_client.get_property_definition(
            'test_namespace', 'test_property')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.entity.title, 'Not Hypervisor Type')
        self.properties_to_delete.append('test_property')