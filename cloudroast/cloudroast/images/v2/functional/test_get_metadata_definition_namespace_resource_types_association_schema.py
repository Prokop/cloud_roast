from cloudroast.images.fixtures import ImagesFixture


class TestGetMetadataNamespaceResourceTypesAssociationSchema(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestGetMetadataNamespaceResourceTypesAssociationSchema, cls).\
            setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGetMetadataNamespaceResourceTypesAssociationSchema, cls).\
            tearDownClass()

    def test_get_metadata_namespace_definition_resource_types_association_schema(
            self):
        response = self.images_client.\
            get_metadata_namespace_definition_resource_types_association_schema()
        self.assertEqual(response.status_code, 200)
