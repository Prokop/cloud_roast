from cafe.drivers.unittest.decorators import DataDrivenClass
from cafe.drivers.unittest.datasets import DatasetList
from cloudcafe.identity.config import (DefaultUser)
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
                "not_found_exp_resp": 404,
                "invalid_token_exp_resp": 401,
                "user_config": DefaultUser}}]
        for test_case in test_cases:
            self.append_new_dataset(test_case["name"], test_case["data"])


@DataDrivenClass(ValidateDataset())
class TestAuthenticate(IdentityV3Fixture):

    def test_auth_domain_scope(self):
       response = self.domain_composite.apis.tokens.client.authenticate(
           user_id=self.domain_composite.user_config.user_id,
           username=self.domain_composite.user_config.username,
           password=self.domain_composite.user_config.password,
           user_domain_name=self.domain_composite.user_config.user_domain_name)
       code = response.status_code
       self.assertEqual(code, 201)

    def test_auth_project_scope(self):
       response = self.project_composite.apis.tokens.client.authenticate(
           user_id=self.project_composite.user_config.user_id,
           username=self.project_composite.user_config.username,
           password=self.project_composite.user_config.password,
           user_domain_name=self.project_composite.user_config.user_domain_name)
       code = response.status_code
       self.assertEqual(code, 201)

