from cloudcafe.identity.common.models.base import (
    BaseIdentityModel)
from cloudcafe.identity.v3.common.domains.models.responses import Domain


class Policy(BaseIdentityModel):
    """
    Response model for User
    """

    NS_PREFIX = 'RAX-AUTH'

    def __init__(
            self, id_=None, name=None, domain=None,
            default_region=None, default_project_id=None):
        super(Policy, self).__init__(locals())

    @classmethod
    def _dict_to_obj(cls, data):
        """
        @summary: Converting Dictionary Representation of a User object
            to a User object
        @return: User object
        @param data: Dictionary Representation of a User object
        """
        if data is None:
            return None
        data = cls._remove_extension_prefix(
            prefix=cls.NS_PREFIX, data_dict=data)
        if 'domain' in data:
            data['domain'] = Domain._dict_to_obj(data.get("domain"))

        return cls(
            id_=data.get("id"),
            name=data.get("name"),
            default_project_id=data.get("default_project_id"),
            default_region=data.get("default_region"),
            domain=data.get("domain"))