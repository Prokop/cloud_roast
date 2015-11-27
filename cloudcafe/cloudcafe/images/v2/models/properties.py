
import json

from cafe.engine.models.base import (
    AutoMarshallingListModel, AutoMarshallingModel)
from cloudcafe.compute.common.equality_tools import EqualityTools


class Property(AutoMarshallingModel):
    """@Summary: Metadata definition properties v2 model"""

    def __init__(self, description=None, enum=None, name=None, title=None,
                 type=None, additional_properties=None):
        self.description = description
        self.enum = enum
        self.name = name
        self.title = title
        self.type = type
        self.additional_properties = additional_properties

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
        if 'properties' in json_dict.keys():
            properties = []
            for property_dict in json_dict['properties']:
                properties.append(cls._dict_to_obj(property_dict))
            return properties
        else:
            return cls._dict_to_obj(json_dict)

    @classmethod
    def _dict_to_obj(cls, json_dict):
        additional_properties = {}
        for key, value in json_dict.items():
            if key not in ['description', 'enum', 'name', 'title', 'type']:
                additional_properties.update({key: value})
        property = Property(description=json_dict.get('description'),
                              enum=json_dict.get('enum'),
                              name=json_dict.get('name'),
                              title=json_dict.get('title'),
                              type=json_dict.get('type'),
                              additional_properties=additional_properties)
        return property

    def _obj_to_json(self):
        obj_dict = {}
        obj_dict['description'] = self.description
        obj_dict['enum'] = self.enum
        obj_dict['name'] = self.name
        obj_dict['title'] = self.title
        obj_dict['type'] = self.type
        obj_dict = self._remove_empty_values(obj_dict)
        return json.dumps(obj_dict)

    @classmethod
    def _xml_to_obj(cls, serialized_str):
        raise NotImplementedError(
            'Glance does not serve XML-formatted resources')

    def _obj_to_xml(self):
        raise NotImplementedError(
            'Glance does not serve XML-formatted resources')


class Properties(AutoMarshallingListModel):
    """@Summary: Metadata definition namespaces v2 model"""

    def __init__(self, properties=None):
        super(Properties, self).__init__()
        self.extend(properties or [])

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls._list_to_obj(json_dict.get('images'))

    @classmethod
    def _list_to_obj(cls, dict_list):
        properties = Properties()
        for property_dict in dict_list:
            properties.append(Property._dict_to_obj(property_dict))
        return properties
