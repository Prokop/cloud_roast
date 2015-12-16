__author__ = 'sprokopenko'

from cafe.drivers.unittest.decorators import tags
from cloudcafe.networking.networks.common.models.response.network \
    import Network
from cloudroast.networking.networks.fixtures import NetworkingAPIFixture
from cloudcafe.networking.networks.common.constants \
    import NeutronResponseCodes, NeutronErrorTypes
import pdb

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
        request_kwargs = dict(network_id=expected_net.id, name = 'test_create_subnet', use_exact_name=True)
        name = 'test_create_subnet'
        request_kwargs['name'] = name
        expected_net.name = name
        resp = self.subnets.behaviors.create_subnet(**request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        upd_subnet = resp.response.entity
        self.assertEqual(request_kwargs['name'],upd_subnet.name)
        self.assertEqual(request_kwargs['network_id'],upd_subnet.network_id)
        # self.assertSubnetResponse(upd_subnet)

    @tags('subnets')
    def test_subnet_read(self):
        expected_net = self.network
        request_kwargs = dict(network_id=expected_net.id, name = 'test_create_subnet', use_exact_name=True)
        name = 'test_create_subnet'
        request_kwargs['name'] = name
        expected_net.name = name
        resp = self.subnets.behaviors.create_subnet(**request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        created_subnet = resp.response.entity
        self.assertEqual(created_subnet, self.subnets.behaviors.get_subnet(created_subnet.id).response.entity)

    @tags('subnets','list_subnets')
    def test_subnet_list(self):
        expected_net = self.network
        request_kwargs = dict(network_id=expected_net.id, name = 'test_create_subnet', use_exact_name=True)
        name = 'test_create_subnet'
        request_kwargs['name'] = name
        expected_net.name = name
        resp = self.subnets.behaviors.create_subnet(**request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        subnet = resp.response.entity
        resp = self.subnets.behaviors.list_subnets()
        self.assertFalse(resp.failures)
        list_subnets = resp.response.entity

        msg = ('Network {0} missing in expected network list').format(
                self.network, list_subnets)
        self.assertIn(subnet, list_subnets, msg)


    @tags('subnets', 'sub_delete')
    def test_subnet_delete(self):
        """
        @summary: Testing deleting a subnet
        """
        expected_net = self.network
        request_kwargs = dict(network_id=expected_net.id, name = 'test_create_subnet_to_delete', use_exact_name=True)
        name = 'test_create_subnet'
        request_kwargs['name'] = name
        expected_net.name = name
        resp = self.subnets.behaviors.create_subnet(**request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        subnet = resp.response.entity
        request_kwargs = dict(subnet_id=subnet.id)
        resp_deletion = self.subnets.behaviors.delete_subnet(**request_kwargs)
        self.assertFalse(resp_deletion.failures)
        neg_msg = ('(negative) Getting a deleted subnet')
        status_code = NeutronResponseCodes.NOT_FOUND
        error_type = NeutronErrorTypes.SUBNET_NOT_FOUND
        getting_subnet = self.subnets.behaviors.get_subnet(subnet.id)
        self.assertNegativeResponse(
            resp=getting_subnet, status_code=status_code, msg=neg_msg,
            delete_list=self.delete_subnets,
            error_type=error_type)


    @tags('subnets','update_subnet')
    def test_subnet_update(self):
        expected_net = self.network
        request_kwargs = dict(network_id=expected_net.id, name = 'test_create_subnet', use_exact_name=True)
        name = 'test_create_subnet'
        request_kwargs['name'] = name
        expected_net.name = name
        resp = self.subnets.behaviors.create_subnet(**request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp.failures)
        created_subnet = resp.response.entity
        update_request_kwargs = dict(subnet_id=resp.response.entity.id, name="test_updated_subnet")
        resp_updated_net = self.subnets.behaviors.update_subnet(**update_request_kwargs)
        # Fail the test if any failure is found
        self.assertFalse(resp_updated_net.failures)
        updated_subnet = resp_updated_net.response.entity
        created_subnet.name='test_updated_subnet'
        self.assertSubnetResponse(created_subnet, updated_subnet)