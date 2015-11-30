"""
Copyright 2014 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from cafe.engine.http.client import AutoMarshallingHTTPClient
from cloudcafe.images.v2.models.image import (Image, Images, ImageUpdate,
                                              Member, Members)
from cloudcafe.images.v2.models.namespaces import (Namespace, Namespaces)
from cloudcafe.images.v2.models.resource_types import (ResourceType, ResourceTypes)
from cloudcafe.images.v2.models.properties import (Property, Properties)
from cloudcafe.images.v2.models.task import Task, Tasks
from cloudcafe.images.v2.models.versions import Versions
from cloudcafe.images.v2.models.objects import Object
from cloudcafe.images.v2.models.tags import Tag, Tags
from cloudcafe.images.v2.models.schemas import Schema


class ImagesClient(AutoMarshallingHTTPClient):
    """@summary: Client for Images v2"""

    def __init__(self, base_url, auth_token, serialize_format,
                 deserialize_format):
        """@summary: Constructs the images api client"""

        super(ImagesClient, self).__init__(serialize_format,
                                           deserialize_format)
        self.auth_token = auth_token
        self.serialize_format = serialize_format
        self.deserialize_format = deserialize_format
        self.default_headers['X-Auth-Token'] = auth_token
        ct = ''.join(['application/', self.serialize_format])
        accept = ''.join(['application/', self.deserialize_format])
        self.default_headers['Content-Type'] = ct
        self.default_headers['Accept'] = accept
        self.base_url = base_url

    def get_versions(self, url_addition=None, requestslib_kwargs=None):
        """@summary: List all available Cloud Images versions"""

        endpoint = self.base_url.replace('/v2', '')

        url = endpoint

        if url_addition:
            url = '{0}{1}'.format(endpoint, url_addition)

        return self.request('GET', url, response_entity_type=Versions,
                            requestslib_kwargs=requestslib_kwargs)

    def get_images_schema(self, requestslib_kwargs=None):
        """@summary: Get json schema of the images object"""

        url = '{0}/{1}'.format(self.base_url, 'schemas/images')
        return self.request('GET', url, requestslib_kwargs=requestslib_kwargs)

    def get_image_schema(self, requestslib_kwargs=None):
        """@summary: Get json schema of the image object"""

        url = '{0}/{1}'.format(self.base_url, 'schemas/image')
        return self.request('GET', url, requestslib_kwargs=requestslib_kwargs)

    def create_image(self, checksum=None, container_format=None,
                     created_at=None, disk_format=None, file_=None, id_=None,
                     min_disk=None, min_ram=None, name=None, protected=None,
                     schema=None, self_=None, size=None, status=None,
                     tags=None, updated_at=None, visibility=None,
                     additional_properties=None, requestslib_kwargs=None):
        """@summary:  Create a new image"""

        image = Image(checksum=checksum, container_format=container_format,
                      created_at=created_at, disk_format=disk_format,
                      file_=file_, id_=id_, min_disk=min_disk, min_ram=min_ram,
                      name=name, protected=protected, schema=schema,
                      self_=self_, size=size, status=status, tags=tags,
                      updated_at=updated_at, visibility=visibility,
                      additional_properties=additional_properties)
        url = '{0}/images'.format(self.base_url)
        return self.request('POST', url, request_entity=image,
                            response_entity_type=Image,
                            requestslib_kwargs=requestslib_kwargs)

    def get_image(self, image_id, requestslib_kwargs=None):
        """@summary: Get a single image"""

        url = '{0}/images/{1}'.format(self.base_url, image_id)
        return self.request('GET', url, response_entity_type=Image,
                            requestslib_kwargs=requestslib_kwargs)

    def list_images(self, filters=None, requestslib_kwargs=None):
        """
        @summary: List all images
        @param filters: filter params to list images call
        @type filters: dictionary
        @return: resp
        @rtype: Requests.response
        """
        url = '{0}/images'.format(self.base_url)
        return self.request('GET', url, params=filters,
                            response_entity_type=Images,
                            requestslib_kwargs=requestslib_kwargs)

    def update_image(self, image_id, replace=None, add=None, remove=None,
                     requestslib_kwargs=None):
        """@summary: Update an existing image"""

        url = '{0}/images/{1}'.format(self.base_url, image_id)
        image_update = ImageUpdate(add, replace, remove)
        headers = self.default_headers
        headers['Content-Type'] = (
            'application/openstack-images-v2.0-json-patch')
        return self.request('PATCH', url, headers=headers,
                            request_entity=image_update,
                            response_entity_type=Image,
                            requestslib_kwargs=requestslib_kwargs)

    def delete_image(self, image_id, requestslib_kwargs=None):
        """@summary: Delete an image"""

        url = '{0}/images/{1}'.format(self.base_url, image_id)
        return self.request('DELETE', url,
                            requestslib_kwargs=requestslib_kwargs)

    def store_image_file(self, image_id, file_data, content_type=None,
                         requestslib_kwargs=None):
        """@summary: Store image file data on given image id"""

        url = '{0}/images/{1}/file'.format(self.base_url, image_id)

        content_type = content_type or 'application/octet-stream'
        headers = {'Content-Type': content_type}

        return self.request('PUT', url, headers=headers, data=file_data)

    def get_image_file(self, image_id, requestslib_kwargs=None):
        """@summary: Get image file data for given image id"""

        url = '{0}/images/{1}/file'.format(self.base_url, image_id)
        return self.request('GET', url, response_entity_type=Image,
                            requestslib_kwargs=requestslib_kwargs)

    def add_tag(self, image_id, tag, requestslib_kwargs=None):
        """@summary: Add a tag to an image"""

        url = '{0}/images/{1}/tags/{2}'.format(self.base_url, image_id, tag)
        return self.request('PUT', url, requestslib_kwargs=requestslib_kwargs)

    def delete_tag(self, image_id, tag, requestslib_kwargs=None):
        """@summary: Delete a tag from an image"""

        url = '{0}/images/{1}/tags/{2}'.format(self.base_url, image_id, tag)
        return self.request('DELETE', url,
                            requestslib_kwargs=requestslib_kwargs)

    def get_image_members_schema(self, requestslib_kwargs=None):
        """@summary: Get schema of the image members object"""

        url = '{0}/{1}'.format(self.base_url, 'schemas/members')
        return self.request('GET', url, requestslib_kwargs=requestslib_kwargs)

    def get_image_member_schema(self, requestslib_kwargs=None):
        """@summary: Get schema of the image member object"""

        url = '{0}/{1}'.format(self.base_url, 'schemas/member')
        return self.request('GET', url, requestslib_kwargs=requestslib_kwargs)

    def add_member(self, image_id, member_id, requestslib_kwargs=None):
        """@summary: Add a member to an image"""

        url = '{0}/images/{1}/members'.format(self.base_url, image_id)
        member = Member(member_id=member_id)
        return self.request('POST', url, request_entity=member,
                            response_entity_type=Member,
                            requestslib_kwargs=requestslib_kwargs)

    def get_member(self, image_id, member_id, requestslib_kwargs=None):
        """@summary: List all image members"""

        url = '{0}/images/{1}/members/{2}'.format(self.base_url, image_id,
                                                  member_id)
        return self.request('GET', url, response_entity_type=Member,
                            requestslib_kwargs=requestslib_kwargs)

    def list_members(self, image_id, requestslib_kwargs=None):
        """@summary: List all image members"""

        url = '{0}/images/{1}/members'.format(self.base_url, image_id)
        return self.request('GET', url, response_entity_type=Members,
                            requestslib_kwargs=requestslib_kwargs)

    def update_member(self, image_id, member_id, status,
                      requestslib_kwargs=None):
        """@summary: Update a member for an image"""

        url = '{0}/images/{1}/members/{2}'.format(self.base_url, image_id,
                                                  member_id)
        member = Member(status=status)
        return self.request('PUT', url, request_entity=member,
                            response_entity_type=Member,
                            requestslib_kwargs=requestslib_kwargs)

    def delete_member(self, image_id, member_id):
        """@summary: Delete a member from an image"""

        url = '{0}/images/{1}/members/{2}'.format(self.base_url, image_id,
                                                  member_id)
        return self.request('DELETE', url)

    def get_tasks_schema(self, requestslib_kwargs=None):
        """@summary: Get schema of the tasks object"""

        url = '{0}/{1}'.format(self.base_url, 'schemas/tasks')

        return self.request('GET', url, requestslib_kwargs=requestslib_kwargs)

    def get_task_schema(self, requestslib_kwargs=None):
        """@summary: Get schema of the task object"""

        url = '{0}/{1}'.format(self.base_url, 'schemas/task')

        return self.request('GET', url, requestslib_kwargs=requestslib_kwargs)

    def create_task(self, input_=None, type_=None, requestslib_kwargs=None):
        """@summary: Create a new task"""

        task = Task(input_=input_, type_=type_)

        url = '{0}/tasks'.format(self.base_url)

        return self.request('POST', url, request_entity=task,
                            response_entity_type=Task,
                            requestslib_kwargs=requestslib_kwargs)

    def get_task(self, task_id, requestslib_kwargs=None):
        """@summary: Get a single task"""

        url = '{0}/tasks/{1}'.format(self.base_url, task_id)

        return self.request('GET', url, response_entity_type=Task,
                            requestslib_kwargs=requestslib_kwargs)

    def list_tasks(self, limit=None, marker=None, sort_dir=None, status=None,
                   type_=None, requestslib_kwargs=None):
        """@summary: List all tasks"""

        url = '{0}/tasks'.format(self.base_url)

        params = {'limit': limit, 'marker': marker, 'sort_dir': sort_dir,
                  'status': status, 'type': type_}

        return self.request('GET', url, params=params,
                            response_entity_type=Tasks,
                            requestslib_kwargs=requestslib_kwargs)

    def delete_task(self, task_id, requestslib_kwargs=None):
        """
        @summary: Deletes the specified task
        @param task_id: The id of a task
        @type task_id: String
        @return: resp
        @rtype: Requests.response
        """

        url = '{0}/tasks/{1}'.format(self.base_url, task_id)

        resp = self.request('DELETE', url, response_entity_type=Task,
                            requestslib_kwargs=requestslib_kwargs)

        return resp

    def create_namespace(self, namespace, display_name=None, description=None, visibility=None, protected=None,
                         properties=None, objects=None, resource_type_associations=None, additional_properties=None,
                         requestslib_kwargs=None):

        """@summary:  Create a new image"""

        namespace = Namespace(namespace=namespace, display_name=display_name, description=description,
                              visibility=visibility, protected=protected, properties=properties, objects=objects,
                              resource_type_associations=resource_type_associations,
                              additional_properties=additional_properties)
        url = '{0}/metadefs/namespaces'.format(self.base_url)
        return self.request('POST', url, request_entity=namespace, response_entity_type=Namespace,
                            requestslib_kwargs=requestslib_kwargs)

    def update_namespace(self, namespace, display_name=None, description=None, visibility=None, protected=None,
                         properties=None, objects=None, resource_type_associations=None, additional_properties=None,
                         requestslib_kwargs=None):

        """@summary:  Create a new image"""

        namespace = Namespace(namespace=namespace, display_name=display_name, description=description,
                              visibility=visibility, protected=protected, properties=properties, objects=objects,
                              resource_type_associations=resource_type_associations,
                              additional_properties=additional_properties)
        url = '{0}/metadefs/namespaces/{1}'.format(self.base_url, namespace.namespace)
        return self.request('PUT', url, request_entity=namespace, response_entity_type=Namespace,
                            requestslib_kwargs=requestslib_kwargs)

    def list_namespaces(self, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Namespaces,
                            requestslib_kwargs=requestslib_kwargs)

    def get_namespace(self, namespace, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}'.format(self.base_url, namespace)
        return self.request('GET', url, response_entity_type=Namespace,
                            requestslib_kwargs=requestslib_kwargs)

    def delete_namespace(self, namespace, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}'.format(self.base_url, namespace)
        return self.request('DELETE', url, response_entity_type=Namespace,
                            requestslib_kwargs=requestslib_kwargs)

    def list_resource_types(self, requestslib_kwargs=None):
        url = '{0}/metadefs/resource_types'.format(self.base_url)
        return self.request('GET', url, response_entity_type=ResourceType,
                            requestslib_kwargs=requestslib_kwargs)

    def create_resource_type_association(self, namespace, name=None,
                            prefix='_', properties_target='image',
                            requestslib_kwargs=None):

        """@summary:  Create a new resource type association"""

        resource_type_association = ResourceType(
            name=name, prefix=prefix, properties_target=properties_target)
        url = '{0}/metadefs/namespaces/{1}/resource_types'.format(self.base_url,
                            namespace)
        return self.request('POST', url,
                            request_entity=resource_type_association,
                            response_entity_type=ResourceType,
                            requestslib_kwargs=requestslib_kwargs)

    def delete_resource_type_association(self, namespace, name,
                                         requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/resource_types/{2}'.format(
            self.base_url, namespace, name)
        return self.request('DELETE', url, response_entity_type=ResourceType,
                            requestslib_kwargs=requestslib_kwargs)

    def list_resource_type_associations(self, namespace,
                                        requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/resource_types'.format(self.base_url,
                                                                    namespace)
        return self.request('GET', url, response_entity_type=ResourceType,
                            requestslib_kwargs=requestslib_kwargs)

    def create_property(self, namespace, name, description=None, enum=None,
                            title=None, type=None, requestslib_kwargs=None):

        """@summary:  Create a new property"""

        property = Property(description=description, enum=enum, name=name,
                            title=title, type=type)
        url = '{0}/metadefs/namespaces/{1}/properties'.format(self.base_url,
                            namespace)
        return self.request('POST', url,
                            request_entity=property,
                            response_entity_type=Property,
                            requestslib_kwargs=requestslib_kwargs)

    def remove_property_definition(self, namespace, name,
                                         requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/properties/{2}'.format(
            self.base_url, namespace, name)
        return self.request('DELETE', url, response_entity_type=Property,
                            requestslib_kwargs=requestslib_kwargs)

    def list_properties(self, namespace, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/properties'.format(self.base_url,
                                namespace)
        return self.request('GET', url, response_entity_type=Property,
                            requestslib_kwargs=requestslib_kwargs)

    def get_property_definition(self, namespace, name, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/properties/{2}'.format(self.base_url,
                                namespace, name)
        return self.request('GET', url, response_entity_type=Property,
                            requestslib_kwargs=requestslib_kwargs)

    def update_property_definition(self, namespace, name, description=None,
        enum=None, title=None, type=None, requestslib_kwargs=None):

        property = Property(description=description, enum=enum, name=name,
                            title=title, type=type)
        url = '{0}/metadefs/namespaces/{1}/properties/{2}'.format(self.base_url,
                namespace, name)
        return self.request('PUT', url, request_entity=property,
                            response_entity_type=Property,
                            requestslib_kwargs=requestslib_kwargs)

    def create_object(self, namespace, name, description=None, properties=None,
                            required=None, requestslib_kwargs=None):

        """@summary:  Create a new metadata definition object"""

        obj = Object(description=description, name=name,
                            properties=properties, required=required)
        url = '{0}/metadefs/namespaces/{1}/objects'.format(self.base_url,
                            namespace)
        return self.request('POST', url,
                            request_entity=obj,
                            response_entity_type=Object,
                            requestslib_kwargs=requestslib_kwargs)

    def list_objects(self, namespace, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/objects'.format(self.base_url,
                            namespace)
        return self.request('GET', url, response_entity_type=Object,
                            requestslib_kwargs=requestslib_kwargs)

    def get_object_definition(self, namespace, name, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/objects/{2}'.format(self.base_url,
                                namespace, name)
        return self.request('GET', url, response_entity_type=Object,
                            requestslib_kwargs=requestslib_kwargs)

    def update_object_definition(self, namespace, name, description=None,
        properties=None, required=None, requestslib_kwargs=None):
        obj = Object(description=description, name=name,
                            properties=properties, required=required)
        url = '{0}/metadefs/namespaces/{1}/objects/{2}'.format(self.base_url,
                            namespace, name)
        return self.request('PUT', url,
                            request_entity=obj,
                            response_entity_type=Object,
                            requestslib_kwargs=requestslib_kwargs)

    def delete_objects_definition(self, namespace, name,
        requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/objects/{2}'.format(self.base_url,
                            namespace, name)
        return self.request('DELETE', url, response_entity_type=Object,
                            requestslib_kwargs=requestslib_kwargs)

    def create_tags(self, namespace, name, requestslib_kwargs=None):

        """@summary:  Create a new metadata definition tag"""

        tags = Tags([Tag(name)])
        url = '{0}/metadefs/namespaces/{1}/tags'.format(self.base_url,
                                                        namespace)
        return self.request('POST', url, request_entity=tags,
                            response_entity_type=Tags,
                            requestslib_kwargs=requestslib_kwargs)

    def list_tags(self, namespace, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/tags'.format(self.base_url,
        namespace)
        return self.request('GET', url, response_entity_type=Tags,
                            requestslib_kwargs=requestslib_kwargs)

    def delete_tags(self, namespace, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/tags'.format(self.base_url,
        namespace)
        return self.request('DELETE', url, response_entity_type=Tags,
                            requestslib_kwargs=requestslib_kwargs)

    def add_tag_definition(self, namespace, name, requestslib_kwargs=None):

        """@summary:  Create a new metadata definition tag"""

        url = '{0}/metadefs/namespaces/{1}/tags/{2}'.format(self.base_url,
                                                            namespace, name)
        return self.request('POST', url,
                            response_entity_type=Tag,
                            requestslib_kwargs=requestslib_kwargs)

    def get_tag_definition(self, namespace, name, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/tags/{2}'.format(self.base_url,
                                                            namespace, name)
        return self.request('GET', url, response_entity_type=Tag,
                            requestslib_kwargs=requestslib_kwargs)

    def update_tag_definition(self, namespace, name, new_name,
                              requestslib_kwargs=None):
        tag = Tag(name=new_name)
        url = '{0}/metadefs/namespaces/{1}/tags/{2}'.format(self.base_url,
        namespace, name)
        return self.request('PUT', url, request_entity=tag,
                            response_entity_type=Tag,
                            requestslib_kwargs=requestslib_kwargs)

    def delete_tag_definition(self, namespace, name, requestslib_kwargs=None):
        url = '{0}/metadefs/namespaces/{1}/tags/{2}'.format(self.base_url,
        namespace, name)
        return self.request('DELETE', url, response_entity_type=Tag,
                            requestslib_kwargs=requestslib_kwargs)

    def get_metadata_definition_namespace_schema(self, requestslib_kwargs=None):
        url = '{0}/schemas/metadefs/namespace'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Schema,
                            requestslib_kwargs=requestslib_kwargs)

    def get_metadata_definition_namespaces_schema(self, requestslib_kwargs=None):
        url = '{0}/schemas/metadefs/namespaces'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Schema,
                            requestslib_kwargs=requestslib_kwargs)

    def get_metadata_definition_object_schema(self, requestslib_kwargs=None):
        url = '{0}/schemas/metadefs/object'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Schema,
                            requestslib_kwargs=requestslib_kwargs)

    def get_metadata_definition_objects_schema(self, requestslib_kwargs=None):
        url = '{0}/schemas/metadefs/objects'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Schema,
                            requestslib_kwargs=requestslib_kwargs)

    def get_metadata_definition_property_schema(self, requestslib_kwargs=None):
        url = '{0}/schemas/metadefs/property'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Schema,
                            requestslib_kwargs=requestslib_kwargs)

    def get_metadata_definition_properties_schema(self, requestslib_kwargs=None):
        url = '{0}/schemas/metadefs/properties'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Schema,
                            requestslib_kwargs=requestslib_kwargs)

    def get_metadata_definition_tag_schema(self, requestslib_kwargs=None):
        url = '{0}/schemas/metadefs/tag'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Schema,
                            requestslib_kwargs=requestslib_kwargs)

    def get_metadata_definition_tags_schema(self, requestslib_kwargs=None):
        url = '{0}/schemas/metadefs/tags'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Schema,
                            requestslib_kwargs=requestslib_kwargs)

    def get_metadata_namespace_definition_resource_type_association_schema(
            self, requestslib_kwargs=None):
        url = '{0}/schemas/metadefs/resource_type'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Schema,
                            requestslib_kwargs=requestslib_kwargs)

    def get_metadata_namespace_definition_resource_types_association_schema(
            self, requestslib_kwargs=None):
        url = '{0}/schemas/metadefs/resource_types'.format(self.base_url)
        return self.request('GET', url, response_entity_type=Schema,
                            requestslib_kwargs=requestslib_kwargs)