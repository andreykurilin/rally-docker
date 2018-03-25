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
from xrally_docker.scenarios import container


class RunContainerTestCase(test.TestCase):

    def test_run(self):
        random_name = "RandomName"
        command = "echo 'hi!'"

        gen_name = mock.MagicMock(return_value=random_name)
        dclient = mock.MagicMock()
        dclient.return_value.containers.run.return_value = "some output"

        scenario = container.RunContainer({"docker": {"images": []}})
        scenario.client = dclient
        scenario.generate_random_name = gen_name

        scenario.run("foo", command)

        dclient.return_value.images.pull.assert_called_once_with("foo:latest")

        gen_name.assert_called_once_with()
        dclient.return_value.containers.run.assert_called_once_with(
            image="foo:latest",
            name=random_name,
            command=command
        )