from cafe.drivers.unittest.decorators import tags
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
class TestListUsers(IdentityV3Fixture):

    @tags('periodic')
    def test_list_users_using_domain_scoped_token(self):
        composite = self.domain_composite
        response = composite.apis.users.client.list_users()
        self.assertEqual(200, response.status_code)
        users = response.entity
        self.assertGreater(len(users), 0)
        user_names = [u.name for u in users]
        self.assertIn(composite.user_config.username, user_names)

    def test_list_users_using_project_scoped_token(self):
        composite = self.project_composite
        response = composite.apis.users.client.list_users()
        self.assertEqual(200, response.status_code)
        users = response.entity
        self.assertGreater(len(users), 0)
        user_names = [u.name for u in users]
        self.assertIn(composite.user_config.username, user_names)
