from cloudroast.images.fixtures import ImagesFixture


class TestGetMetadataDefinitionObjectsSchema(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetMetadataDefinitionObjectsSchema, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGetMetadataDefinitionObjectsSchema, cls).tearDownClass()

    def test_get_metadata_definition_objects_schema(self):
        response = self.images_client.get_metadata_definition_objects_schema()
        self.assertEqual(response.status_code, 200)
