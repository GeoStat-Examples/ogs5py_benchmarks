# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='2units2faults_root',
    task_id='2units2faults',
    output_dir='out',
)
model.msh.read_file('2units2faults.msh')
model.gli.read_file('2units2faults.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['SURFACE', 'South'],
    EPSILON=0.0001,
    DIS_TYPE=[
        ['LINEAR', 4],
        [0, 40],
        [1, 80],
        [2, 80],
        [3, 40],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'South'],
    EPSILON=0.0001,
    DIS_TYPE=[
        ['LINEAR', 4],
        [0, 2500000.0],
        [1, 2500000.0],
        [2, 1000000.0],
        [3, 1000000.0],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['SURFACE', 'North'],
    EPSILON=0.0001,
    DIS_TYPE=[
        ['LINEAR', 4],
        [4, 2000000.0],
        [5, 2000000.0],
        [6, 500000.0],
        [7, 500000.0],
    ],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1750000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 60],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE='matrix1',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1,
    POROSITY=[1, 0.15],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 7e-10],
    PERMEABILITY_TENSOR=['ISOTROPIC', 2e-14],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE='matrix2',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1,
    POROSITY=[1, 0.08],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 7e-10],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-14],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE='fault1',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.05,
    POROSITY=[1, 1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 4.6e-10],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-08],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    MEDIUM_TYPE='fault1',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=0.05,
    POROSITY=[1, 1],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 4.6e-10],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-09],
    MASS_DISPERSION=[1, 6.0, 1.0],
    DENSITY=[1, 1000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2600.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 1000.0],
        ['CONDUCTIVITY'],
        [1, 3.0],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2600.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 1000.0],
        ['CONDUCTIVITY'],
        [1, 3.0],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1000.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 0],
        ['CONDUCTIVITY'],
        [1, 0.63],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1000.0],
    THERMAL=[
        ['EXPANSION'],
        [6e-06],
        ['CAPACITY'],
        [1, 0],
        ['CONDUCTIVITY'],
        [1, 0.63],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    DAT_TYPE='LIQUID',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 4680.0],
    SPECIFIC_HEAT_CONDUCTIVITY=[1, 0.6],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 2, 1e-10, 3000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 1, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 0, 1e-13, 1000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=2,
    NON_LINEAR_SOLVER=['PICARD', 0.001, 1, 0.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_END=4567884556,
    TIME_START=0,
    TIME_STEPS=[
        [1, 1],
        [1, 2.71],
        [1, 7.2086],
        [1, 18.814446],
        [1, 48.16498176],
        [1, 120.8941042],
        [1, 297.3994964],
        [1, 716.7327863],
        [1, 1691.489376],
        [1, 3907.340458],
        [1, 8830.589434],
        [1, 19515.60265],
        [1, 42153.70172],
        [1, 88944.31064],
        [1, 183225.2799],
        [1, 368282.8126],
        [1, 721834.3127],
        [1, 1378703.537],
        [1, 2564388.579],
        [1, 4641543.329],
        [1, 8169116.259],
        [1, 13969188.8],
        [1, 23188853.41],
        [1, 37334053.99],
        [1, 58241124.23],
        [1, 87944097.58],
        [1, 128398382.5],
        [1, 181041719.3],
        [1, 246216738.2],
        [1, 322543927.1],
        [1, 406405348.1],
        [1, 491750471.2],
        [1, 570430546.6],
        [1, 633177906.8],
        [1, 671168581.2],
        [1, 677880267],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_END=4567884556,
    TIME_START=0,
    TIME_STEPS=[
        [1, 1],
        [1, 2.71],
        [1, 7.2086],
        [1, 18.814446],
        [1, 48.16498176],
        [1, 120.8941042],
        [1, 297.3994964],
        [1, 716.7327863],
        [1, 1691.489376],
        [1, 3907.340458],
        [1, 8830.589434],
        [1, 19515.60265],
        [1, 42153.70172],
        [1, 88944.31064],
        [1, 183225.2799],
        [1, 368282.8126],
        [1, 721834.3127],
        [1, 1378703.537],
        [1, 2564388.579],
        [1, 4641543.329],
        [1, 8169116.259],
        [1, 13969188.8],
        [1, 23188853.41],
        [1, 37334053.99],
        [1, 58241124.23],
        [1, 87944097.58],
        [1, 128398382.5],
        [1, 181041719.3],
        [1, 246216738.2],
        [1, 322543927.1],
        [1, 406405348.1],
        [1, 491750471.2],
        [1, 570430546.6],
        [1, 633177906.8],
        [1, 671168581.2],
        [1, 677880267],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    GEO_TYPE=['POINT', 'POINT15'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    GEO_TYPE=['POINT', 'POINT16'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_Z1'],
    ],
    GEO_TYPE=['POINT', 'POINT17'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
