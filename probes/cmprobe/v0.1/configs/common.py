#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: omotcha

import os
# project structure
configs_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.split(configs_dir)[0]
cmc_bin_path = project_dir + "/cmc/cmc"
cmc_sdk_config_path = project_dir + "/cmc/testdata/sdk_config.yml"

# probing logic
round_robin = False
allow_mail_alert = False
allow_file_alert = True
allow_txpool_scanning = True
allow_print_alert = False

# pending transaction tolerance
pending_transaction_tolerance = 5

# probing frequency
probe_interval = 20
scheduler_interval = 1
consensus_tolerance_1 = 5
consensus_tolerance_2 = 60
consensus_tolerance_3 = 2000

# alert mail
subject_limit = 5
content_limit = 20
mail_count_limit = 5
mail_count_reset_interval = 4

# alert file
log_append = False
