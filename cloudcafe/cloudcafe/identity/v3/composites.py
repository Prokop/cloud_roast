from cloudcafe.identity.v3.common.tokens.behavior import TokensBehavior
from cloudcafe.identity.v3.common.tokens.client import TokensClient
from cloudcafe.identity.composites import IdentityBaseComposite
from cloudcafe.identity.v3.config import IdentityV3Config


class DomainIdentityV3Composite(IdentityBaseComposite):
    _ident_config_class = IdentityV3Config

    def __init__(self, user_config=None):
        super(DomainIdentityV3Composite, self).__init__(user_config=user_config)
        self.version = 'v3'
        self.tokens_client = TokensClient(
            url=self.url,
            serialize_format=self.ident_config.serialize_format,
            deserialize_format=self.ident_config.deserialize_format,
            auth_token=None)
        self.tokens_behavior = TokensBehavior(
            self.tokens_client, self.user_config.scope_domain_id)
        self.load_clients_and_behaviors()

    def fetch_token(self):
        """
        Authenticate and retrieve the resp and the token in the header
        """
        resp = self.tokens_behavior.authenticate(
            username=self.user_config.username,
            password=self.user_config.password,
            domain_id=self.user_config.domain_id)
        self.access_data = resp.entity
        self.token = resp.headers['x-subject-token']
        return resp


class ProjectIdentityV3Composite(IdentityBaseComposite):
    _ident_config_class = IdentityV3Config

    def __init__(self, user_config=None):
        super(ProjectIdentityV3Composite, self).__init__(user_config=user_config)
        self.version = 'v3'
        self.tokens_client = TokensClient(
            url=self.url,
            serialize_format=self.ident_config.serialize_format,
            deserialize_format=self.ident_config.deserialize_format,
            auth_token=None)
        self.tokens_behavior = TokensBehavior(
            self.tokens_client, self.user_config.scope_domain_id,
            self.user_config.scope_project_id)
        self.load_clients_and_behaviors()

    def fetch_token(self):
        """
        Authenticate and retrieve the resp and the token in the header
        """
        resp = self.tokens_behavior.authenticate(
            username=self.user_config.username,
            password=self.user_config.password,
            domain_id=self.user_config.domain_id)
        self.access_data = resp.entity
        self.token = resp.headers['x-subject-token']
        return resp