# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='H2_Permeability_GasPressure_root',
    task_id='H2_Permeability_GasPressure',
    output_dir='out',
)
model.msh.read_file('H2_Permeability_GasPressure.msh')
model.gli.read_file('H2_Permeability_GasPressure.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NUM_TYPE='NEW',
)
model.rfd.read_file('H2_Permeability_GasPressure.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'PLY_1'],
    DIS_TYPE=['CONSTANT', 101325],
    TIM_TYPE=['CURVE', 2],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'PLY_3'],
    DIS_TYPE=['CONSTANT', 101325],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1875000],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 101325],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    POROSITY=[1, 0.16],
    PERMEABILITY_TENSOR=['ORTHOTROPIC', 3e-17, 3e-18],
    PERMEABILITY_FUNCTION_PRESSURE=[10, 3],
    PERMEABILITY_SATURATION=[
        [4, 0.5, 1, 0.5],
        [44, 0, 0.5, 0.5],
    ],
    CAPILLARY_PRESSURE=[4, 0.003924],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='PRESSURE2',
    DENSITY=[2, 1.2, 101325, 1.189e-05],
    VISCOSITY=[1, 1.6e-05],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    LINEAR_SOLVER=[2, 0, 1e-15, 10000, 1, 100, 4],
    ELE_UPWINDING=[0, 1.0],
    ELE_MASS_LUMPING=1,
    ELE_GAUSS_POINTS=3,
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 1000, 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_STEPS=[
        [1, 1000],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
        [1, 1],
        [1, 999],
    ],
    TIME_END=10000,
    TIME_START=0,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
