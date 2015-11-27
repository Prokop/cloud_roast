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

from cloudcafe.networking.networks.common.behaviors \
    import NetworkingBaseBehaviors, NetworkingResponse


class FloatingIPsBehaviors(NetworkingBaseBehaviors):

    def __init__(self, floating_ip_client, floating_ip_config):
        super(FloatingIPsBehaviors, self).__init__()
        self.config = floating_ip_config
        self.client = floating_ip_client
