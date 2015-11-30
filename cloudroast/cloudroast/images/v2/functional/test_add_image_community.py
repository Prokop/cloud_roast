import ipdb

from cafe.drivers.unittest.decorators import tags
from cloudcafe.images.common.types import \
    ImageMemberStatus, Schemas
from cloudroast.images.fixtures import ImagesFixture


class TestAddImageMember(ImagesFixture):

    @classmethod
    def setUpClass(cls):
        super(TestAddImageMember, cls).setUpClass()
        cls.image = cls.images_client.create_image()

    @classmethod
    def tearDownClass(cls):
        super(TestAddImageMember, cls).tearDownClass()
        response = cls.images_client.delete_image(cls.image.entity.id_)
        assert response.status_code == 204

    @tags(type='smoke')
    def test_add_image_member(self):
        """
        @summary: Add image member

        1) Create image
        2) Add image member
        3) Verify that the response code is 200
        4) Verify that the response contains the correct properties
        list
        5) Verify that user can can see community image in list of images
        """
        response = self.images_client.add_member(self.image.entity.id_, 'community')
        self.assertEqual(response.status_code, 200)
        member = response.entity
        self.assertEqual(member.image_id, self.image.entity.id_)
        self.assertEqual(member.member_id, 'community')
        self.assertEqual(member.schema, Schemas.IMAGE_MEMBER_SCHEMA)
        self.assertEqual(member.status, ImageMemberStatus.PENDING)
        response = self.images_client.list_images()
        self.assertEqual(response.status_code, 200)
        images_list = response.entity
        self.assertIn(self.image.entity, images_list)
        #ipdb.set_trace()
        response = self.admin_images_client.add_member(self.image.entity.id_, self.admin_tenant_id)
        self.assertEqual(response.status_code, 200)
        self.member = response.entity

        response = self.alt_images_client.list_images()
        self.assertEqual(response.status_code, 200)
        images_list = response.entity
        self.assertNotIn(self.image.entity, images_list)


