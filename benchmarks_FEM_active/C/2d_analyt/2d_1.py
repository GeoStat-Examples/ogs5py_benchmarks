# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='2d_1_root',
    task_id='2d_1',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE', 'CaesarSURF'],
    DIS_TYPE=['CONSTANT', 2.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE', 'DorisSURF'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POLYLINE', 'Emil'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POLYLINE', 'Franz'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE=['POLYLINE', 'Anton'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.gli.read_file('2d_1.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.95],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='ConsTracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='ConsTracer',
    MOBILE=1,
    DIFFUSION=[1, 1e-09],
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
model.msh.read_file('2d_1.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
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
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['ConsTracer'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT1'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [1728000.0],
        [3456000.0],
        [5184000.0],
        [6912000.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['ConsTracer'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT2'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [1728000.0],
        [3456000.0],
        [5184000.0],
        [6912000.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['ConsTracer'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=6912000,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.rfd.read_file('2d_1.rfd')
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[160, 43200.0],
    TIME_END=72000000000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[160, 43200.0],
    TIME_END=720000000000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
