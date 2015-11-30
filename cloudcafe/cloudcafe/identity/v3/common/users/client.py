from cloudcafe.identity.common.client import BaseIdentityAPIClient
from cloudcafe.identity.v3.common.users.models import\
    responses as users_responses
from cloudcafe.identity.v3.common.groups.models import\
    responses as groups_responses
from cloudcafe.identity.v3.common.projects.models import\
    responses as projects_responses


class UsersClient(BaseIdentityAPIClient):

    def list_users(self, requestslib_kwargs=None):
        """
        @summary: Fetching the users
        @return: User information
        @rtype: User List
        """
        url = "{0}/users".format(self.url)
        return self.get(
            url, response_entity_type=users_responses.Users,
            requestslib_kwargs=requestslib_kwargs)

    def list_groups_for_user(self, user_id, requestslib_kwargs=None):
        url = "{0}/users/{user_id}/groups".format(self.url, user_id=user_id)
        return self.get(url, response_entity_type=groups_responses.Groups,
            requestslib_kwargs=requestslib_kwargs)

    def list_projects_for_user(self, user_id, requestslib_kwargs=None):
        url = "{0}/users/{user_id}/projects".format(self.url, user_id=user_id)
        return self.get(url, response_entity_type=projects_responses.Projects,
            requestslib_kwargs=requestslib_kwargs)
