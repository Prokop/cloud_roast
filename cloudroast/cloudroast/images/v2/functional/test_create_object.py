from cloudroast.images.fixtures import ImagesFixture


class TestCreateObject(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestCreateObject, cls).setUpClass()
        response = cls.images_client.create_namespace(namespace='test_namespace')
        assert response.status_code == 201
        cls.namespaces_to_delete = [response.entity.namespace]
        cls.objects_to_delete = []

    @classmethod
    def tearDownClass(cls):
        for obj in cls.objects_to_delete:
            cls.images_client.delete_objects_definition(
            'test_namespace', name=obj)
        for namespace in cls.namespaces_to_delete:
            cls.images_client.delete_namespace(namespace)
        super(TestCreateObject, cls).tearDownClass()

    def test_create_objects(self):
        #import ipdb; ipdb.set_trace()
        response = self.images_client.create_object(
            'test_namespace', name='test_object',
            properties={"quota:cpu_period": {"description":
            "A period with value 0 means no value.","maximum": 1000000,
            "minimum": 1000,"title": "Quota: CPU Period","type": "integer"}},
            required=['1'])
        self.assertEqual(response.status_code, 201)
        obj = response.entity
        self.assertEqual(obj.name, 'test_object')
        self.objects_to_delete.append('test_object')



