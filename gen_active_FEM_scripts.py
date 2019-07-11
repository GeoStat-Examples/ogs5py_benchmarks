# -*- coding: utf-8 -*-
"""
Walk all ogs5 benchmarks
"""
from __future__ import print_function
import os
import csv
import zipfile
import urllib.request
from shutil import rmtree
from ogs5py import OGS


def download_benchmarks(zip_dir):
    print("Downloading OGS5 Benchmarks")
    data_filename = "data.zip"
    data_url = "https://github.com/ufz/ogs5-benchmarks/archive/master.zip"
    urllib.request.urlretrieve(data_url, data_filename)
    # extract the data
    print("Extracting OGS5 Benchmarks")
    with zipfile.ZipFile(data_filename, "r") as zf:
        zf.extractall(zip_dir)


# get all FEM models which have an active benchmark check
with open('active_names.csv') as csvfile:
    active_names = csv.reader(csvfile)
    use_names = []
    for row in active_names:
        if row[0] == 'Linux-FEM':
            # get rid of the authors initials
            use_names.append("_".join(row[1].split("_")[1:]))

# set directories
out_dir = os.path.join(os.getcwd(), "benchmarks_FEM_active")
zip_dir = os.path.join(os.getcwd(), "ogs5_benchmarks_raw")
download_benchmarks(zip_dir)
rootdir = os.path.join(zip_dir, "ogs5-benchmarks-master")

FAIL = []
FAIL_OK = []
log_str = []
test_cnt = 0
start_test = 0

# GENERATION SETTINGS
use_old_dir = True
run = False
write_files = False
gen_scr = True
print_progress = True

# skip some runs
skip_run = []  # takes for ever...
skip_dir_run = []

for name in use_names:
    test_cnt += 1
    relative_root, task_id = os.path.split(name)
    root = os.path.join(rootdir, relative_root)
    if use_old_dir:
        tmp_root = relative_root
    else:
        tmp_root = ("test_{:03}".format(test_cnt) + "_model")

    tmp_log = (
        str(test_cnt)
        + " "
        + tmp_root
        + " - load: "
        + os.path.join(root, task_id)
    )
    log_str.append(tmp_log)

    if print_progress:
        print(tmp_log)

    model = OGS(task_root=os.path.join(out_dir, tmp_root), output_dir="out")
    load_success = False
    try:
        model.load_model(
            verbose=False,
            task_root=root,
            task_id=task_id,
            encoding="ISO-8859-15",  # lots of windows files (non utf8)
            use_task_id=True,  # use the given task_id for some reference
        )
    except ValueError as valerr:
        print("FAIL..." + str(valerr))
        log_str.append("FAIL..." + str(valerr))
    else:
        load_success = True
        print("OK...loading successfull")
        log_str.append("OK...loading successfull")

    if gen_scr and load_success:
        model.gen_script(
            script_name=model.task_id + ".py",
            script_dir=model.task_root,
            task_root=task_id + "_root",
            output_dir="out",
            separate_files=["ddc", "rfd"]
        )

    model.task_root = os.path.join(model.task_root, task_id + "_root")
    if write_files and load_success:
        model.write_input()

    skip_this_run = task_id in skip_run
    skip_this_run |= any([s_dir in root for s_dir in skip_dir_run])
    skip_this_run |= not model.pqc.is_empty  # skip phreeqc
    skip_this_run |= not model.gem.is_empty  # skip gem
    skip_this_run |= not model.ddc.is_empty  # skip mpi

    if run and load_success and not skip_this_run:
        success = model.run_model(
            ogs_name="ogs", print_log=False
        )
        if success:
            tmp_log = "....OK"
        else:
            FAIL.append(os.path.join(root, task_id))
            tmp_log = "..FAIL"
            model.output_dir = os.path.abspath(
                os.path.join(model.task_root, "out_ori")
            )
            model.task_root = root
            ori_succ = model.run_model(
                ogs_name="ogs", print_log=False  # in sys-path
            )
            if ori_succ:
                tmp_log += " ..original OK"
                FAIL[-1] = " (original OK)" + FAIL[-1]
                FAIL_OK.append(os.path.join(root, task_id))
            else:
                tmp_log += " ..original FAIL"
            log_str.append(tmp_log)
        print(tmp_log)
    elif run and load_success:
        print("run skip " + task_id)

# save some logs
if run:
    with open(os.path.join(out_dir, "FAIL.txt"), "w") as outfile:
        for line in FAIL:
            print(line, file=outfile)

    with open(os.path.join(out_dir, "FAIL_OK.txt"), "w") as outfile:
        for line in FAIL_OK:
            print(line, file=outfile)

with open(os.path.join(out_dir, "LOG.txt"), "w") as outfile:
    for line in log_str:
        print(line, file=outfile)

# cleanup
print("Removing OGS5 Benchmarks")
os.remove("data.zip")
rmtree(zip_dir)
