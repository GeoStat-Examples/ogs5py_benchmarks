# -*- coding: utf-8 -*-
"""
Walk all ogs5 benchmarks
"""
from __future__ import print_function
import os
import zipfile
import urllib.request
from shutil import rmtree
from ogs5py import OGS, search_task_id


def download_benchmarks(zip_dir):
    print("Downloading OGS5 Benchmarks")
    data_filename = "data.zip"
    data_url = "https://github.com/ufz/ogs5-benchmarks/archive/master.zip"
    urllib.request.urlretrieve(data_url, data_filename)
    # extract the data
    print("Extracting OGS5 Benchmarks")
    with zipfile.ZipFile(data_filename, "r") as zf:
        zf.extractall(zip_dir)


# set directories
out_dir = os.path.join(os.getcwd(), "benchmarks")
zip_dir = os.path.join(os.getcwd(), "ogs5_benchmarks_raw")
download_benchmarks(zip_dir)
rootdir = os.path.join(zip_dir, "ogs5-benchmarks-master")
# skip some tasks
skip_dirs = [
    "HT_EOS",  # .bat files to copy stuff... uarg.. (maybe rewrite with ogs5py)
    ".git",  # ignore git config dir
]
skip_task = [
    "2d_h_us_line_Warrick",  # lonesome mmp
    "model_1",  # $AREA keyword in POINTS --> not in GUI/HM but repeated key
    "bact_growth_new",  # #THERMAL in mfp
    "thm_quad",  # $STORATIVITY in mmp
    "HT_var_density_1D",  # $AREA in mmp
    "viscosity_yaws",  # $AREA in mmp
    "uc_pris",  # GLI not valid (SRF not present for VOLUME)
    "brand_m1_l1",  # GLI not valid (TIN and Polylines at the same time[?])
    # repeated Keywords ... ogs5py can't handle this
    "lag2d",  # repeated Keywords NEIGHBOR (cct)
    "decal",  # repeated Keywords NEIGHBOR (cct)
#    "2D1P_transport",  # repeated Keywords POROSITY (mmp)
#    "Nuklidtransport",  # repeated Keywords MASS_DISPERSION (mmp)
#    "cement2d",  # repeated Keywords KINETIC_GEM (gem)
#    "model_1",  # repeated Keywords DAT_TYPE (out)
#    "Leakage",  # repeated Keywords TIM_TYPE (out)
#    "CO2-FLOW",  # repeated Keywords DAT_TYPE (out)
#    "2pf_2pt",  # repeated Keywords SIMULATOR (pcs)
]

# search for all root folders
roots = []
for dirpath, dirnames, filenames in os.walk(rootdir):
    # print path to all subdirectories first.
    for skip in skip_dirs:
        if skip in dirnames:
            # don't go into any skip directories.
            dirnames.remove(skip)
    for subdirname in dirnames:
        roots.append(os.path.join(dirpath, subdirname))
root_cnt = len(roots)
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
skip_run = ["Heatpipe"]  # takes for ever...
skip_dir_run = []

# if it failed at some point, you can provide the last used task_id
last_id_used = ""
if last_id_used:
    found_last_id = False
else:
    found_last_id = True

for num_root, root in enumerate(roots):
    if num_root < start_test:
        continue
    found_ids = search_task_id(root, (".pcs"))
    use_ids = [found for found in found_ids if found not in set(skip_task)]
    for num_id, task_id in enumerate(use_ids):

        if not found_last_id and task_id != last_id_used:
            print("skip before last_id_used: " + task_id)
            continue
        elif not found_last_id:
            print("found last_id_used: " + task_id)
            found_last_id = True
            continue

        test_cnt += 1
        if use_old_dir:
            tmp_root = root[len(rootdir) + 1 :]
        else:
            tmp_root = (
                "test_{:03}".format(test_cnt)
                + "_"
                + str(num_root + 1)
                + "-"
                + str(root_cnt)
                + "_"
                + str(num_id + 1)
                + "-"
                + str(len(use_ids))
            )

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

        model = OGS(
            task_root=os.path.join(out_dir, tmp_root), output_dir="out"
        )
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
                ogs_name="ogs", print_log=False  # in sys-path
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
