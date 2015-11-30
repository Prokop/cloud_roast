from cafe.drivers.unittest.datasets import DatasetList
from cafe.drivers.unittest.decorators import DataDrivenClass
from cloudcafe.identity.config import DefaultUser
from cloudroast.identity.v3.fixture import IdentityV3Fixture
from cloudroast.metrics import MetricGenerator


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
class TestCheckRoleForDomainUser(IdentityV3Fixture):
    """Test Class for check token test case."""

    def setUp(self):
        super(TestCheckRoleForDomainUser, self).setUp()
        self.mgen = MetricGenerator.GetMetricGenerator()
        composite = self.project_composite
        response = composite.apis.roles.client.grant_role_to_domain_user(
            domain_id=composite.user_config.scope_domain_id,
            user_id=composite.ident_config.user_for_test_roles,
            role_id=composite.ident_config.role_for_grant_id)
        assert response.status_code == 204

    def tearDown(self):
        composite = self.project_composite
        response = composite.apis.roles.client.revoke_role_from_domain_user(
            domain_id=composite.user_config.scope_domain_id,
            user_id=composite.ident_config.user_for_test_roles,
            role_id=composite.ident_config.role_for_grant_id)
        assert response.status_code == 204
        super(TestCheckRoleForDomainUser, self).tearDown()

    def test_check_role_for_domain_user_using_domain_scoped_token(self):
        with self.mgen.create_metric("identity.check_role_for_domain_user_using_domain_scoped_token"):
            composite = self.domain_composite
            response = composite.apis.roles.client.check_role_for_domain_user(
                domain_id=composite.user_config.scope_domain_id,
                user_id=composite.ident_config.user_for_test_roles,
                role_id=composite.ident_config.role_for_grant_id)
            self.assertEqual(204, response.status_code)

    def test_check_role_for_domain_user_using_project_scoped_token(self):
        """ Expected to return 403 using project scoped token """
        with self.mgen.create_metric("identity.check_role_for_domain_user_using_project_scoped_token"):
            composite = self.project_composite
            response = composite.apis.roles.client.check_role_for_domain_user(
                domain_id=composite.user_config.scope_domain_id,
                user_id=composite.ident_config.user_for_test_roles,
                role_id=composite.ident_config.role_for_grant_id)
            self.assertEqual(403, response.status_code)
