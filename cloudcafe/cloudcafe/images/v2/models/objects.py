
import json

from cafe.engine.models.base import (
    AutoMarshallingListModel, AutoMarshallingModel)
from cloudcafe.compute.common.equality_tools import EqualityTools


class Object(AutoMarshallingModel):
    """@Summary: Metadata definition objects v2 model"""

    def __init__(self, description=None, name=None, properties=None,
                 required=None, additional_properties=None):
        self.description = description
        self.name = name
        self.properties = properties
        self.required = required
        self.additional_properties = additional_properties

    def __eq__(self, other):
        return EqualityTools.are_objects_equal(self, other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        values = []
        for obj in self.__dict__:
            values.append("{0}: {1}".format(obj, self.__dict__[obj]))
        return '[{0}]'.format(', '.join(values))

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        if 'objects' in json_dict.keys():
            objects = []
            for obj_dict in json_dict['objects']:
                objects.append(cls._dict_to_obj(obj_dict))
            return objects
        else:
            return cls._dict_to_obj(json_dict)

    @classmethod
    def _dict_to_obj(cls, json_dict):
        additional_properties = {}
        for key, value in json_dict.items():
            if key not in ['description', 'name', 'properties', 'required']:
                additional_properties.update({key: value})
        obj = Object(description=json_dict.get('description'),
                              name=json_dict.get('name'),
                              properties=json_dict.get('properties'),
                              required=json_dict.get('required'),
                              additional_properties=additional_properties)
        return obj

    def _obj_to_json(self):
        obj_dict = {}
        obj_dict['description'] = self.description
        obj_dict['name'] = self.name
        obj_dict['properties'] = self.properties
        obj_dict['required'] = self.required
        obj_dict = self._remove_empty_values(obj_dict)
        return json.dumps(obj_dict)

    @classmethod
    def _xml_to_obj(cls, serialized_str):
        raise NotImplementedError(
            'Glance does not serve XML-formatted resources')

    def _obj_to_xml(self):
        raise NotImplementedError(
            'Glance does not serve XML-formatted resources')


class Objects(AutoMarshallingListModel):
    """@Summary: Metadata definition namespaces v2 model"""

    def __init__(self, objs=None):
        super(Objects, self).__init__()
        self.extend(objs or [])

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls._list_to_obj(json_dict.get('images'))

    @classmethod
    def _list_to_obj(cls, dict_list):
        objs = Objects()
        for obj_dict in dict_list:
            objs.append(Object._dict_to_obj(obj_dict))
        return objs

