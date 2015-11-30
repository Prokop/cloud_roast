import ipdb

from cafe.drivers.unittest.decorators import tags
from cloudcafe.images.common.types import \
    ImageMemberStatus, Schemas
from cloudroast.images.fixtures import ImagesFixture


class TestBookmarkingCommunityImage(ImagesFixture):

    @classmethod
    def setUpClass(cls):
        super(TestBookmarkingCommunityImage, cls).setUpClass()
        response = cls.admin_images_client.create_image(visibility='community')
        cls.image = response
        assert response.status_code == 201
        assert response.entity.visibility == 'community'

    @classmethod
    def tearDownClass(cls):
        super(TestBookmarkingCommunityImage, cls).tearDownClass()
        response = cls.admin_images_client.delete_image(cls.image.entity.id_)
        assert response.status_code == 204

    @tags(type='smoke')
    def test_bookmark_community_image(self):
        response = self.admin_images_client.list_images(filters={'visibility': 'community'})
        self.assertEqual(response.status_code, 200)
        images_list = response.entity
        self.assertIn(self.image.entity, images_list)
        response = self.admin_images_client.add_member(self.image.entity.id_, self.admin_tenant_id)
        self.assertEqual(response.status_code, 200)
        self.member = response.entity
        self.assertEqual(self.member.image_id, self.image.entity.id_)
        self.assertEqual(self.member.member_id, self.admin_tenant_id)



