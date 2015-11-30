
import json

from cafe.engine.models.base import (
    AutoMarshallingListModel, AutoMarshallingModel)
from cloudcafe.compute.common.equality_tools import EqualityTools

class ResourceType(AutoMarshallingModel):
    """@Summary: Metadata definition resource_types v2 model"""

    def __init__(self, name=None, prefix=None, properties_target=None):
        self.name = name
        self.prefix = prefix
        self.properties_target = properties_target

    def __eq__(self, other):
        return EqualityTools.are_objects_equal(self, other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        values = []
        for prop in self.__dict__:
            values.append("{0}: {1}".format(prop, self.__dict__[prop]))
        return '[{0}]'.format(', '.join(values))

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        if 'resource_types' in json_dict.keys():
            resource_types = []
            for resource_types_dict in json_dict['resource_types']:
                resource_types.append(cls._dict_to_obj(resource_types_dict))
            return resource_types
        else:
            return cls._dict_to_obj(json_dict)

    @classmethod
    def _dict_to_obj(cls, json_dict):
        additional_properties = {}
        for key, value in json_dict.items():
            if key not in ['name', 'prefix', 'properties_target']:
                additional_properties.update({key: value})
        resource_type = ResourceType(name=json_dict.get('name'),
                              prefix=json_dict.get('prefix'))
        return resource_type

    def _obj_to_json(self):
        obj_dict = {}
        obj_dict['name'] = self.name
        obj_dict['prefix'] = self.prefix
        obj_dict['properties_target'] = self.properties_target
        return json.dumps(obj_dict)

    @classmethod
    def _xml_to_obj(cls, serialized_str):
        raise NotImplementedError(
            'Glance does not serve XML-formatted resources')

    def _obj_to_xml(self):
        raise NotImplementedError(
            'Glance does not serve XML-formatted resources')


class ResourceTypes(AutoMarshallingListModel):
    """@Summary: Metadata definition resource_types v2 model"""

    def __init__(self, resource_types=None):
        super(ResourceTypes, self).__init__()
        self.extend(resource_types or [])

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls._list_to_obj(json_dict.get('images'))

    @classmethod
    def _list_to_obj(cls, dict_list):
        resource_types = ResourceTypes()
        for resource_type_dict in dict_list:
            resource_types.append(ResourceType._dict_to_obj(resource_type_dict))
        return resource_types
