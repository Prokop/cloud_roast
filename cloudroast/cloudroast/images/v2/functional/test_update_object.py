from cloudroast.images.fixtures import ImagesFixture


class TestUpdateObject(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestUpdateObject, cls).setUpClass()
        response = cls.images_client.create_namespace(
            namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        response = cls.images_client.create_object(
            'test_namespace', name='test_object',
            properties={"quota:cpu_period": {"description":
            "A period with value 0 means no value.","maximum": 1000000,
            "minimum": 1000,"title": "Quota: CPU Period","type": "integer"}},
            required=['test required'])
        assert response.status_code == 201
        cls.objects_to_delete = []

    @classmethod
    def tearDownClass(cls):
        for obj in cls.objects_to_delete:
            cls.images_client.delete_objects_definition(
            'test_namespace', name=obj)
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestUpdateObject, cls).tearDownClass()

    def test_update_object(self):
        response = self.images_client.get_object_definition(
        'test_namespace', 'test_object')
        self.assertEqual(response.status_code, 200)
        objs = response.entity.name
        self.assertEqual(objs, 'test_object')
        objs_required = response.entity.required[0]
        self.assertEqual(objs_required, 'test required')
        response = self.images_client.update_object_definition(
            'test_namespace',  name='test_object',
            required=['new test required'])
        response = self.images_client.get_object_definition(
        'test_namespace', 'test_object')
        self.assertEqual(response.status_code, 200)
        objs = response.entity.name
        self.assertEqual(objs, 'test_object')
        objs_required = response.entity.required[0]
        self.assertEqual(objs_required, 'new test required')
        self.objects_to_delete.append('test_object')