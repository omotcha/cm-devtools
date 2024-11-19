#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: omotcha

from configs.common import cmc_sdk_config_path, cmc_bin_path

# contract call
contract_name = "probe"
contract_name_cm = "b7a5f9b5bab88de99a8e7f87f6c3719f1fba5723"
method_name = "check"
contract_params = ""

# statements
probe_statements = [
    cmc_bin_path,
    "client",
    "contract",
    "user",
    "invoke",
    "--contract-name=" + contract_name,
    "--method=" + method_name,
    "--sdk-conf-path=" + cmc_sdk_config_path,
    "--params=" + contract_params,
    "--sync-result=true"
]

txpool_statements = [
    cmc_bin_path,
    "txpool",
    "txids",
    "--sdk-conf-path=" + cmc_sdk_config_path
]

# flattened statements
# probe_statement = " ".join(probe_statements)
# txpool_statement = " ".join(txpool_statements)
