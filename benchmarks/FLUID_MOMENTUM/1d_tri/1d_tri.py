# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='1d_tri_root',
    task_id='1d_tri',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 9810],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT2'],
    DIS_TYPE=['CONSTANT', 9810],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT3'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.gli.read_file('1d_tri.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
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
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-12],
    MASS_DISPERSION=[1, 0.25, 0.5],
    DENSITY=[1, 2000.0],
)
model.msh.read_file('1d_tri.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
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
    NOD_VALUES=[
        ['PRESSURE1'],
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=86400.0,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='FLUID_MOMENTUM',
)
model.rfd.add_block(
    PROJECT=['Benchmark', '1D', 'Transport'],
)
model.rfd.add_block(
    ITERATION_PROPERTIES_CONCENTRATION=[
        [0],
        [0, 1000, 1e-06, 0],
    ],
)
model.rfd.add_block(
    REFERENCE_CONDITIONS=[9.81, 0.0, 101325.0],
)
model.rfd.add_block(
    APRIORI_REFINE_ELEMENT=[0, 0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[1, 86400],
    TIME_END=86400.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='FLUID_MOMENTUM',
    TIME_STEPS=[1, 86400],
    TIME_END=86400.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
