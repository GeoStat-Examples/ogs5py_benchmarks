# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='h_tri_root',
    task_id='h_tri',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', 20000.0],
)
model.ddc.add_block(
    main_key='DOMAIN',
    ELEMENTS=[
        [9],
        [11],
        [16],
        [17],
        [18],
    ],
    NODES_INNER=[
        [6],
        [11],
        [10],
        [12],
        [16],
        [15],
    ],
)
model.ddc.add_block(
    main_key='DOMAIN',
    ELEMENTS=[
        [0],
        [1],
        [2],
        [8],
    ],
    NODES_INNER=[
        [0],
        [6],
        [5],
        [1],
        [2],
        [10],
    ],
)
model.ddc.add_block(
    main_key='DOMAIN',
    ELEMENTS=[
        [14],
        [15],
        [19],
        [21],
        [22],
        [23],
    ],
    NODES_INNER=[
        [8],
        [9],
        [14],
        [13],
        [12],
        [17],
        [16],
        [18],
        [19],
    ],
)
model.ddc.add_block(
    main_key='DOMAIN',
    ELEMENTS=[
        [5],
        [10],
        [12],
        [13],
        [20],
    ],
    NODES_INNER=[
        [2],
        [8],
        [7],
        [6],
        [12],
        [13],
        [18],
    ],
)
model.ddc.add_block(
    main_key='DOMAIN',
    ELEMENTS=[
        [3],
        [4],
        [6],
        [7],
    ],
    NODES_INNER=[
        [2],
        [7],
        [6],
        [3],
        [8],
        [4],
        [9],
    ],
)
model.gli.read_file('h_tri.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 0.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    GEO_TYPE=['SURFACE', 'SURFACE0'],
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-12],
)
model.msh.read_file('h_tri.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-14, 1000, 1.0, 100, 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=86400.0,
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.add_block(
    PROJECT=[
        ['Triangle', 'elements', 'for', 'flow'],
        ['Test', 'of', 'OUT', 'method', 7],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[1, 86400.0],
    TIME_END=86400.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
