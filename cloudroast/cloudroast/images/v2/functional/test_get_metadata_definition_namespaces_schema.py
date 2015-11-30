from cloudroast.images.fixtures import ImagesFixture


class TestGetMetadataDefinitionNamespacesSchema(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetMetadataDefinitionNamespacesSchema, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGetMetadataDefinitionNamespacesSchema, cls).tearDownClass()

    def test_get_metadata_definition_namespaces_schema(self):
        response = self.images_client.get_metadata_definition_namespaces_schema()
        self.assertEqual(response.status_code, 200)
