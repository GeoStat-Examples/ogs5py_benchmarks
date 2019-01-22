# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='colloid_t_root',
    task_id='colloid_t',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'BC_TOP'],
    DIS_TYPE=['CONSTANT', 937.35],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'BC_DOWN'],
    DIS_TYPE=['CONSTANT', 200.0],
)
model.gli.read_file('colloid_t.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 200],
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
    PCS_TYPE='PRESSURE1',
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
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.114476e-11],
    MASS_DISPERSION=[1, 0.005, 0],
    DENSITY=[1, 2000.0],
    CAPILLARY_PRESSURE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
)
model.msh.read_file('colloid_t.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    ELE_GAUSS_POINTS=2,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='FLUID_MOMENTUM',
    ELE_GAUSS_POINTS=2,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
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
    PCS_TYPE='LIQUID_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    RWPT_VALUES='PARTICLES',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=['STEPS', 10],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    APP_TYPE=2,
    COUNT=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='FLUID_MOMENTUM',
    APP_TYPE=2,
    COUNT=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RANDOM_WALK',
    APP_TYPE=2,
    COUNT=1,
)
model.pct.read_file('colloid_t.pct')
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[60, 51],
    TIME_END=3060,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='FLUID_MOMENTUM',
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
