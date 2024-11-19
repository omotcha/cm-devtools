#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: omotcha

import os
import sys
# uncomment line below if "module not found" happens
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import subprocess
from schedule import every, repeat, run_pending
from alert.mail_alert import send_mail_alert
from alert.file_alert import update_file_alert
from analyers.txpool_analyzer import analyze_txpool

from configs.common import round_robin, allow_mail_alert, allow_txpool_scanning, allow_file_alert, allow_print_alert
from configs.common import probe_interval, scheduler_interval, mail_count_reset_interval
from configs.common import consensus_tolerance_1
from configs.common import mail_count_limit
from configs.common import log_append
from statements.statements import probe_statements

global mail_count


@repeat(every(mail_count_reset_interval).hours)
def job_reset_mail_count():
    global mail_count
    if mail_count >= mail_count_limit:
        print("resetting mail count...")
        mail_count = 0
    time.sleep(10)


@repeat(every(probe_interval).seconds)
def job_probe():
    global mail_count
    aggregating_content: str = ""
    print("probing...")

    # call probe contract
    result = subprocess.run(probe_statements, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.stderr:
        aggregating_content += str(result.stderr)
        # analyze err
        if allow_txpool_scanning:
            aggregating_content += analyze_txpool()
        # mail alert
        if allow_mail_alert and mail_count < mail_count_limit:
            send_mail_alert(subject="Alert from cmprobe", content=aggregating_content)
            mail_count += 1
        # file alert
        if allow_file_alert:
            update_file_alert(aggregating_content, log_append)
        # print alert
        if allow_print_alert:
            print(aggregating_content)
    else:
        print(result.stdout)
    # wait for consensus
    time.sleep(consensus_tolerance_1)
    print("\n")


def single_probe() -> bool:
    aggregating_content: str = ""
    print("probing...")
    result = subprocess.run(probe_statements, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.stderr:
        # print(result.stderr)
        # print("\n")
        return False
    else:
        # print(result.stdout)
        # print("\n")
        return True


def probe_schedule():
    while True:
        run_pending()
        time.sleep(scheduler_interval)


if __name__ == '__main__':
    mail_count = 0
    if round_robin:
        probe_schedule()
    else:
        single_probe()
