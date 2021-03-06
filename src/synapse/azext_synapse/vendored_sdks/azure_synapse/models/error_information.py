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


class ErrorInformation(Model):
    """ErrorInformation.

    :param message:
    :type message: str
    :param error_code:
    :type error_code: str
    :param source: Possible values include: 'System', 'User', 'Unknown',
     'Dependency'
    :type source: str or ~azure.synapse.models.ErrorSource
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorInformation, self).__init__(**kwargs)
        self.message = kwargs.get('message', None)
        self.error_code = kwargs.get('error_code', None)
        self.source = kwargs.get('source', None)
