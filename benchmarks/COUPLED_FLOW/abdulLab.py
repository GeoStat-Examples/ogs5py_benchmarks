# -*- coding: utf-8 -*-
from __future__ import division, print_function
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
model.rfd.add_block(
    PROJECT='Woolhiser',
)
model.rfd.add_block(
    CURVE=[
        [0, 1.2e-05],
        [1200, 1.2e-05],
        [1200.01, 0],
        [1500, 0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.24, 12000],
        [0.3, 10000],
        [0.45, 6500],
        [0.6, 6000],
        [0.75, 5800],
        [0.9, 5000],
        [1, 3000],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0, 0],
        [0.01, 1e-09],
        [0.02, 2.26274e-08],
        [0.03, 1.40296e-07],
        [0.04, 5.12e-07],
        [0.05, 1.39754e-06],
        [0.06, 3.17454e-06],
        [0.07, 6.35245e-06],
        [0.08, 1.15852e-05],
        [0.09, 1.9683e-05],
        [0.1, 3.16228e-05],
        [0.11, 4.85587e-05],
        [0.12, 7.18316e-05],
        [0.13, 0.000102978],
        [0.14, 0.00014374],
        [0.15, 0.00019607],
        [0.16, 0.000262144],
        [0.17, 0.000344366],
        [0.18, 0.000445375],
        [0.19, 0.000568056],
        [0.2, 0.000715542],
        [0.21, 0.000891224],
        [0.22, 0.001098758],
        [0.23, 0.00134207],
        [0.24, 0.001625364],
        [0.25, 0.001953125],
        [0.26, 0.00233013],
        [0.27, 0.002761448],
        [0.28, 0.003252454],
        [0.29, 0.003808825],
        [0.3, 0.004436553],
        [0.31, 0.005141947],
        [0.32, 0.005931642],
        [0.33, 0.006812597],
        [0.34, 0.007792111],
        [0.35, 0.008877817],
        [0.36, 0.010077696],
        [0.37, 0.011400076],
        [0.38, 0.012853642],
        [0.39, 0.014447434],
        [0.4, 0.016190862],
        [0.41, 0.018093699],
        [0.42, 0.020166095],
        [0.43, 0.022418577],
        [0.44, 0.024862056],
        [0.45, 0.027507829],
        [0.46, 0.030367584],
        [0.47, 0.033453407],
        [0.48, 0.036777785],
        [0.49, 0.040353607],
        [0.5, 0.044194174],
        [0.51, 0.048313199],
        [0.52, 0.052724813],
        [0.53, 0.057443569],
        [0.54, 0.062484445],
        [0.55, 0.067862851],
        [0.56, 0.073594629],
        [0.57, 0.07969606],
        [0.58, 0.086183866],
        [0.59, 0.093075216],
        [0.6, 0.100387728],
        [0.61, 0.108139475],
        [0.62, 0.116348986],
        [0.63, 0.125035252],
        [0.64, 0.134217728],
        [0.65, 0.14391634],
        [0.66, 0.154151484],
        [0.67, 0.164944034],
        [0.68, 0.176315343],
        [0.69, 0.188287248],
        [0.7, 0.200882072],
        [0.71, 0.21412263],
        [0.72, 0.22803223],
        [0.73, 0.242634677],
        [0.74, 0.25795428],
        [0.75, 0.27401585],
        [0.76, 0.290844707],
        [0.77, 0.308466683],
        [0.78, 0.326908123],
        [0.79, 0.346195892],
        [0.8, 0.366357377],
        [0.81, 0.387420489],
        [0.82, 0.409413667],
        [0.83, 0.432365881],
        [0.84, 0.456306639],
        [0.85, 0.481265983],
        [0.86, 0.507274499],
        [0.87, 0.534363317],
        [0.88, 0.562564114],
        [0.89, 0.591909118],
        [0.9, 0.622431112],
        [0.91, 0.654163435],
        [0.92, 0.687139988],
        [0.93, 0.721395234],
        [0.94, 0.756964201],
        [0.95, 0.793882491],
        [0.96, 0.832186275],
        [0.97, 0.8719123],
        [0.98, 0.913097893],
        [0.99, 0.955780962],
        [1, 1],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0, 7.272e-07],
        [119009.9, 7.272e-07],
        [120000, 0],
        [150000, 0],
    ],
)
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
