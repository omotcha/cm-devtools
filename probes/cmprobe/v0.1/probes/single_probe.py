#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: omotcha

import os
import sys

# uncomment line below if "module not found" happens
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import subprocess
from statements.statements import probe_statements


def single_probe() -> bool:
    # print("probing...")
    result = subprocess.run(probe_statements, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.stderr:
        # print(result.stderr)
        # print("\n")
        return False
    else:
        # print(result.stdout)
        # print("\n")
        return True


if __name__ == '__main__':
    print(single_probe())
