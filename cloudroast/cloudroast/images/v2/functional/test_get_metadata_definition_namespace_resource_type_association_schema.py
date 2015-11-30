from cloudroast.images.fixtures import ImagesFixture


class TestGetMetadataNamespaceResourceTypeAssociationSchema(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetMetadataNamespaceResourceTypeAssociationSchema, cls).\
            setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGetMetadataNamespaceResourceTypeAssociationSchema, cls).\
            tearDownClass()

    def test_get_metadata_namespace_definition_resource_type_association_schema(
            self):
        response = self.images_client.\
            get_metadata_namespace_definition_resource_type_association_schema()
        self.assertEqual(response.status_code, 200)
