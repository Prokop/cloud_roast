import exceptions
from cloudcafe.identity.common.client import BaseIdentityAPIClient
from cloudcafe.identity.v3.common.roles.models.responses import Role, Roles


class RolesClient(BaseIdentityAPIClient):
    def list_roles_for_domain_user(self, domain_id,
                                   user_id, requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/users/{user_id}/roles".format(
            url=self.url, domain_id=domain_id, user_id=user_id)
        return self.get(url, response_entity_type=Roles,
                        requestslib_kwargs=requestslib_kwargs)

    def grant_role_to_domain_user(self, domain_id,
                                  user_id, role_id, requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, user_id=user_id, role_id=role_id)
        return self.put(url, requestslib_kwargs=requestslib_kwargs)

    def check_role_for_domain_user(self, domain_id,
                                   user_id, role_id, requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, user_id=user_id, role_id=role_id)
        return self.head(url, requestslib_kwargs=requestslib_kwargs)

    def revoke_role_from_domain_user(self, domain_id,
                                     user_id, role_id, requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, user_id=user_id, role_id=role_id)
        return self.delete(url, requestslib_kwargs=requestslib_kwargs)

    def list_roles_for_domain_group(self, domain_id,
                                    group_id, requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/groups/{group_id}/roles".format(
            url=self.url, domain_id=domain_id, group_id=group_id)
        return self.get(url, response_entity_type=Roles,
                        requestslib_kwargs=requestslib_kwargs)

    def grant_role_to_domain_group(self, domain_id,
                                   group_id, role_id, requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, group_id=group_id, role_id=role_id)
        return self.put(url, requestslib_kwargs=requestslib_kwargs)

    def check_role_for_domain_group(self, domain_id,
                                    group_id, role_id, requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, group_id=group_id, role_id=role_id)
        return self.head(url, requestslib_kwargs=requestslib_kwargs)

    def revoke_role_from_domain_group(self, domain_id,
                                      group_id, role_id, requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, group_id=group_id, role_id=role_id)
        return self.delete(url, requestslib_kwargs=requestslib_kwargs)

    def list_roles_for_project_user(self, project_id, user_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/users/{user_id}/roles".format(
            url=self.url, project_id=project_id, user_id=user_id)
        return self.get(url, response_entity_type=Roles,
                        requestslib_kwargs=requestslib_kwargs)

    def grant_role_to_project_user(self, project_id, user_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, user_id=user_id,
            role_id=role_id)
        return self.put(url, requestslib_kwargs=requestslib_kwargs)

    def check_role_for_project_user(self, project_id, user_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, user_id=user_id,
            role_id=role_id)
        return self.head(url, requestslib_kwargs=requestslib_kwargs)

    def revoke_role_from_project_user(self, project_id, user_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, user_id=user_id,
            role_id=role_id)
        return self.delete(url, requestslib_kwargs=requestslib_kwargs)

    def list_roles_for_project_group(self, project_id, group_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/groups/{group_id}/roles".format(
            url=self.url, project_id=project_id, group_id=group_id)
        return self.get(url, response_entity_type=Roles,
                        requestslib_kwargs=requestslib_kwargs)

    def grant_role_to_project_group(self, project_id, group_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, group_id=group_id,
            role_id=role_id)
        return self.put(url, requestslib_kwargs=requestslib_kwargs)

    def check_role_for_project_group(self, project_id, group_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, group_id=group_id,
            role_id=role_id)
        return self.head(url, requestslib_kwargs=requestslib_kwargs)

    def revoke_role_from_project_group(self, project_id, group_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, group_id=group_id,
            role_id=role_id)
        return self.delete(url, requestslib_kwargs=requestslib_kwargs)