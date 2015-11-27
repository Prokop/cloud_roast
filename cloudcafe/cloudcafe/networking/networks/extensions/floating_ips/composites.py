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

from cloudcafe.networking.networks.composites import _NetworkingAuthComposite
from cloudcafe.networking.networks.extensions.floating_ips.behaviors \
    import FloatingIPsBehaviors
from cloudcafe.networking.networks.extensions.floating_ips.client \
    import FloatingIPClient
from cloudcafe.networking.networks.extensions.floating_ips.config \
    import FloatingIPsConfig


class FloatingIPsComposite(object):
    networking_auth_composite = _NetworkingAuthComposite

    def __init__(self):
        auth_composite = self.networking_auth_composite()
        self.url = auth_composite.networking_url
        self.user = auth_composite._auth_user_config
        self.config = FloatingIPsConfig()
        self.client = FloatingIPClient(**auth_composite.client_args)

        self.behaviors = FloatingIPsBehaviors(
            floating_ip_client=self.client,
            floating_ip_config=self.config)
