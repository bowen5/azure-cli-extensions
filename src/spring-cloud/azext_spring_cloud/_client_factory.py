# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azure.cli.core.commands.client_factory import get_mgmt_service_client
from .vendored_sdks.appplatform import AppPlatformManagementClient


def cf_spring_cloud(cli_ctx, *_):
    return get_mgmt_service_client(cli_ctx, AppPlatformManagementClient)


def cf_app_services(cli_ctx, *_):
    return cf_spring_cloud(cli_ctx).services


def cf_apps(cli_ctx, *_):
    return cf_spring_cloud(cli_ctx).apps


def cf_deployments(cli_ctx, *_):
    return cf_spring_cloud(cli_ctx).deployments


def cf_bindings(cli_ctx, *_):
    return cf_spring_cloud(cli_ctx).bindings