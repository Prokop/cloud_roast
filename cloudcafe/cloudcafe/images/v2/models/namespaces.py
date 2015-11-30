
import json

from cafe.engine.models.base import (
    AutoMarshallingListModel, AutoMarshallingModel)
from cloudcafe.compute.common.equality_tools import EqualityTools


class Namespace(AutoMarshallingModel):
    """@Summary: Metadata definition namespaces v2 model"""

    def __init__(self, namespace=None, display_name=None, description=None, visibility=None, protected=None,
                 properties=None, objects=None, resource_type_associations=None, additional_properties=None):
        self.namespace = namespace
        self.display_name = display_name
        self.description = description
        self.visibility = visibility
        self.protected = protected
        self.properties = properties
        self.objects = objects
        self.resource_type_associations = resource_type_associations
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
        if 'namespaces' in json_dict.keys():
            namespaces = []
            for namespace_dict in json_dict['namespaces']:
                namespaces.append(cls._dict_to_obj(namespace_dict))
            return namespaces
        else:
            return cls._dict_to_obj(json_dict)

    @classmethod
    def _dict_to_obj(cls, json_dict):
        additional_properties = {}
        for key, value in json_dict.items():
            if key not in ['namespace', 'display_name', 'description', 'visibility', 'protected', 'properties',
                           'objects', 'resource_type_associations']:
                additional_properties.update({key: value})
        namespace = Namespace(namespace=json_dict.get('namespace'),
                              display_name=json_dict.get('display_name'),
                              description=json_dict.get('description'),
                              visibility=json_dict.get('visibility'),
                              protected=json_dict.get('protected'),
                              properties=json_dict.get('properties'),
                              objects=json_dict.get('objects'),
                              resource_type_associations=json_dict.get('resource_type_associations'),
                              additional_properties=additional_properties)
        return namespace

    def _obj_to_json(self):
        obj_dict = {}
        obj_dict['namespace'] = self.namespace
        obj_dict['display_name'] = self.display_name
        obj_dict['description'] = self.description
        obj_dict['visibility'] = self.visibility
        obj_dict['protected'] = self.protected
        obj_dict['properties'] = self.properties
        obj_dict['objects'] = self.objects
        obj_dict['resource_type_associations'] = self.resource_type_associations
        obj_dict = self._remove_empty_values(obj_dict)
        return json.dumps(obj_dict)

    @classmethod
    def _xml_to_obj(cls, serialized_str):
        raise NotImplementedError(
            'Glance does not serve XML-formatted resources')

    def _obj_to_xml(self):
        raise NotImplementedError(
            'Glance does not serve XML-formatted resources')


class Namespaces(AutoMarshallingListModel):
    """@Summary: Metadata definition namespaces v2 model"""

    def __init__(self, namespaces=None):
        super(Namespaces, self).__init__()
        self.extend(namespaces or [])

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls._list_to_obj(json_dict.get('images'))

    @classmethod
    def _list_to_obj(cls, dict_list):
        namespaces = Namespaces()
        for namespace_dict in dict_list:
            namespaces.append(Namespace._dict_to_obj(namespace_dict))
        return namespaces
