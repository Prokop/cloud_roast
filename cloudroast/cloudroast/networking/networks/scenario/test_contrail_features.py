from random import randint
from cloudroast.networking.networks.fixtures import NetworkingComputeFixture
from cloudroast.networking.networks.scenario.common import ScenarioMixin
from cafe.drivers.unittest.datasets import DatasetList
from cafe.drivers.unittest.decorators import DataDrivenFixture, \
    data_driven_test, tags
from vnc_api import vnc_api
from cloudcafe.networking.networks.config import ContrailConfig
from cloudcafe.networking.networks.extensions.security_groups_api.composites \
    import SecurityGroupsComposite

CONF = ContrailConfig()

# Creating data sets for data driven test
data_set_list_lls = DatasetList()
data_set_list_lls.append_new_dataset(
        name='with_fabric_dns',
        data_dict={'lls_name': 'cloudroast-lls-%s' % randint(1, 9),
                   'lls_ip': '169.254.%s.%s' % (randint(0, 254),
                                                randint(1, 254)),
                   'lls_port': int(CONF.fabric_service_port),
                   'fabric_port': int(CONF.fabric_service_port),
                   'fabric_dns': CONF.fabric_service_name},
        tags=['scenario', 'sdn'])
data_set_list_lls.append_new_dataset(
        name='with_fabric_ip',
        data_dict={'lls_name': 'cloudroast-lls-%s' % randint(1, 9),
                   'lls_ip': '169.254.%s.%s' % (randint(0, 254),
                                                randint(1, 254)),
                   'lls_port': int(CONF.fabric_service_port),
                   'fabric_port': int(CONF.fabric_service_port),
                   'fabric_ip': CONF.fabric_service_ip,
                   },
        tags=['scenario', 'sdn'])


class ContrailTests(NetworkingComputeFixture, ScenarioMixin):

    PRIVATE_KEY_PATH = '/root/pkey'
    NSLOOKUP_COMMAND = 'nslookup %s'
    NC_COMMAND = 'nc -z %s %s'

    @classmethod
    def setUpClass(cls):
        super(ContrailTests, cls).setUpClass()
        cls.security_groups = SecurityGroupsComposite()

        # Create an instence for the tests
        cls._create_keypair()
        cls.open_securgroup = cls._create_open_loginable_secgroup()
        cls.server = cls._create_server('contrail',
                                        security_groups=[cls.open_securgroup])
        cls.server.remote_client = cls._get_remote_client(cls.server, True)
        cls.ssh_client = cls.server.remote_client.ssh_client

    def _provision_link_local(self, oper, lls_name, linklocal_obj):
        server_addr = CONF.api_server_ip
        if 'http' in server_addr:
            self._vnc_lib = vnc_api.VncApi(api_server_url=server_addr)
        else:
            self._vnc_lib = vnc_api.VncApi(api_server_host=server_addr)
        try:
            current_config = self._vnc_lib.global_vrouter_config_read(
                fq_name=['default-global-system-config',
                         'default-global-vrouter-config'])
        except Exception as e:
            if oper == "add":
                linklocal_services_obj = vnc_api.LinklocalServicesTypes([linklocal_obj])
                conf_obj = vnc_api.GlobalVrouterConfig(linklocal_services=linklocal_services_obj)
                result = self._vnc_lib.global_vrouter_config_create(conf_obj)
            return

        current_linklocal = current_config.get_linklocal_services()
        if current_linklocal is None:
            obj = {'linklocal_service_entry': []}
        else:
            obj = current_linklocal.__dict__
        new_linklocal = []
        for key, value in obj.iteritems():
            found = False
            for vl in value:
                entry = vl.__dict__
                if ('linklocal_service_name' in entry and
                        entry['linklocal_service_name'] == lls_name):
                    if oper == "add":
                        new_linklocal.append(linklocal_obj)
                    found = True
                else:
                    new_linklocal.append(vl)
            if not found and oper == "add":
                new_linklocal.append(linklocal_obj)
            obj[key] = new_linklocal

        conf_obj = vnc_api.GlobalVrouterConfig(linklocal_services=obj)
        result = self._vnc_lib.global_vrouter_config_update(conf_obj)


class ContrailvDNSTests(ContrailTests):

    @tags('scenario', 'sdn')
    def test_vdns_resolving_names(self):
        server_name = self.server.entity.name
        msg = ("Resolving a server's name %s has failed") % server_name
        response = self.ssh_client.execute_command(self.NSLOOKUP_COMMAND %
                                                   server_name)
        self.assertFalse(response.stderr)
        self.assertIn('Name: ', response.stdout.strip(), msg)


@DataDrivenFixture
class ContrailLLSTests(ContrailTests):

    @data_driven_test(data_set_list_lls)
    def ddtest_access_lls(self, lls_name='', lls_ip='', lls_port=0,
                          fabric_port=0, fabric_ip=[], fabric_dns=''):
        linklocal_obj = vnc_api.LinklocalServiceEntryType(
            linklocal_service_name=lls_name,
            linklocal_service_ip=lls_ip,
            linklocal_service_port=lls_port,
            ip_fabric_service_port=fabric_port,
            ip_fabric_service_ip=[fabric_ip],
            ip_fabric_DNS_service_name=fabric_dns)
        self._provision_link_local('add', lls_name, linklocal_obj)
        self.addClassCleanup(self._provision_link_local, 'delete', lls_name,
                             linklocal_obj)

        # invoke a command to validate LLS is reacheable
        self.ssh_client.execute_command(self.NC_COMMAND % (lls_ip,
                                                           fabric_port))
        self.assertTrue(True)

    @data_driven_test(data_set_list_lls)
    def ddtest_name_resolving_lls(self, lls_name='', lls_ip='', lls_port=0,
                                  fabric_port=0, fabric_ip=[],
                                  fabric_dns=''):
        linklocal_obj = vnc_api.LinklocalServiceEntryType(
            linklocal_service_name=lls_name,
            linklocal_service_ip=lls_ip,
            linklocal_service_port=lls_port,
            ip_fabric_service_port=fabric_port,
            ip_fabric_service_ip=[fabric_ip],
            ip_fabric_DNS_service_name=fabric_dns)
        self._provision_link_local('add', lls_name, linklocal_obj)
        self.addClassCleanup(self._provision_link_local, 'delete', lls_name,
                             linklocal_obj)

        # invoke a command to validate LLS name is resolvable
        self.ssh_client.execute_command(self.NC_COMMAND % (lls_name,
                                        fabric_port))
        self.assertTrue(True)
