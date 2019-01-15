# -*- coding: utf-8 -*-
"""
run all ogs5py benchmarks
"""
import sys
import os
import fnmatch
import time
from pexpect.popen_spawn import PopenSpawn
import pexpect
from ogs5py.tools.tools import Output

# pexpect.spawn just runs on unix-like systems
if sys.platform == "win32":
    CmdRun = PopenSpawn
else:
    CmdRun = pexpect.spawn


def call_script(script, output, timeout=3):
    cwd, script_file = os.path.split(script)
    args = [sys.executable, "-u", script_file]
    try:
        child = CmdRun(
            " ".join(args), timeout=timeout, logfile=output, cwd=cwd
        )
        # wait for ogs to finish
        child.expect(pexpect.EOF)
    except pexpect.TIMEOUT:
        output.write("...timeout\n".encode())


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


if __name__ == "__main__":
    timeout = 3  # None for no timeout
    out_dir = os.path.join(os.getcwd(), "benchmarks")
    scripts = find("*.py", out_dir)
    log_name = os.path.join(
        out_dir, "run_log_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    )
    output = Output(log_name, print_log=True)

    for script in scripts:
        print(script)
        call_script(script, output, timeout=timeout)

    output.close()
