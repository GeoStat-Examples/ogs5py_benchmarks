# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='Heatpipe_root',
    task_id='Heatpipe',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 152780.14062],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 305527.21875],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 101300.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 166757.89062],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 68.6],
)
model.gli.read_file('Heatpipe.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 152780.14062],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 101300],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 68.6],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000],
    VISCOSITY=[1, 0.001],
    SPECIFIC_HEAT_CAPACITY=[1, 4218.0],
    HEAT_CONDUCTIVITY=[1, 0.6],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='PRESSURE2',
    DENSITY=7,
    VISCOSITY=[1, 1.1e-05],
    SPECIFIC_HEAT_CAPACITY=[1, 1180.0],
    HEAT_CONDUCTIVITY=[1, 0.016],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    POROSITY=[1, 0.35],
    DIFFUSION=273,
    EVAPORATION=[647, 100, 0.2963869693978282],
    TORTUOSITY=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-13],
    PERMEABILITY_SATURATION=[
        [6, 0, 1, 2],
        [66, 0, 1, 2, 1e-19],
    ],
    CAPILLARY_PRESSURE=[6, 136650.7228084974],
)
model.msh.read_file('Heatpipe.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650.0],
    THERMAL=[
        ['EXPANSION:', 1e-05],
        ['CAPACITY:'],
        [1, 1291.0],
        ['CONDUCTIVITY:'],
        [1, 2.5],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    ELE_MASS_LUMPING=1,
    ELE_GAUSS_POINTS=1,
    LINEAR_SOLVER=[2, 6, 1e-12, 2000, 1, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 25, 1],
    COUPLING_CONTROL=['LMAX', 0.001],
    COUPLED_PROCESS=['HEAT_TRANSPORT', 1, 1],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    ELE_MASS_LUMPING=1,
    ELE_GAUSS_POINTS=1,
    LINEAR_SOLVER=[2, 6, 1e-12, 2000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 25, 1.0],
    COUPLING_CONTROL=['LMAX', 0.001],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['TEMPERATURE1'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE=['POLYLINE', 'Profile'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 5],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    NUM_TYPE='NEW',
)
model.rfd.read_file('Heatpipe.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 100],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_CONTROL=[
        ['PI_AUTO_STEP_SIZE'],
        [1, 0.001, 1e-09, 0.01],
    ],
    TIME_END=1e+100,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_CONTROL=[
        ['PI_AUTO_STEP_SIZE'],
        [1, 0.001, 1e-09, 0.01],
    ],
    TIME_END=1e+100,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
