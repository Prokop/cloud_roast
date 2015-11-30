from cafe.drivers.unittest.datasets import DatasetList
from cafe.drivers.unittest.decorators import DataDrivenClass
from cloudcafe.identity.config import DefaultUser
from cloudroast.identity.v3.fixture import IdentityV3Fixture


class ValidateDataset(DatasetList):
    def __init__(self):
        test_cases = [
            # {"name": "ServiceAdmin", "data": {
            #     "get_service_catalog_resp": 200,
            #     "user_config": ServiceAdmin}},
            # {"name": "IdentityAdmin", "data": {
            #     "get_service_catalog_resp": 200,
            #     "user_config": IdentityAdmin}},
            # {"name": "UserAdmin", "data": {
            #     "get_service_catalog_resp": 200,
            #     "user_config": UserAdmin}},
            # {"name": "UserManage", "data": {
            #     "get_service_catalog_resp": 200,
            #     "user_config": UserManage}},
            {"name": "DefaultUser", "data": {
                "user_config": DefaultUser}}]
        for test_case in test_cases:
            self.append_new_dataset(test_case["name"], test_case["data"])


@DataDrivenClass(ValidateDataset())
class TestListRolesForProjectGroup(IdentityV3Fixture):
    """Test Class for check token test case."""

    def setUp(self):
        super(TestListRolesForProjectGroup, self).setUp()
        composite = self.project_composite
        response = composite.apis.roles.client.grant_role_to_project_group(
            project_id=composite.user_config.project_id,
            group_id=composite.ident_config.group_for_test_roles,
            role_id=composite.ident_config.role_for_grant_id)
        assert response.status_code == 204

    def tearDown(self):
        composite = self.project_composite
        response = composite.apis.roles.client.revoke_role_from_project_group(
            project_id=composite.user_config.project_id,
            group_id=composite.ident_config.group_for_test_roles,
            role_id=composite.ident_config.role_for_grant_id)
        assert response.status_code == 204
        super(TestListRolesForProjectGroup, self).tearDown()

    def test_list_roles_for_domain_group_using_domain_scoped_token(self):
        composite = self.domain_composite
        response = composite.apis.roles.client.list_roles_for_project_group(
            project_id=composite.user_config.project_id,
            group_id=composite.ident_config.group_for_test_roles)
        self.assertEqual(200, response.status_code)
        role_names = [r.name for r in response.entity]
        self.assertIn('test', role_names)
        role_ids = [r.id_ for r in response.entity]
        self.assertIn(composite.ident_config.role_for_grant_id, role_ids)

    def test_list_roles_for_domain_group_using_project_scoped_token(self):
        composite = self.project_composite
        response = composite.apis.roles.client.list_roles_for_project_group(
            project_id=composite.user_config.project_id,
            group_id=composite.ident_config.group_for_test_roles)
        self.assertEqual(200, response.status_code)
        role_names = [r.name for r in response.entity]
        self.assertIn('test', role_names)
        role_ids = [r.id_ for r in response.entity]
        self.assertIn(composite.ident_config.role_for_grant_id, role_ids)


