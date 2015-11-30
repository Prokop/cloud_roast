from cloudroast.images.fixtures import ImagesFixture


class TestGetMetadataPropertySchema(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetMetadataPropertySchema, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGetMetadataPropertySchema, cls).tearDownClass()

    def test_get_metadata_definition_property_schema(self):
        response = self.images_client.get_metadata_definition_property_schema()
        self.assertEqual(response.status_code, 200)
