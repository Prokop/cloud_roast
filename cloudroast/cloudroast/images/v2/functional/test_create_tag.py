from cloudroast.images.fixtures import ImagesFixture


class TestCreateTag(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestCreateTag, cls).setUpClass()
        response = cls.images_client.create_namespace(
            namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        cls.tags_to_delete = []

    @classmethod
    def tearDownClass(cls):
        for tag in cls.tags_to_delete:
            cls.images_client.delete_tag_definition('test_namespace', name=tag)
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestCreateTag, cls).tearDownClass()

    def test_create_tag(self):
        response = self.images_client.create_tags('test_namespace',
                                                  'test_tag')
        self.assertEqual(response.status_code, 201)
        tags = response.entity
        self.assertEqual(len(tags), 1)
        self.assertEqual(tags[0].name, 'test_tag')
        self.tags_to_delete.append('test_tag')
