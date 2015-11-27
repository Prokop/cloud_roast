
import json

from cafe.engine.models.base import (
    AutoMarshallingListModel, AutoMarshallingModel)
from cloudcafe.compute.common.equality_tools import EqualityTools


class Schema(AutoMarshallingModel):
    """@Summary: Metadata definition objects v2 model"""

    def __init__(self, additional_properties=None, definitions=None,
                 name=None, properties=None, required=None):
        self.additional_properties = additional_properties
        self.definitions = definitions
        self.name = name
        self.properties = properties
        self.required = required

    def __eq__(self, other):
        return EqualityTools.are_objects_equal(self, other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        values = []
        for schema in self.__dict__:
            values.append("{0}: {1}".format(schema, self.__dict__[schema]))
        return '[{0}]'.format(', '.join(values))

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        if 'schemas' in json_dict.keys():
            schemas = []
            for schema_dict in json_dict['schemas']:
                schemas.append(cls._dict_to_obj(schema_dict))
            return schemas
        else:
            return cls._dict_to_obj(json_dict)

    @classmethod
    def _dict_to_obj(cls, json_dict):
        additional_properties = {}
        for key, value in json_dict.items():
            if key not in ['additional_properties', 'definitions', 'name'
            'properties', 'required']:
                additional_properties.update({key: value})
        schema = Schema(
            additional_properties = json_dict.get('additional_properties'),
                              definitions = json_dict.get('definitions'),
                              name=json_dict.get('name'),
                              properties=json_dict.get('properties'),
                              required = json_dict.get('required'))
        return schema

    def _obj_to_json(self):
        obj_dict = {}
        obj_dict['additional_properties'] = self.additional_properties
        obj_dict['definitions'] = self.definitions
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


class Schemas(AutoMarshallingListModel):
    """@Summary: Metadata definition namespaces v2 model"""

    def __init__(self, objs=None):
        super(Schemas, self).__init__()
        self.extend(objs or [])

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls._list_to_obj(json_dict.get('images'))

    @classmethod
    def _list_to_obj(cls, dict_list):
        schemas = Schemas()
        for schema_dict in dict_list:
            schemas.append(Schema._dict_to_obj(schema_dict))
        return schemas

