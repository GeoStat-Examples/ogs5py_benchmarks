# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='HBr_10C_Diff_new_root',
    task_id='HBr_10C_Diff_new',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 283.15],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 283.15],
)
model.gli.read_file('HBr_10C_Diff_new.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'PLY_Model_Area'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TRACER',
    GEO_TYPE=['POLYLINE', 'PLY_CLEAN'],
    DIS_TYPE=['CONSTANT', 1e-10],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='TRACER',
    GEO_TYPE=['POLYLINE', 'PLY_TRACER'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'PLY_Model_Area'],
    DIS_TYPE=['CONSTANT', 283.15],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='TRACER',
    MOBILE=1,
    DIFFUSION=[10, -0.88166, -1079.3],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 999.7],
    VISCOSITY=[1, 0.0013],
    THERMAL=[
        ['CAPACITY'],
        [1, 0.004192],
        ['CONDUCTIVITY'],
        [1, 0.587],
    ],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.45],
    TORTUOSITY=[1, 0.45],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 0.0028935],
    DENSITY=[1, 2650.0],
    MASS_DISPERSION=[1, 0.0001, 5e-05],
    HEAT_DISPERSION=[1, 0.0001, 5e-05],
)
model.msh.read_file('HBr_10C_Diff_new.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650.0],
    THERMAL=[
        ['EXPANSION:'],
        [0.0],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY'],
        [1, 3.2],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-10, 1000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-10, 10000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-10, 10000, 1.0, 1, 2],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['TRACER'],
        ['TEMPERATURE1'],
    ],
    GEO_TYPE=['POLYLINE', 'PLY_Model_Area'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 200],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['TRACER'],
        ['TEMPERATURE1'],
    ],
    GEO_TYPE=['POINT', 'POINT1'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 5],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['TRACER'],
    ],
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 5],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
    BOUNDARY_CONDITION_OUTPUT=[],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    TEMPERATURE_UNIT='KELVIN',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[4900, 432.0],
    TIME_END=8.64e+39,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[4900, 432],
    TIME_END=8.64e+39,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[4900, 432],
    TIME_END=8.64e+39,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
