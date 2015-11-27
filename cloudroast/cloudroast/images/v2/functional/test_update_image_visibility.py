from cloudroast.images.fixtures import ImagesFixture


class TestUpdateImageVisibility(ImagesFixture):
    @classmethod
    def setUpClass(cls):
        super(TestUpdateImageVisibility, cls).setUpClass()
        response = cls.images_client.create_image(visibility='private')
        assert response.status_code == 201
        cls.image_id = response.entity.id_
        assert response.entity.visibility == 'private'

    @classmethod
    def tearDownClass(cls):
        super(TestUpdateImageVisibility, cls).tearDownClass()
        response = cls.images_client.delete_image(cls.image_id)
        assert response.status_code == 204

    def test_make_image_public(self):
        """This test makes image public and need account admin role"""
        response = self.admin_images_client.update_image(self.image_id, replace={'visibility': 'public'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.entity.visibility, 'public')

    def test_make_image_private(self):
        """This test makes image private and need account admin role"""
        response = self.images_client.update_image(self.image_id, replace={'visibility': 'private'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.entity.visibility, 'private')
