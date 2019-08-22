# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='h_frac_line2D_root',
    task_id='h_frac_line2D',
    output_dir='out',
)
model.msh.read_file('h_frac_line2D.msh')
model.gli.read_file('h_frac_line2D.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.read_file('h_frac_line2D.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=[
        ['LINEAR', 2],
        [1, 10000.0],
        [2, 100000.0],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    GEO_TYPE=['SURFACE', 'SURFACE0'],
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-12],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 0.0],
    VISCOSITY=[1, 0.001],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-14, 1000, 1.0, 100, 4],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[1, 86400.0],
    TIME_END=86400.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='VTK',
    TIM_TYPE=86400.0,
)
model.write_input()
model.run_model()
