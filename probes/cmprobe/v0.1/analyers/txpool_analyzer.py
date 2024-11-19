#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: omotcha

import subprocess

from statements.statements import txpool_statements
from configs.common import pending_transaction_tolerance


def analyze_txpool() -> str:
    result = subprocess.run(txpool_statements, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.stderr:
        return "\n[txpool][error] cannot fetch txpool info:\n{0}\n".format(str(result.stderr))
    else:
        l: int = len(result.stdout)
        if l > pending_transaction_tolerance:
            return "\n[txpool][warning] {0} transactions found pending in txpool.\n".format(l)
        return "\n[txpool][info] Fine.\n"
