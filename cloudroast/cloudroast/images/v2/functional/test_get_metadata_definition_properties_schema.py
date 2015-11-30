from cloudroast.images.fixtures import ImagesFixture


class TestGetMetadataPropertiesSchema(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetMetadataPropertiesSchema, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGetMetadataPropertiesSchema, cls).tearDownClass()

    def test_get_metadata_definition_properties_schema(self):
        response = self.images_client.get_metadata_definition_properties_schema()
        self.assertEqual(response.status_code, 200)
