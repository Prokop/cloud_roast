import ipdb

from cloudroast.images.fixtures import ImagesFixture
from cloudcafe.images.common.types import \
    ImageMemberStatus, Schemas


class TestPublicImageDowngrade(ImagesFixture):

    @classmethod
    def setUpClass(cls):
        super(TestPublicImageDowngrade, cls).setUpClass()
        response = cls.admin_images_client.create_image(visibility='public')
        cls.image = response
        assert response.status_code == 201
        cls.image_id = response.entity.id_
        assert response.entity.visibility == 'public'
        response = cls.alt_images_client.list_images()
        assert response.status_code == 200
        images_list = response.entity
        assert cls.image.entity in images_list

    @classmethod
    def tearDownClass(cls):
        super(TestPublicImageDowngrade, cls).tearDownClass()
        response = cls.admin_images_client.delete_image(cls.image_id)
        assert response.status_code == 204

    def test_public_image_downgrade(self):
        """
        @summary: create a non-discoverable community image
        """
        response = self.admin_images_client.add_member(self.image.entity.id_, 'community')
        self.assertEqual(response.status_code, 200)
        member = response.entity
        self.assertEqual(member.image_id, self.image.entity.id_)
        self.assertEqual(member.member_id, 'community')
        self.assertEqual(member.schema, Schemas.IMAGE_MEMBER_SCHEMA)
        self.assertEqual(member.status, ImageMemberStatus.PENDING)
        response = self.admin_images_client.list_images()
        self.assertEqual(response.status_code, 200)
        images_list = response.entity
        self.assertIn(self.image.entity, images_list)
        response = self.alt_images_client.list_images()
        self.assertEqual(response.status_code, 200)
        images_list = response.entity
        self.assertNotIn(self.image.entity, images_list)

