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

import re

from cafe.drivers.unittest.fixtures import BaseTestFixture
from cloudcafe.auth.config import UserAuthConfig, UserConfig
from cloudcafe.auth.provider import AuthProvider
from cloudcafe.common.resources import ResourcePool
from cloudcafe.compute.common.exception_handler import ExceptionHandler
from cloudcafe.compute.config import ComputeEndpointConfig
from cloudcafe.compute.flavors_api.config import FlavorsConfig
from cloudcafe.compute.images_api.behaviors import (
    ImageBehaviors as ComputeImageBehaviors)
from cloudcafe.compute.images_api.client import (
    ImagesClient as ComputeImagesClient)
from cloudcafe.compute.servers_api.behaviors import ServerBehaviors
from cloudcafe.compute.servers_api.client import ServersClient
from cloudcafe.compute.servers_api.config import ServersConfig
from cloudcafe.images.common.constants import ImageProperties, Messages
from cloudcafe.images.config import (
    AltUserConfig, ImagesConfig, MarshallingConfig, ThirdUserConfig)
from cloudcafe.images.v2.behaviors import ImagesBehaviors
from cloudcafe.images.v2.client import ImagesClient
from cloudcafe.objectstorage.config import ObjectStorageConfig
from cloudcafe.objectstorage.objectstorage_api.behaviors import (
    ObjectStorageAPI_Behaviors)
from cloudcafe.objectstorage.objectstorage_api.client import (
    ObjectStorageAPIClient)
from cloudcafe.objectstorage.objectstorage_api.config import (
    ObjectStorageAPIConfig)


class ImagesFixture(BaseTestFixture):
    """@summary: Fixture for Cloud Images api"""

    @classmethod
    def setUpClass(cls):
        super(ImagesFixture, cls).setUpClass()
        cls.images_config = ImagesConfig()
        cls.marshalling = MarshallingConfig()
        cls.endpoint_config = UserAuthConfig()
        cls.user_config = UserConfig()
        cls.alt_user_config = AltUserConfig()
        cls.third_user_config = ThirdUserConfig()
        cls.resources = ResourcePool()
        cls.serialize_format = cls.marshalling.serializer
        cls.deserialize_format = cls.marshalling.deserializer

        cls.user_list = cls.generate_user_list(cls.images_config.account_list)

        cls.access_data = cls.user_list['user'][cls.ACCESS_DATA]
        cls.images_client = cls.user_list['user'][cls.CLIENT]
        cls.images_behavior = cls.user_list['user'][cls.BEHAVIOR]
        cls.tenant_id = cls.access_data.token.tenant.id_
        cls.addClassCleanup(cls.images_behavior.resources.release)

        if cls.user_list.get('alt_user'):
            cls.alt_access_data = cls.user_list['alt_user'][cls.ACCESS_DATA]
            cls.alt_images_client = cls.user_list['alt_user'][cls.CLIENT]
            cls.alt_images_behavior = cls.user_list['alt_user'][cls.BEHAVIOR]
            cls.alt_tenant_id = cls.alt_access_data.token.tenant.id_
            cls.addClassCleanup(cls.alt_images_behavior.resources.release)

        if cls.user_list.get('third_user'):
            cls.third_access_data = (
                cls.user_list['third_user'][cls.ACCESS_DATA])
            cls.third_images_client = cls.user_list['third_user'][cls.CLIENT]
            cls.third_images_behavior = (
                cls.user_list['third_user'][cls.BEHAVIOR])
            cls.third_tenant_id = cls.third_access_data.token.tenant.id_
            cls.addClassCleanup(cls.third_images_behavior.resources.release)

        if cls.user_list.get('images_admin_user'):
            cls.admin_access_data = cls.user_list['images_admin_user'][cls.ACCESS_DATA]
            cls.admin_images_client = cls.user_list['images_admin_user'][cls.CLIENT]
            cls.admin_images_behavior = cls.user_list['images_admin_user'][cls.BEHAVIOR]
            cls.admin_tenant_id = cls.access_data.token.tenant.id_
            cls.addClassCleanup(cls.admin_images_behavior.resources.release)

        cls.error_msg = Messages.ERROR_MSG
        cls.id_regex = re.compile(ImageProperties.ID_REGEX)
        cls.import_from = cls.images_config.import_from
        cls.import_from_bootable = cls.images_config.import_from_bootable
        cls.import_from_format = cls.images_config.import_from_format
        cls.export_to = cls.images_config.export_to
        cls.max_created_at_delta = cls.images_config.max_created_at_delta
        cls.max_expires_at_delta = cls.images_config.max_expires_at_delta
        cls.max_updated_at_delta = cls.images_config.max_updated_at_delta
        cls.test_file = cls.read_data_file(cls.images_config.test_file)

        cls.addClassCleanup(cls.resources.release)

        cls.exception_handler = ExceptionHandler()
        cls.images_client.add_exception_handler(cls.exception_handler)

    @classmethod
    def tearDownClass(cls):
        super(ImagesFixture, cls).tearDownClass()
        cls.resources.release()
        cls.images_behavior.resources.release()
        if cls.user_list.get('alt_user'):
            cls.alt_images_behavior.resources.release()
        if cls.user_list.get('third_user'):
            cls.third_images_behavior.resources.release()
        cls.images_client.delete_exception_handler(cls.exception_handler)

    @classmethod
    def generate_user_list(cls, account_list):
        """
        @summary: Generates list of users containing access_data, account
        types, behaviors, clients, and configurations
        """

        cls.ACCESS_DATA = "access_data"
        cls.BEHAVIOR = "behavior"
        cls.CLIENT = "client"
        cls.CONFIG = "config"
        user_list = dict()
        for user in account_list:
            user_list[user] = dict()
            user_list[user][cls.CONFIG] = UserConfig(section_name=user)
            user_list[user][cls.CONFIG].SECTION_NAME = user

            access_data = AuthProvider.get_access_data(
                cls.endpoint_config,
                user_config=user_list[user][cls.CONFIG])
            # If authentication fails, fail immediately
            if access_data is None:
                cls.assertClassSetupFailure('Authentication failed.')
            user_list[user][cls.ACCESS_DATA] = access_data

            images_service = access_data.get_service(
                cls.images_config.endpoint_name)
            images_url_check = images_service.get_endpoint(
                cls.images_config.region)
            # If endpoint validation fails, fail immediately
            if images_url_check is None:
                cls.assertClassSetupFailure('Endpoint validation failed')
            cls.url = (images_service.get_endpoint(
                cls.images_config.region).public_url)
            # If a url override was provided, use it instead
            if cls.images_config.override_url:
                cls.url = cls.images_config.override_url

            images_client = cls.generate_images_client(access_data)
            user_list[user][cls.CLIENT] = images_client

            images_behavior = ImagesBehaviors(images_client, cls.images_config)
            user_list[user][cls.BEHAVIOR] = images_behavior

        return user_list

    @classmethod
    def generate_images_client(cls, auth_data):
        """@summary: Returns new images client for requested auth data"""

        client_args = {'base_url': cls.url, 'auth_token': auth_data.token.id_,
                       'serialize_format': cls.serialize_format,
                       'deserialize_format': cls.deserialize_format}
        return ImagesClient(**client_args)

    @staticmethod
    def read_data_file(file_path):
        """@summary: Returns data file given a valid data file path"""
        try:
            with open(file_path, "r") as DATA:
                test_data = DATA.read().rstrip()
        except IOError as file_error:
            raise file_error

        return test_data

    @classmethod
    def get_comparison_data(cls, data_file):
        """
        @summary: Create comparison dictionary based on a given set of data
        """

        with open(data_file, "r") as DATA:
            all_data = DATA.readlines()

        comparison_dict = dict()
        for line in all_data:
            # Skip any comments or short lines
            if line.startswith('#') or len(line) < 5:
                continue
            # Get the defined data
            if line.startswith('+'):
                line = line.replace('+', '')
                data_columns = [x.strip().lower() for x in line.split('|')]
                continue
            # Process the data
            each_data = dict()
            data = [x.strip() for x in line.split("|")]
            for x, y in zip(data_columns[1:], data[1:]):
                each_data[x] = y
            comparison_dict[data[0]] = each_data

        return comparison_dict


class ComputeIntegrationFixture(ImagesFixture):
    """@summary: Fixture for compute integration with images v2 api"""

    @classmethod
    def setUpClass(cls):
        super(ComputeIntegrationFixture, cls).setUpClass()
        cls.flavors_config = FlavorsConfig()
        cls.servers_config = ServersConfig()
        cls.compute_endpoint = ComputeEndpointConfig()

        # Instantiate servers client
        compute_service = cls.access_data.get_service(
            cls.compute_endpoint.compute_endpoint_name)
        alt_compute_service = cls.alt_access_data.get_service(
            cls.compute_endpoint.compute_endpoint_name)
        compute_url_check = compute_service.get_endpoint(
            cls.compute_endpoint.region)
        alt_compute_url_check = alt_compute_service.get_endpoint(
            cls.compute_endpoint.region)
        # If compute endpoint validation fails, fail immediately
        if compute_url_check is None:
            cls.assertClassSetupFailure('Compute endpoint validation failed')
        # If compute endpoint validation fails, fail immediately
        if alt_compute_url_check is None:
            cls.assertClassSetupFailure('Compute endpoint validation failed')
        cls.compute_url = compute_service.get_endpoint(
            cls.compute_endpoint.region).public_url
        cls.alt_compute_url = alt_compute_service.get_endpoint(
            cls.compute_endpoint.region).public_url

        client_args = {'url': cls.compute_url,
                       'auth_token': cls.access_data.token.id_,
                       'serialize_format': cls.serialize_format,
                       'deserialize_format': cls.deserialize_format}
        cls.servers_client = ServersClient(**client_args)
        alt_client_args = {'url': cls.alt_compute_url,
                           'auth_token': cls.alt_access_data.token.id_,
                           'serialize_format': cls.serialize_format,
                           'deserialize_format': cls.deserialize_format}
        cls.alt_servers_client = ServersClient(**alt_client_args)

        # Instantiate compute images client and behavior
        cls.compute_images_client = ComputeImagesClient(**client_args)
        cls.alt_compute_images_client = ComputeImagesClient(**alt_client_args)
        cls.compute_image_behaviors = ComputeImageBehaviors(
            images_client=cls.compute_images_client,
            servers_client=cls.servers_client, config=cls.images_config)
        cls.alt_compute_image_behaviors = ComputeImageBehaviors(
            images_client=cls.alt_compute_images_client,
            servers_client=cls.alt_servers_client, config=cls.images_config)

        # Instantiate servers behavior
        cls.server_behaviors = ServerBehaviors(
            servers_client=cls.servers_client,
            images_client=cls.compute_images_client,
            servers_config=cls.servers_config, images_config=cls.images_config,
            flavors_config=cls.flavors_config)
        cls.alt_server_behaviors = ServerBehaviors(
            servers_client=cls.alt_servers_client,
            images_client=cls.alt_compute_images_client,
            servers_config=cls.servers_config, images_config=cls.images_config,
            flavors_config=cls.flavors_config)


class ObjectStorageIntegrationFixture(ComputeIntegrationFixture):
    """
    @summary: Fixture for object storage integration with images v2 api
    """

    @classmethod
    def setUpClass(cls):
        super(ObjectStorageIntegrationFixture, cls).setUpClass()
        cls.object_storage_config = ObjectStorageConfig()
        cls.object_storage_api_config = ObjectStorageAPIConfig()

        objectstorage_service = cls.access_data.get_service(
            cls.object_storage_config.identity_service_name)
        objectstorage_url_check = objectstorage_service.get_endpoint(
            cls.object_storage_config.region)
        # If endpoint validation fails, fail immediately
        if objectstorage_url_check is None:
            cls.assertClassSetupFailure('Endpoint validation failed')
        alt_objectstorage_service = cls.alt_access_data.get_service(
            cls.object_storage_config.identity_service_name)
        alt_objectstorage_url_check = alt_objectstorage_service.get_endpoint(
            cls.object_storage_config.region)
        # If endpoint validation fails, fail immediately
        if alt_objectstorage_url_check is None:
            cls.assertClassSetupFailure('Endpoint validation failed')

        cls.storage_url = objectstorage_service.get_endpoint(
            cls.object_storage_config.region).public_url
        cls.alt_storage_url = alt_objectstorage_service.get_endpoint(
            cls.object_storage_config.region).public_url

        cls.object_storage_client = ObjectStorageAPIClient(
            cls.storage_url, cls.access_data.token.id_)
        cls.alt_object_storage_client = ObjectStorageAPIClient(
            cls.alt_storage_url, cls.alt_access_data.token.id_)

        cls.object_storage_behaviors = ObjectStorageAPI_Behaviors(
            cls.object_storage_client, cls.object_storage_api_config)
        cls.alt_object_storage_behaviors = ObjectStorageAPI_Behaviors(
            cls.alt_object_storage_client, cls.object_storage_api_config)
