from cloudroast.images.fixtures import ImagesFixture


class TestCreateResourceTypeAssociation(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestCreateResourceTypeAssociation, cls).setUpClass()
        response = cls.images_client.create_namespace(namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        cls.resource_type_association_to_delete = []

    @classmethod
    def tearDownClass(cls):
        for resource_type in cls.resource_type_association_to_delete:
            cls.images_client.delete_resource_type_association(
            'test_namespace', name=resource_type)
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestCreateResourceTypeAssociation, cls).tearDownClass()

    def test_create_resource_type_association(self):
        response = self.images_client.create_resource_type_association(
            'test_namespace', name='test_resource_type_association')
        self.assertEqual(response.status_code, 201)
        resource_type_association = response.entity
        self.assertEqual(resource_type_association.name,
                         'test_resource_type_association')
        self.resource_type_association_to_delete.append(
            'test_resource_type_association')



