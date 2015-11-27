"""
Copyright 2013 Rackspace

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
from os import path


class RequestUtilities(object):

    @classmethod
    def get_id(cls, request):
        """
        Utility to extract the producer id from location header
        """
        location = request.headers.get('location')
        extracted_id = None
        if location:
            extracted_id = int(path.split(location)[1])
        return extracted_id
