from cloudroast.images.fixtures import ImagesFixture


class TestAddTagDefinition(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestAddTagDefinition, cls).setUpClass()
        response = cls.images_client.create_namespace(
            namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        response = cls.images_client.create_tags('test_namespace', 'test_tag')
        assert response.status_code == 201
        cls.tags_to_delete = [response.entity[0].name]

    @classmethod
    def tearDownClass(cls):
        for tag in cls.tags_to_delete:
            cls.images_client.delete_tag_definition('test_namespace', name=tag)
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestAddTagDefinition, cls).tearDownClass()

    def test_add_tag_definition(self):
        response = self.images_client.add_tag_definition('test_namespace',
                                                  name='additional_test_tag')
        self.assertEqual(response.status_code, 201)
        response = self.images_client.list_tags(namespace='test_namespace')
        tags = response.entity
        self.assertEqual(len(tags), 2)
        self.assertEqual(tags[0].name, 'additional_test_tag')
        self.tags_to_delete.append('additional_test_tag')
