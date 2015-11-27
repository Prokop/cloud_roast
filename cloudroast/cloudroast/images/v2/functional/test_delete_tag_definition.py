from cloudroast.images.fixtures import ImagesFixture


class TestDeleteTagDefinition(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestDeleteTagDefinition, cls).setUpClass()
        response = cls.images_client.create_namespace(
            namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        response = cls.images_client.create_tags('test_namespace', 'test_tag')
        assert response.status_code == 201

    @classmethod
    def tearDownClass(cls):
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestDeleteTagDefinition, cls).tearDownClass()

    def test_delete_tag_definition(self):
        response = self.images_client.delete_tag_definition('test_namespace',
                                                  name='test_tag')
        self.assertEqual(response.status_code, 204)
        response = self.images_client.list_tags(namespace='test_namespace')
        tags = response.entity
        self.assertEqual(len(tags), 0)


