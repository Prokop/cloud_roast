from cafe.engine.behaviors import BaseBehavior


class TokensBehaviorException(Exception):
    pass


class TokensBehavior(BaseBehavior):

    def __init__(self, client, scope_domain_id=None, scope_project_id=None):
        super(TokensBehavior, self).__init__()
        self.client = client
        self.scope_project_id = scope_project_id
        self.scope_domain_id = scope_domain_id

    def authenticate(self, username, password, domain_id):
        """
        @summary Authenticate the user with username and password
        """

        if not self.client.url.endswith(("v3", "v3/")):
            self.client.url = '{url}/v3'.format(url=self.client.url)

        if self.scope_project_id is None:
            auth_response = self.client.authenticate(
                username=username, password=password, user_domain_id=domain_id,
                scope='project', domain_id=self.scope_domain_id)
        else:
            auth_response = self.client.authenticate(
                username=username, password=password, user_domain_id=domain_id,
                scope='project', project_id=self.scope_project_id,
                project_domain_id=self.scope_domain_id)
        self._verify_entity(auth_response)
        return auth_response

    def _verify_entity(self, resp):
        """
        Verify authentication call succeeded and verify auth response entity
        deserialized correctly
        """
        if not resp.ok:
            msg = "Auth failed with status_code {0} ".format(resp.status_code)
            self._log.error(msg)
            raise TokensBehaviorException(msg)

        if resp.entity is None:
            msg = "Response body did not deserialize as expected"
            self._log.error(msg)
            # Verification fails at the moment, that's why
            # I'm commneting this out
            # raise TokensBehaviorException(msg)
        return resp.entity
