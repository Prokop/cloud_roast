from cloudroast.images.fixtures import ImagesFixture


class TestListResourceTypes(ImagesFixture):
    def test_list_resource_types(self):
        response = self.images_client.list_resource_types()
        self.assertEqual(response.status_code, 200)
