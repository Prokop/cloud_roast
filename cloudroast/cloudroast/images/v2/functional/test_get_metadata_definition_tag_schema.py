from cloudroast.images.fixtures import ImagesFixture


class TestGetMetadataTagSchema(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetMetadataTagSchema, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGetMetadataTagSchema, cls).tearDownClass()

    def test_get_metadata_definition_tag_schema(self):
        response = self.images_client.get_metadata_definition_tag_schema()
        self.assertEqual(response.status_code, 200)
