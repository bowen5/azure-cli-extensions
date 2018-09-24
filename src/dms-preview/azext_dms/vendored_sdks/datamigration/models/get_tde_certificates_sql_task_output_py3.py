# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GetTdeCertificatesSqlTaskOutput(Model):
    """Output of the task that gets TDE certificates in Base64 encoded format.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar base64_encoded_certificates: Mapping from certificate name to base
     64 encoded format.
    :vartype base64_encoded_certificates: dict[str, list[str]]
    :ivar validation_errors: Validation errors
    :vartype validation_errors:
     list[~azure.mgmt.datamigration.models.ReportableException]
    """

    _validation = {
        'base64_encoded_certificates': {'readonly': True},
        'validation_errors': {'readonly': True},
    }

    _attribute_map = {
        'base64_encoded_certificates': {'key': 'base64EncodedCertificates', 'type': '{[str]}'},
        'validation_errors': {'key': 'validationErrors', 'type': '[ReportableException]'},
    }

    def __init__(self, **kwargs) -> None:
        super(GetTdeCertificatesSqlTaskOutput, self).__init__(**kwargs)
        self.base64_encoded_certificates = None
        self.validation_errors = None