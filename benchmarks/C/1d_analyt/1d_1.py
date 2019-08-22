# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='1d_1_root',
    task_id='1d_1',
    output_dir='out',
)
model.msh.read_file('1d_1.msh')
model.gli.read_file('1d_1.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=1,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=1,
)
model.rfd.read_file('1d_1.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE:', 'LEFTSURF'],
    DIS_TYPE=['CONSTANT:', 2.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE:', 'RIGHTSURF'],
    DIS_TYPE=['CONSTANT:', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Decay',
    GEO_TYPE=['SURFACE:', 'LEFTSURF'],
    DIS_TYPE=['CONSTANT:', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='SorbLin',
    GEO_TYPE=['SURFACE:', 'LEFTSURF'],
    DIS_TYPE=['CONSTANT:', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='DecaySorbnonlin',
    GEO_TYPE=['SURFACE:', 'LEFTSURF'],
    DIS_TYPE=['CONSTANT:', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['SURFACE:', 'LEFTSURF'],
    DIS_TYPE=['CONSTANT:', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Decay',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='SorbLin',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='DecaySorbnonlin',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE', 'RIGHTSURF'],
    DIS_TYPE=['CONSTANT_NEUMANN', 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.5],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.0005787037],
    MASS_DISPERSION=[1, 0.25, 0.25],
    DENSITY=[1, 2000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Decay',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
    DECAY=[1, 1e-07, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='SorbLin',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
    ISOTHERM=[2, 0.001, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='DecaySorbnonlin',
    MOBILE=1,
    DIFFUSION=[1, 3e-09],
    DECAY=[2, 1e-07, 0.1],
    ISOTHERM=[3, 0.001, 0.5],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='ConsTracer',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='FLUID_MOMENTUM',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 0.5, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[100, 86400.0],
    TIME_END=8640000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[100, 86400.0],
    TIME_END=8640000.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['Decay'],
        ['SorbLin'],
        ['DecaySorbnonlin'],
        ['ConsTracer'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT_LINE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [86400],
        [2160000],
        [4320000],
        [6480000],
        [8640000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['Decay'],
        ['SorbLin'],
        ['DecaySorbnonlin'],
        ['ConsTracer'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [86400],
        [2160000],
        [4320000],
        [6480000],
        [8640000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['Decay'],
        ['SorbLin'],
        ['DecaySorbnonlin'],
        ['ConsTracer'],
    ],
    GEO_TYPE=['POINT', 'POINT8'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
