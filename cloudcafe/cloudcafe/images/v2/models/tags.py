
import json

from cafe.engine.models.base import (
    AutoMarshallingListModel, AutoMarshallingModel)
from cloudcafe.compute.common.equality_tools import EqualityTools


class Tag(AutoMarshallingModel):
    """@Summary: Metadata definition objects v2 model"""

    def __init__(self, name=None):
        self.name = name

    def __eq__(self, other):
        return EqualityTools.are_objects_equal(self, other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        values = []
        for tag in self.__dict__:
            values.append("{0}: {1}".format(tag, self.__dict__[tag]))
        return '[{0}]'.format(', '.join(values))

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        if 'tags' in json_dict.keys():
            tags = []
            for tag_dict in json_dict['tags']:
                tags.append(cls._dict_to_obj(tag_dict))
            return tags
        else:
            return cls._dict_to_obj(json_dict)

    @classmethod
    def _dict_to_obj(cls, json_dict):
        #additional_properties = {}
        """
        for key, value in json_dict.items():
            if key not in ['name']:
                additional_properties.update({key: value})
        """
        tag = Tag(name=json_dict.get('name'))

        return tag

    def _obj_to_json(self):
        obj_dict = {}
        obj_dict['name'] = self.name
        obj_dict = self._remove_empty_values(obj_dict)
        return json.dumps(obj_dict)

    @classmethod
    def _xml_to_obj(cls, serialized_str):
        raise NotImplementedError(
            'Glance does not serve XML-formatted resources')

    def _obj_to_xml(self):
        raise NotImplementedError(
            'Glance does not serve XML-formatted resources')


class Tags(AutoMarshallingListModel):
    """@Summary: Metadata definition namespaces v2 model"""

    def __init__(self, objs=None):
        super(Tags, self).__init__()
        self.extend(objs or [])

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls._list_to_obj(json_dict.get('tags'))

    @classmethod
    def _list_to_obj(cls, dict_list):
        tags = Tags()
        for tag_dict in dict_list:
            tags.append(Tag._dict_to_obj(tag_dict))
        return tags

    def _obj_to_json(self):
        obj_dict = {}
        obj_dict['tags'] = [dict(name=t.name) for t in self]
        obj_dict = self._remove_empty_values(obj_dict)
        return json.dumps(obj_dict)