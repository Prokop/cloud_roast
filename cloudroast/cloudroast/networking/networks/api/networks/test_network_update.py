"""
Copyright 2015 Symantec

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

from cafe.drivers.unittest.decorators import tags
from cloudcafe.networking.networks.common.constants \
    import NeutronResponseCodes, NeutronErrorTypes
from cloudcafe.networking.networks.common.models.response.network \
    import Network
from cloudroast.networking.networks.fixtures import NetworkingAPIFixture


class NetworkUpdateDeleteTest(NetworkingAPIFixture):

    @classmethod
    def setUpClass(cls):
        """Setting up test data"""
        super(NetworkUpdateDeleteTest, cls).setUpClass()

        # Data for creating networks and asserting responses
        cls.network_data = dict(
            status='ACTIVE', subnets=[],
            name='test_net_create', admin_state_up=True,
            tenant_id=cls.net.networking_auth_composite().tenant_id,
            shared=False)
        cls.expected_network = Network(**cls.network_data)

    def setUp(self):
        # Creating network
        resp = self.networks.behaviors.create_network(
            name=self.expected_network.name, use_exact_name=True,
            raise_exception=False)
        if resp.response.entity and hasattr(resp.response.entity, 'id'):
            self.delete_networks.append(resp.response.entity.id)

        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        self.network = resp.response.entity

        # Check the Network response
        self.assertNetworkResponse(self.expected_network, self.network)

    def tearDown(self):
        self.networkingCleanUp()

    @tags('periodic', 'smoke')
    def test_network_update(self):
        expected_net = self.network
        request_kwargs = dict(network_id=expected_net.id)

        name = 'test_net_updated'
        request_kwargs['name'] = name
        expected_net.name = name

        resp = self.networks.behaviors.update_network(**request_kwargs)

        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        upd_net = resp.response.entity

        self.assertNetworkResponse(expected_net, upd_net)

    @tags('periodic', 'smoke')
    def test_network_delete(self):
        """
        @summart: Testing deleting a network
        """
        expected_network = self.network

        resp = self.networks.behaviors.delete_network(expected_network.id)
        self.assertFalse(resp.failures)

        resp = self.networks.behaviors.get_network(expected_network.id)

        neg_msg = ('(negative) Getting a deleted network')
        status_code = NeutronResponseCodes.NOT_FOUND
        error_type = NeutronErrorTypes.NETWORK_NOT_FOUND
        self.assertNegativeResponse(
            resp=resp, status_code=status_code, msg=neg_msg,
            delete_list=self.delete_networks,
            error_type=error_type)
