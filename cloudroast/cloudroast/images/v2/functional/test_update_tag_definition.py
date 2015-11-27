from cloudroast.images.fixtures import ImagesFixture


class TestUpdateTagDefinition(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestUpdateTagDefinition, cls).setUpClass()
        response = cls.images_client.create_namespace(
            namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        response = cls.images_client.create_tags('test_namespace', 'test_tag')
        assert response.status_code == 201

    @classmethod
    def tearDownClass(cls):
        for tag in cls.tags_to_delete:
            cls.images_client.delete_tag_definition('test_namespace', name=tag)
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestUpdateTagDefinition, cls).tearDownClass()

    def test_update_tag_definitions(self):
        response = self.images_client.get_tag_definition('test_namespace',
                                                  name='test_tag')
        self.assertEqual(response.status_code, 200)
        tags = response.entity
        self.assertEqual(tags.name, 'test_tag')
        response = self.images_client.update_tag_definition('test_namespace',
                                    name = 'test_tag', new_name='new_test_tag')
        self.assertEqual(response.status_code, 200)
        response = self.images_client.get_tag_definition('test_namespace',
                                                  name='new_test_tag')
        self.assertEqual(response.status_code, 200)
        tag = response.entity
        self.assertEqual(tag.name, 'new_test_tag')
        self.tags_to_delete.append('new_test_tag')
