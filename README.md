Welcome to the ogs5py benchmarks
================================

Purpose
-------
Most of the OGS5 benchmarks were rewritten into a ogs5py-script in this repository.

The following were skipped:

+ `HT_EOS`   (folder) \*.bat files to copy stuff... uarg.. (maybe rewrite with ogs5py)
+ `bact_growth_new`    #THERMAL in mfp
+ `HT_var_density_1D`    $AREA in mmp
+ `thm_quad`    $STORATIVITY in mmp
+ `viscosity_yaws`    $AREA in mmp
+ `uc_pris`    GLI not valid (SRF not present for VOLUME)
+ `brand_m1_l1`    GLI not valid (TIN and Polylines at the same time[?])
+ `2d_h_us_line_Warrick`    lonesome mmp

The following benchmarks have multiple sub keywords in some files, which is
not convertable to a ogs5py script at the moment. Therefore the following are skipped as well:

+ `lag2d`    repeated NEIGHBOR (cct)
+ `decal`    repeated NEIGHBOR (cct)
+ `2D1P_transport`    repeated POROSITY (mmp)
+ `Nuklidtransport`    repeated MASS_DISPERSION (mmp)
+ `cement2d`    repeated KINETIC_GEM (gem)
+ `model_1`    repeated DAT_TYPE (out)
+ `Leakage`    repeated TIM_TYPE (out)
+ `CO2-FLOW`    repeated DAT_TYPE (out)
+ `2pf_2pt`    repeated SIMULATOR (pcs)


Generation
----------

+ The scripts were generated with the python script
      gen_benchmark_scripts.py
+ You can run all generated scripts for testing with the python script
      run_ogs5py_scripts.py


Created January 2019, Copyright Sebastian Müller 2019
