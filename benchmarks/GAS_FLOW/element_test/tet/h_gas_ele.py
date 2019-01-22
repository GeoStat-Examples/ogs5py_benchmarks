# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='h_gas_ele_root',
    task_id='h_gas_ele',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='AIR_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 95500.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='AIR_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT2'],
    DIS_TYPE=['CONSTANT', 95500.0],
)
model.gli.read_file('h_gas_ele.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='AIR_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 101325.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    FLUID_NAME=['CARBON', 'DIOXIDE'],
    DENSITY=7,
    COMPRESSIBILITY=[7, 0, 7, 0, 0],
    VISCOSITY=[1, 1.78e-05],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.005],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.005],
    PERMEABILITY_TENSOR=['ISOTROPIC', 2.77e-19],
)
model.msh.read_file('h_gas_ele.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='AIR_FLOW',
    LINEAR_SOLVER=[2, 6, 1e-15, 100, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 10, 0.0],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='AIR_FLOW',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'OUT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [300.0],
        [3000.0],
        [30000.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    ELE_VALUES=[
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
        ['MASS_FLUX1_X'],
        ['MASS_FLUX1_Y'],
        ['MASS_FLUX1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=4320.0,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='AIR_FLOW',
    NUM_TYPE='NEW',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='AIR_FLOW',
    TIME_STEPS=[100, 300.0],
    TIME_END=30000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
