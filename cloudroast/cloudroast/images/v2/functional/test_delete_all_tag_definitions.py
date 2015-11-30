from cloudroast.images.fixtures import ImagesFixture


class TestDeleteAllTagDefinitions(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestDeleteAllTagDefinitions, cls).setUpClass()
        response = cls.images_client.create_namespace(namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        response = cls.images_client.create_tags('test_namespace', 'test_tag')
        assert response.status_code == 201

    @classmethod
    def tearDownClass(cls):
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestDeleteAllTagDefinitions, cls).tearDownClass()

    def test_delete_all_tag_definitions(self):
        response = self.images_client.delete_tags('test_namespace')
        self.assertEqual(response.status_code, 200)
        response = self.images_client.list_tags(namespace='test_namespace')
        self.assertEqual(response.status_code, 200)
        tags = response.entity
        self.assertEqual(len(tags), 0)


