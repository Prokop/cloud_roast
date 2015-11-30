from cloudroast.images.fixtures import ImagesFixture


class TestGetMetadataDefinitionNamespaceSchema(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetMetadataDefinitionNamespaceSchema, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGetMetadataDefinitionNamespaceSchema, cls).tearDownClass()

    def test_get_metadata_definition_namespace_schema(self):
        response = self.images_client.get_metadata_definition_namespace_schema()
        self.assertEqual(response.status_code, 200)
