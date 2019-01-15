# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='HM_root',
    task_id='HM',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'RIGHT'],
    DIS_TYPE=['CONSTANT', 1],
    TIM_TYPE=['CURVE', 1],
    PRESSURE_AS_HEAD=0,
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 0.255],
    PRESSURE_AS_HEAD=[1, 1026],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CONCENTRATION1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 1],
)
model.gli.read_file('HM.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['GRADIENT', 0.25, 0, 9810],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CONCENTRATION1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CONCENTRATION1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 1],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CONCENTRATION1',
    MOBILE=1,
    DIFFUSION=[1, 0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    DENSITY=[3, 1000, 0, 0.026],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1,
    TORTUOSITY=[1, 1],
    POROSITY=[1, 0.385],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.238815e-09],
    PERMEABILITY_SATURATION=10,
    CAPILLARY_PRESSURE=[10, 0.0001, 100],
    MASS_DISPERSION=[1, 0.005, 0.0005],
    STORAGE=10,
)
model.msh.read_file('HM.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    LINEAR_SOLVER=[3, 6, 1e-14, 1000, 1, 100, 4],
    NON_LINEAR_ITERATION=['PICARD', 'ERNORM', 25, 0, 1e-07],
    COUPLING_CONTROL=['ERNORM', 0.005],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 5000, 1, 100, 4],
    COUPLING_CONTROL=['ERNORM', 0.005],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
        ['CONCENTRATION1'],
    ],
    ELE_VALUES=[
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='VTK',
    TIM_TYPE=[
        [9000],
        [19000],
        [29000],
    ],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.rfd.add_block(
    CURVE=[
        [0, 0.267],
        [10000, 0.267],
        [10001, 0.262],
        [20000, 0.262],
        [20001, 0.2655],
        [40000, 0.2655],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_END=30000,
    TIME_START=0.0,
    TIME_CONTROL=[
        ['SELF_ADAPTIVE'],
        ['MULTIPLIER'],
        [3, 1.3],
        [5, 1.01],
        [7, 0.8],
        [9, 0.5],
        ['MIN_TIME_STEP'],
        [0.001],
        ['MAX_TIME_STEP'],
        [10000],
        ['INITIAL_STEP_SIZE'],
        [10.0],
        ['ITERATIVE_TYPE'],
        ['COUPLED'],
        ['STAY'],
        [3],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_END=30000,
    TIME_START=0.0,
    TIME_CONTROL=[
        ['SELF_ADAPTIVE'],
        ['MULTIPLIER'],
        [3, 1.3],
        [5, 1.01],
        [7, 0.8],
        [9, 0.5],
        ['MIN_TIME_STEP'],
        [0.001],
        ['MAX_TIME_STEP'],
        [10000],
        ['INITIAL_STEP_SIZE'],
        [10.0],
        ['ITERATIVE_TYPE'],
        ['COUPLED'],
        ['STAY'],
        [3],
    ],
)
model.write_input()
model.run_model()
