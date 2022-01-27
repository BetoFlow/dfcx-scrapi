"""CX Versions Resource functions."""

# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from typing import Dict
import google.cloud.dialogflowcx_v3beta1.services as services
import google.cloud.dialogflowcx_v3beta1.types as types
from dfcx_scrapi.core.scrapi_base import ScrapiBase

# logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Versions(ScrapiBase):
    """Core Class for CX Versions Resource functions."""

    def __init__(
        self,
        creds_path: str = None,
        creds_dict: Dict = None,
        creds=None,
        flow_id: str = None,
    ):
        super().__init__(
            creds_path=creds_path,
            creds_dict=creds_dict,
            creds=creds,
        )

        if flow_id:
            self.flow_id = flow_id

    def list_versions(self, flow_id):
        """List all Versions for a given Flow"""

        request = types.version.ListVersionsRequest()

        request.parent = flow_id
        client_options = self._set_region(flow_id)
        client = services.versions.VersionsClient(
            client_options=client_options, credentials=self.creds
        )

        response = client.list_versions(request)

        versions = []
        for page in response.pages:
            for version in page.versions:
                versions.append(version)

        return versions