from cloudcafe.identity.common.client import BaseIdentityAPIClient
from cloudcafe.identity.v3.common.domains.models.responses import Domain

class DomainClient(BaseIdentityAPIClient):

    def create_domain(self, name, requestslib_kwargs=None):
        url = "{url}/domains".format(url=self.url)
        return self.post(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def list_domains(self, requestslib_kwargs=None):
        url = "{url}/domains".format(url=self.url)
        return self.get(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def show_domain_details(self, domain_id, requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}".format(url=self.url,
                                                   domain_id=domain_id)
        return self.get(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def update_domain(self, domain_id, name,
                        requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}".format(url=self.url,
                                          domain_id=domain_id)
        return self.patch(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def delete_domain(self, domain_id, requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}".format(url=self.url,
                                          domain_id=domain_id)
        return self.delete(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def list_roles_for_domain_user(self, domain_id, user_id,
                                   requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/users/{user_id}/roles".format(
            url=self.url, domain_id=domain_id, user_id=user_id)
        return self.get(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def grant_role_to_domain_user(self, domain_id, user_id, role_id,
                                   requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, user_id=user_id, role_id=role_id)
        return self.put(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def check_role_for_domain_user(self, domain_id, user_id, role_id,
                                   requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, user_id=user_id, role_id=role_id)
        return self.head(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def revoke_role_from_domain_user(self, domain_id, user_id, role_id,
                                   requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/users/{user_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, user_id=user_id, role_id=role_id)
        return self.delete(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def list_roles_for_domain_group(self, domain_id, group_id,
                                   requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/groups/{group_id}/roles".format(
            url=self.url, domain_id=domain_id, group_id=group_id)
        return self.get(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def grant_role_to_domain_group(self, domain_id, group_id, role_id,
                                   requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, group_id=group_id,
            role_id=role_id)
        return self.put(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def check_role_for_domain_group(self, domain_id, group_id, role_id,
                                   requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, group_id=group_id,
            role_id=role_id)
        return self.head(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)

    def revoke_role_from_domain_group(self, domain_id, group_id, role_id,
                                   requestslib_kwargs=None):
        url = "{url}/domains/{domain_id}/groups/{group_id}/roles/{role_id}".format(
            url=self.url, domain_id=domain_id, group_id=group_id,
            role_id=role_id)
        return self.delete(url, response_entity_type=Domain,
                        requestslib_kwargs=requestslib_kwargs)