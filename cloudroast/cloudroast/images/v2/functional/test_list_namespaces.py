from cloudroast.images.fixtures import ImagesFixture


class TestListNamespaces(ImagesFixture):
    def test_list_namespaces(self):
        response = self.images_client.list_namespaces()
        self.assertEqual(response.status_code, 200)
