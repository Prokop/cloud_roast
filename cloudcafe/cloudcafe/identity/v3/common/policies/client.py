from cloudcafe.identity.common.client import BaseIdentityAPIClient
from cloudcafe.identity.v3.common.policies.models import responses


class PoliciesClient(BaseIdentityAPIClient):

    def create_policy(self, blob, project_id, type, user_id,
                      requestslib_kwargs=None):
        url = "{0}/policies".format(self.url)
        return self.post(url, response_entity_type=responses.Policy,
            requestslib_kwargs=requestslib_kwargs)

    def list_policies(self, requestslib_kwargs=None):
        url = "{0}/policies".format(self.url)
        return self.get(url, response_entity_type=responses.Policy,
            requestslib_kwargs=requestslib_kwargs)

    def show_policy_details(self, policy_id, requestslib_kwargs=None):
        url = "{0}/policies/{policy_id}".format(self.url,
                                                policy_id=policy_id)
        return self.get(url, response_entity_type=responses.Policy,
            requestslib_kwargs=requestslib_kwargs)

    def update_policy(self, policy_id, requestslib_kwargs=None):
        url = "{0}/policies/{policy_id}".format(self.url,
                                                policy_id=policy_id)
        return self.patch(url, response_entity_type=responses.Policy,
            requestslib_kwargs=requestslib_kwargs)

    def delete_policy(self, policy_id, requestslib_kwargs=None):
        url = "{0}/policies/{policy_id}".format(self.url,
                                                policy_id=policy_id)
        return self.delete(url, response_entity_type=responses.Policy,
            requestslib_kwargs=requestslib_kwargs)
