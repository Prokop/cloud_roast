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
                "not_found_exp_resp": 404,
                "invalid_token_exp_resp": 401,
                "user_config": DefaultUser}}]
        for test_case in test_cases:
            self.append_new_dataset(test_case["name"], test_case["data"])


@DataDrivenClass(ValidateDataset())
class TestValidateToken(IdentityV3Fixture):
    """Test Class for validate token test case."""
    @tags('periodic')
    def test_validate_token(self):
        for composite in (self.project_composite, self.domain_composite):
            response = composite.apis.tokens.client.authenticate(
                user_id=composite.user_config.user_id,
                username=composite.user_config.username,
                password=composite.user_config.password,
                user_domain_name=composite.user_config.user_domain_name)
            x_subj_token = response.headers.get('x-subject-token')
            response = composite.apis.tokens.client.validate_token(x_subj_token)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.entity.user.name, composite.user_config.username)
            self.assertEqual(response.entity.user.id_, composite.user_config.user_id)
            self.assertEqual(response.entity.user.domain.name,
                             composite.user_config.user_domain_name)
            self.assertEqual(response.entity.user.domain.id_,
                             composite.user_config.user_domain_id)
