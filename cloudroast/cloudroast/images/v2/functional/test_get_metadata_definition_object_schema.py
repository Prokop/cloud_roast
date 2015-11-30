from cloudroast.images.fixtures import ImagesFixture


class TestGetMetadataDefinitionObjectSchema(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetMetadataDefinitionObjectSchema, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGetMetadataDefinitionObjectSchema, cls).tearDownClass()

    def test_get_metadata_definition_object_schema(self):
        response = self.images_client.get_metadata_definition_object_schema()
        self.assertEqual(response.status_code, 200)
