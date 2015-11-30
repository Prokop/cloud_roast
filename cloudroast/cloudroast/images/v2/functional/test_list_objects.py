from cloudroast.images.fixtures import ImagesFixture


class TestListObjects(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestListObjects, cls).setUpClass()
        response = cls.images_client.create_namespace(namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        response = cls.images_client.create_object(
            'test_namespace', name='test_object',
            properties={"quota:cpu_period": {"description":
            "A period with value 0 means no value.","maximum": 1000000,
            "minimum": 1000,"title": "Quota: CPU Period","type": "integer"}},
            required=['1'])
        assert response.status_code == 201
        cls.objects_to_delete = []

    @classmethod
    def tearDownClass(cls):
        for obj in cls.objects_to_delete:
            cls.images_client.delete_objects_definition(
            'test_namespace', name=obj)
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestListObjects, cls).tearDownClass()

    def test_list_objects(self):
        response = self.images_client.list_objects(namespace='test_namespace')
        self.assertEqual(response.status_code, 200)
        objs = response.entity[0].name
        self.assertEqual(objs, 'test_object')
        self.objects_to_delete.append('test_object')