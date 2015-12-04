__author__ = 'sprokopenko'

from cafe.drivers.unittest.decorators import tags
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

    @tags('subnets')
    def test_subnet_create(self):
        expected_net = self.network
        request_kwargs = dict(network_id=expected_net.id)
        name = 'test_create_subnet'
        request_kwargs['name'] = name
        expected_net.name = name
        resp = self.networks.subnets_api.behaviors.create_subnet(**request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        upd_net = resp.response.entity
        self.assertNetworkResponse(expected_net, upd_net)


    def test_subnet_read(self):
        expected_net = self.network
        request_kwargs = dict(network_id=expected_net.id)
        name = 'test_read_subnet'
        request_kwargs['name'] = name
        expected_net.name = name
        resp = self.networks.subnets_api.behaviors.get_subnet(**request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        upd_net = resp.response.entity
        self.assertNetworkResponse(expected_net, upd_net)


    def test_subnet_update(self):
        expected_net = self.network
        request_kwargs = dict(network_id=expected_net.id)
        name = 'test_create_subnet'
        request_kwargs['name'] = name
        expected_net.name = name
        resp = self.networks.subnets_api.behaviors.update_subnet(**request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        upd_net = resp.response.entity
        self.assertNetworkResponse(expected_net, upd_net)

    def test_subnet_delete(self):
        expected_net = self.network
        request_kwargs = dict(network_id=expected_net.id)
        name = 'test_create_subnet'
        request_kwargs['name'] = name
        expected_net.name = name
        resp = self.networks.subnets_api.behaviors.delete_subnet(**request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        upd_net = resp.response.entity
        self.assertNetworkResponse(expected_net, upd_net)


    def test_subnet_list(self):
        expected_net = self.network
        request_kwargs = dict(network_id=expected_net.id)
        name = 'test_create_subnet'
        request_kwargs['name'] = name
        expected_net.name = name
        resp = self.networks.subnets_api.behaviors.list_subnets(**request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        upd_net = resp.response.entity
        self.assertNetworkResponse(expected_net, upd_net)