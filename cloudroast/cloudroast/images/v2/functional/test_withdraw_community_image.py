import ipdb

from cafe.drivers.unittest.decorators import tags
from cloudcafe.images.common.types import \
    ImageMemberStatus, Schemas
from cloudroast.images.fixtures import ImagesFixture


class TestWithdrawCommunityImage(ImagesFixture):

    @classmethod
    def setUpClass(cls):
        super(TestWithdrawCommunityImage, cls).setUpClass()
        response = cls.admin_images_client.create_image()
        cls.image = response
        assert response.status_code == 201
        cls.image_id = response.entity.id_
        response = cls.admin_images_client.add_member(cls.image.entity.id_, 'community')
        assert response.status_code == 200
        cls.member = response.entity
        assert cls.member.image_id == cls.image.entity.id_
        assert cls.member.member_id == 'community'
        assert cls.member.schema == Schemas.IMAGE_MEMBER_SCHEMA
        assert cls.member.status == ImageMemberStatus.PENDING

    @classmethod
    def tearDownClass(cls):
        super(TestWithdrawCommunityImage, cls).tearDownClass()
        response = cls.admin_images_client.delete_image(cls.image.entity.id_)
        assert response.status_code == 204

    @tags(type='smoke')
    def test_withdraw_community_image(self):
        """
        @summary: Withdraw a community image
        """
        response = self.admin_images_client.update_image(self.image_id, replace={'visibility': 'private'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.entity.visibility, 'private')
        response = self.admin_images_client.delete_member(self.image.entity.id_, self.member.member_id)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.entity.visibility, 'private')

