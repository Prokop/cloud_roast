from cloudcafe.identity.common.models.base import (
    BaseIdentityModel, BaseIdentityListModel)

class Group(BaseIdentityModel):
    def __init__(
            self, id_=None, name=None, domain_id=None):
        super(Group, self).__init__(locals())

    @classmethod
    def _dict_to_obj(cls, data):
        if data is None:
            return None

        return cls(
            id_=data.get("id"),
            name=data.get("name"),
            domain_id=data.get("domain_id"))

class Groups(BaseIdentityListModel):
    def __init__(self, list_=None):
        super(Groups, self).__init__(list_ or [])

    @classmethod
    def _dict_to_obj(cls, data):
        if data is None:
            return None
        return cls._list_to_obj(data.get('groups', []))

    @classmethod
    def _list_to_obj(cls, data):
        groups = cls()
        for group in data:
            groups.append(Group._dict_to_obj(group))
        return groups
