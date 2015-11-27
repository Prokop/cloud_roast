from cloudcafe.identity.common.client import BaseIdentityAPIClient
from cloudcafe.identity.v3.common.catalog.models.responses import Service, Catalog


class CatalogClient(BaseIdentityAPIClient):

    def get_catalog(self, requestslib_kwargs=None):
        """
        @summary: Fetching a service catalog
        @return: Catalog information
        @rtype: Catalog List
        """

        # GET v3/auth/catalog
        url = "{url}/auth/catalog".format(url=self.url)
        return self.get(url, response_entity_type=Catalog,
                        requestslib_kwargs=requestslib_kwargs)

    def create_service(self, type, requestslib_kwargs=None):
        url = "{url}/services".format(url=self.url)
        return self.post(url, response_entity_type=Service,
                        #headers={'x-subject-token': token},
                        requestslib_kwargs=requestslib_kwargs)

    def list_service(self, requestslib_kwargs=None):
        url = "{url}/services".format(url=self.url)
        return self.get(url, response_entity_type=Service,
                        requestslib_kwargs=requestslib_kwargs)

    def show_service_details(self, service_id, requestslib_kwargs=None):
        url = "{url}/services/{service_id}".format(url=self.url,
                                                   service_id=service_id)
        return self.get(url, response_entity_type=Service,
                        requestslib_kwargs=requestslib_kwargs)

    def update_service(self, service_id, type, requestslib_kwargs=None):
        url = "{url}/services/{service_id}".format(url=self.url,
                                          service_id=service_id)
        return self.patch(url, response_entity_type=Service,
                        requestslib_kwargs=requestslib_kwargs)

    def delete_service(self, service_id, requestslib_kwargs=None):
        url = "{url}/services/{service_id}".format(url=self.url,
                                          service_id=service_id)
        return self.delete(url, response_entity_type=Service,
                        requestslib_kwargs=requestslib_kwargs)


