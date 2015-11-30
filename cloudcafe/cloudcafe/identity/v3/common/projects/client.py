from cloudcafe.identity.common.client import BaseIdentityAPIClient
from cloudcafe.identity.v3.common.projects.models.responses import Project

class ProjectClient(BaseIdentityAPIClient):

    def list_roles_for_project_user(self, project_id, user_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/users/{user_id}/roles".format(
            url=self.url, project_id=project_id, user_id=user_id)
        return self.get(url, response_entity_type=Projects,
                        requestslib_kwargs=requestslib_kwargs)

    def grant_role_to_project_user(self, project_id, user_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, user_id=user_id,
            role_id=role_id)
        return self.put(url, response_entity_type=Project,
                        requestslib_kwargs=requestslib_kwargs)

    def check_role_for_project_user(self, project_id, user_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, user_id=user_id,
            role_id=role_id)
        return self.head(url, response_entity_type=Project,
                        requestslib_kwargs=requestslib_kwargs)

    def revoke_role_for_project_user(self, project_id, user_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, user_id=user_id,
            role_id=role_id)
        return self.delete(url, response_entity_type=Project,
                        requestslib_kwargs=requestslib_kwargs)

    def list_roles_for_project_group(self, project_id, group_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/groups/{group_id}/roles".format(
            url=self.url, project_id=project_id, group_id=group_id)
        return self.get(url, response_entity_type=Project,
                        requestslib_kwargs=requestslib_kwargs)

    def grant_role_to_project_group(self, project_id, group_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, group_id=group_id,
            role_id=role_id)
        return self.put(url, response_entity_type=Project,
                        requestslib_kwargs=requestslib_kwargs)

    def check_role_for_project_group(self, project_id, group_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, group_id=group_id,
            role_id=role_id)
        return self.head(url, response_entity_type=Project,
                        requestslib_kwargs=requestslib_kwargs)

    def revoke_role_to_project_group(self, project_id, group_id, role_id,
                                    requestslib_kwargs=None):
        url = "{url}/projects/{project_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, project_id=project_id, group_id=group_id,
            role_id=role_id)
        return self.delete(url, response_entity_type=Project,
                        requestslib_kwargs=requestslib_kwargs)
