# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='h_frac_root',
    task_id='h_frac',
    output_dir='out',
)
model.msh.read_file('h_frac.msh')
model.gli.read_file('h_frac.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    NUM_TYPE='NEW',
)
model.rfd.read_file('h_frac.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
)
model.bc.append_to_block(
    PRIMARY_VARIABLE='PRESSURE1',
)
model.bc.append_to_block(
    GEO_TYPE=['POLYLINE', 'TOP'],
)
model.bc.append_to_block(
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.bc.append_to_block(
    TIME_INTERVAL=[0.0, 100.0],
)
model.bc.append_to_block(
    TIME_INTERVAL=[100.0, 4320.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
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
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-10, 1000, 1.0, 1, 2],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[200, 4320.0],
    TIME_END=4320.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='LIQUID_FLOW',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='LIQUID_FLOW',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'RIGHT_S'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [1.0],
        [10.0],
        [100.0],
        [1000.0],
        [10000.0],
        [100000.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='LIQUID_FLOW',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'RIGHT_V'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [1.0],
        [10.0],
        [100.0],
        [1000.0],
        [10000.0],
        [100000.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT4'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
