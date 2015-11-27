import ipdb

from cafe.drivers.unittest.decorators import tags
from cloudcafe.images.common.types import \
    ImageMemberStatus, Schemas
from cloudroast.images.fixtures import ImagesFixture


class TestUnbookmarkingCommunityImage(ImagesFixture):

    @classmethod
    def setUpClass(cls):
        super(TestUnbookmarkingCommunityImage, cls).setUpClass()
        response = cls.admin_images_client.create_image(visibility='community')
        cls.image = response
        assert response.status_code == 201
        assert response.entity.visibility == 'community'
        response = cls.admin_images_client.list_images(filters={'visibility': 'community'})
        assert response.status_code == 200
        images_list = response.entity
        assert cls.image.entity in images_list
        response = cls.admin_images_client.add_member(cls.image.entity.id_, cls.admin_tenant_id)
        assert response.status_code == 200
        cls.member = response.entity
        assert cls.member.image_id == cls.image.entity.id_
        assert cls.member.member_id == cls.admin_tenant_id

    @classmethod
    def tearDownClass(cls):
        super(TestUnbookmarkingCommunityImage, cls).tearDownClass()
        response = cls.admin_images_client.delete_image(cls.image.entity.id_)
        assert response.status_code == 204

    @tags(type='smoke')
    def test_unbookmarking_community_image(self):
        response = self.admin_images_client.delete_member(self.image.entity.id_, self.member.member_id)
        self.assertEqual(response.status_code, 204)
        response = self.admin_images_client.list_members(self.image.entity.id_)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(self.member.member_id, response.entity)
