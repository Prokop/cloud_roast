from cloudroast.images.fixtures import ImagesFixture


class TestCreateNamespaces(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestCreateNamespaces, cls).setUpClass()
        cls.namespaces_to_delete = []

    @classmethod
    def tearDownClass(cls):
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestCreateNamespaces, cls).tearDownClass()

    def test_create_namespaces(self):
        response = self.images_client.create_namespace(namespace='test_namespace')
        self.assertEqual(response.status_code, 201)
        namespace = response.entity
        self.namespaces_to_delete.append(namespace.namespace)
        self.assertEqual(namespace.namespace, 'test_namespace')

