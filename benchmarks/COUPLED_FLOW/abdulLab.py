# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='abdulLab_root',
    task_id='abdulLab',
    output_dir='out',
)
model.gli.read_file('abdulLab.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['GRADIENT', 0.9, 0, 9810],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.9],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1e-06],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.34],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5.1e-12],
    PERMEABILITY_SATURATION=[4, 0.0, 1.0, 0.8],
    CAPILLARY_PRESSURE=[4, 2.4],
    MASS_DISPERSION=[1, 0.0, 0.0],
    TORTUOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.0],
    STORAGE=[1, 0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5e-05],
    MASS_DISPERSION=[1, 0.0, 0.0],
    TORTUOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    SURFACE_FRICTION=[5.39, 0.5, 0.66667],
    RILL=[0.0005, 0.00025],
    WIDTH=1.0,
    POROSITY=[1, 1.0],
    MASS_DISPERSION=[1, 0.0, 0.0],
    TORTUOSITY=[1, 0.001],
)
model.msh.read_file('abdulLab.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 0.1, 20, 0.0],
    ELE_GAUSS_POINTS=3,
    COUPLING_CONTROL=['LMAX', 1.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='OVERLAND_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-10, 1000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['NEWTON', 1e-05, 1e-08, 100, 0.0],
    ELE_GAUSS_POINTS=2,
    COUPLING_CONTROL=['LMAX', 1.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    LINEAR_SOLVER=[2, 1, 1e-12, 1000, 1.0, 1, 2],
    COUPLING_CONTROL=['LMAX', 1.0],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    MSH_TYPE='HEAD',
    NOD_VALUES='FLUX',
    GEO_TYPE=['POINT', 'POINT0'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS:', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
    PRIMARY_VARIABLE='PRESSURE1',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='OVERLAND_FLOW',
    NUM_TYPE='NEW',
    PRIMARY_VARIABLE='HEAD',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
    PRIMARY_VARIABLE='HEAD',
)
model.rfd.read_file('abdulLab.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'SURFACE'],
    DIS_TYPE=['CONSTANT_NEUMANN', 1],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=[
        ['CRITICALDEPTH', 1],
        [0.0005],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'WATER_TABLE'],
    DIS_TYPE=[
        ['CONSTANT_NEUMANN', 1.0],
        ['PCS', 'RICHARDS_FLOW'],
        ['PRESSURE1'],
        [0.0005, 0.01],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'WATER_TABLE'],
    DIS_TYPE=[
        ['CONSTANT_NEUMANN', 1],
        ['PCS', 'GROUNDWATER_FLOW'],
        ['HEAD'],
        [0.0005, 0.01],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'SURFACE'],
    DIS_TYPE=[
        ['CONSTANT_NEUMANN', 1],
        ['PCS', 'RICHARDS_FLOW'],
        ['PRESSURE1'],
        [0.1, 0.0005],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'SURFACE'],
    DIS_TYPE=[
        ['CONSTANT_NEUMANN', 1],
        ['PCS', 'OVERLAND_FLOW'],
        ['HEAD'],
        [0.1, 0.0005],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_END=420,
    TIME_START=0.0,
    TIME_STEPS=[30000, 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='OVERLAND_FLOW',
    TIME_END=420,
    TIME_START=0.0,
    TIME_STEPS=[30000, 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_END=420,
    TIME_START=0.0,
    TIME_STEPS=[30000, 1],
)
model.write_input()
model.run_model()
