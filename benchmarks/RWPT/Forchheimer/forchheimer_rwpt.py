# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='forchheimer_rwpt_root',
    task_id='forchheimer_rwpt',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'BC_TOP'],
    DIS_TYPE=['CONSTANT', 0.09555],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'BC_DOWN'],
    DIS_TYPE=['CONSTANT', 0.02038],
)
model.gli.read_file('forchheimer_rwpt.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.02038],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='particles',
    MOBILE=1,
    DIFFUSION=[1, 0.0],
    DECAY=[1, 5.2, 1.0],
    ISOTHERM=[5, 0.9, 0.1, 0.001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.42],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.00010933],
    MASS_DISPERSION=[1, 0.005, 0],
    DENSITY=[1, 2000.0],
    CAPILLARY_PRESSURE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.5],
    FLOWLINEARITY=[5, 100000000.0],
)
model.msh.read_file('forchheimer_rwpt.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
    COUPLING_CONTROL=['LMAX', 0.001],
    LOCAL_PICARD1=[200, 1e-10],
    NON_LINEAR_UPDATE_VELOCITY=1,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RANDOM_WALK',
    NOD_VALUES='leavingParticles',
    GEO_TYPE=['POINT', 'BC_DOWN'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_VALUES=[
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
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
    COUNT=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RANDOM_WALK',
    COUNT=1,
)
model.pct.read_file('forchheimer_rwpt.pct')
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[60, 51],
    TIME_END=3060,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RANDOM_WALK',
    TIME_STEPS=[60, 51],
    TIME_END=3060,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
