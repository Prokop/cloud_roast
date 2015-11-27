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
class TestListRolesForDomainUser(IdentityV3Fixture):
    """Test Class for check token test case."""

    def test_list_roles_for_domain_user(self):
        for composite in (self.project_composite, self.domain_composite):
            response = composite.apis.roles.client.grant_role_to_domain_user(
                domain_id=composite.user_config.scope_domain_id,
                user_id=composite.user_config.user_id,
                role_id=composite.ident_config.role_for_grant_id)
            self.assertEqual(204, response.status_code)
            """
            As per the documentation http://developer.openstack.org/api-ref-identity-v3.html
            /v3/domains/{domain_id}/users/{user_id}/roles/{role_id}
            This operation does not accept a request body and does not return a response body
            So the following check is invalid. Disabling it
            """
            """			
            role_names = [r.name for r in response.entity]
            self.assertIn('admin', role_names)
            """
