import ipdb

from cafe.drivers.unittest.decorators import tags
from cloudcafe.images.common.types import \
    ImageMemberStatus, Schemas
from cloudroast.images.fixtures import ImagesFixture


class TestCommunityImageDiscovery(ImagesFixture):

    @classmethod
    def setUpClass(cls):
        super(TestCommunityImageDiscovery, cls).setUpClass()
        response = cls.admin_images_client.create_image(visibility='private')
        cls.image = response
        assert response.status_code == 201
        assert response.entity.visibility == 'private'
        response = cls.admin_images_client.add_member(cls.image.entity.id_, 'community')
        assert response.status_code == 200
        cls.member = response.entity
        assert cls.member.image_id == cls.image.entity.id_
        assert cls.member.member_id == 'community'
        assert cls.member.schema == Schemas.IMAGE_MEMBER_SCHEMA
        assert cls.member.status == ImageMemberStatus.PENDING

    @classmethod
    def tearDownClass(cls):
        super(TestCommunityImageDiscovery, cls).tearDownClass()
        response = cls.admin_images_client.delete_image(cls.image.entity.id_)
        assert response.status_code == 204

    @tags(type='smoke')
    def test_community_image_discovery(self):
        response = self.alt_images_client.list_images(filters={'visibility': 'shared'})
        self.assertEqual(response.status_code, 200)
        images_list = response.entity
        self.assertIn(self.image.entity, images_list)
