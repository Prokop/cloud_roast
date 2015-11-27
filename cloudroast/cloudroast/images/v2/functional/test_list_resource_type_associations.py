from cloudroast.images.fixtures import ImagesFixture


class TestListResourceTypesAssociations(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestListResourceTypesAssociations, cls).setUpClass()
        response = cls.images_client.create_namespace(namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]

    @classmethod
    def tearDownClass(cls):
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestListResourceTypesAssociations, cls).tearDownClass()

    def test_list_resource_types_associations(self):
        response = self.images_client.list_resource_type_associations(namespace='test_namespace')
        self.assertEqual(response.status_code, 200)
