# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='3DRWPTCubTet_root',
    task_id='3DRWPTCubTet',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT6'],
    DIS_TYPE=['CONSTANT', 0],
)
model.gli.read_file('3DRWPTCubTet.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='particles',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
    DECAY=[1, 0.0, 1.0],
    ISOTHERM=[5, 0.01, 0.1, 0.001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    DAT_TYPE='LIQUID',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=10.0,
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.000215811],
    MASS_DISPERSION=[1, 0.005, 0.005],
)
model.msh.read_file('3DRWPTCubTet.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-10, 1000, 1.0, 100, 4],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='FLUID_MOMENTUM',
    ELE_GAUSS_POINTS=2,
    LINEAR_SOLVER=[2, 6, 1e-10, 1000, 1.0, 0, 2],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='GROUNDWATER_FLOW',
    NOD_VALUES=[
        ['HEAD'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    RWPT_VALUES='PARTICLES',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIM_TYPE='STEADY',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='FLUID_MOMENTUM',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RANDOM_WALK',
)
model.pct.read_file('3DRWPTCubTet.pct')
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_START=0.0,
    TIME_END=1000000000.0,
    TIME_STEPS=[120, 864000.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='FLUID_MOMENTUM',
    TIME_START=0.0,
    TIME_END=1000000000.0,
    TIME_STEPS=[120, 864000.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RANDOM_WALK',
    TIME_START=0.0,
    TIME_END=1000000000.0,
    TIME_STEPS=[120, 864000.0],
)
model.write_input()
model.run_model()
