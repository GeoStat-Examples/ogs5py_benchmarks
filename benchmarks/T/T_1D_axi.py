# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='T_1D_axi_root',
    task_id='T_1D_axi',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT2'],
    DIS_TYPE=['CONSTANT', 25],
)
model.gli.read_file('T_1D_axi.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 25],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 0.0],
    VISCOSITY=[1, 0.0],
    SPECIFIC_HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
)
model.msh.read_file('T_1D_axi.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[
        [1, 2000.0],
        ['CAPACITY'],
        [1, 900],
        ['CONDUCTIVITY'],
        [1, 5.5],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 1, 1e-12, 1000, 0.5, 100, 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    TEMPERATURE_UNIT='KELVIN',
)
model.rfd.add_block(
    PROJECT=['HEAT', 'TRANSPORT', '1D', 'axisymmetric'],
)
model.rfd.add_block(
    REFERENCE_CONDITIONS=[9.81, 293, 101325],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT_NEUMANN', 30],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[100, 1000],
    TIME_END=100000,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
