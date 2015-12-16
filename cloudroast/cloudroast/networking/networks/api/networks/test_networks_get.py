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
from cloudcafe.networking.networks.common.models.response.network \
    import Network
from cloudroast.networking.networks.fixtures import NetworkingAPIFixture
import pdb


class NetworkGetTest(NetworkingAPIFixture):

    @classmethod
    def setUpClass(cls):
        """Setting up test data"""
        super(NetworkGetTest, cls).setUpClass()

        # Data for creating networks and asserting responses
        cls.network_data = dict(
            status='ACTIVE', subnets=[],
            name='test_net_ create', admin_state_up=None,
            tenant_id=cls.net.networking_auth_composite().tenant_id,
            shared=False)

        cls.expected_network = Network(**cls.network_data)
        cls.expected_network.admin_state_up = True

    def setUp(self):
        self.network = self.create_test_network(self.expected_network)

    @tags('periodic', 'smoke')
    def test_network_get(self):
        expected_network = self.network
        resp = self.networks.behaviors.get_network(expected_network.id)

        self.assertFalse(resp.failures)
        network = resp.response.entity

        # Check the Network response
        self.assertNetworkResponse(expected_network, network,
                check_exact_name=False)

    @tags('periodic', 'smoke')
    def test_networks_list(self):
        resp = self.networks.behaviors.list_networks()

        self.assertFalse(resp.failures)
        net_list = resp.response.entity

        msg = ('Network {0} missing in expected network list').format(
                self.network, net_list)
        self.assertIn(self.network, net_list, msg)
