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
class TestListProjectsForUser(IdentityV3Fixture):

    def test_list_projects_for_user_using_domain_scoped_token(self):
        composite = self.domain_composite
        response = composite.apis.users.client.list_projects_for_user(
            user_id=composite.user_config.user_id)
        self.assertEqual(200, response.status_code)
        list_of_groups = response.entity
        self.assertIsNotNone(list_of_groups)

    def test_list_projects_for_user_using_project_scoped_token(self):
        composite = self.project_composite
        response = composite.apis.users.client.list_projects_for_user(
            user_id=composite.user_config.user_id)
        self.assertEqual(200, response.status_code)
        list_of_groups = response.entity
        self.assertIsNotNone(list_of_groups)

