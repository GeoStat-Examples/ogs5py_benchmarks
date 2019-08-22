# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='HT_var_density_1D_root',
    task_id='HT_var_density_1D',
    output_dir='out',
)
model.msh.read_file('HT_var_density_1D.msh')
model.gli.read_file('HT_var_density_1D.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    TEMPERATURE_UNIT='KELVIN',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.read_file('HT_var_density_1D.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 101000],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 100000],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 400],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 100000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 300],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.01],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2850],
    THERMAL=[
        ['EXPANSION'],
        [1e-05],
        ['CAPACITY'],
        [1, 1000.0],
        ['CONDUCTIVITY'],
        [1, 3.2],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[4, 1000, 300, -0.001],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 4000.0],
    HEAT_CONDUCTIVITY=[1, 0.6],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 2, 1e-16, 1000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 25, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 0, 1e-12, 1000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=2,
    NON_LINEAR_SOLVER=['PICARD', 0.001, 25, 0.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[50, 100000],
    TIME_END=1e+99,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[50, 100000],
    TIME_END=1e+99,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['TEMPERATURE1'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
