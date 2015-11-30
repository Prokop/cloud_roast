from cloudroast.images.fixtures import ImagesFixture


class TestGetMetadataTagsSchema(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetMetadataTagsSchema, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGetMetadataTagsSchema, cls).tearDownClass()

    def test_get_metadata_definition_tags_schema(self):
        response = self.images_client.get_metadata_definition_tags_schema()
        self.assertEqual(response.status_code, 200)
