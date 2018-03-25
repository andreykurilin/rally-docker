# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock

from tests.unit import test
from xrally_docker import service


class DockerServiceTestCase(test.TestCase):

    def setUp(self):
        super(DockerServiceTestCase, self).setUp()
        self.client = mock.MagicMock()
        self.docker = service.Docker({})
        self.docker._client = self.client

    def test_get_version(self):
        self.client.version.return_value = {"Version": 3}

        self.assertEqual(3, self.docker.get_version())

        self.client.version.assert_called_once_with()

    def test__fix_the_name(self):
        self.assertEqual("foo:bar", self.docker._fix_the_name("foo:bar"))
        self.assertEqual("foo:latest", self.docker._fix_the_name("foo"))

    def test_pull_image(self):
        image = self.client.images.pull.return_value
        image_name = "foo:bar"

        self.assertEqual(image.attrs, self.docker.pull_image(image_name))

        self.client.images.pull.assert_called_once_with(image_name)
