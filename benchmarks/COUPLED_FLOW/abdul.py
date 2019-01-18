# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS, GLIext

model = OGS(
    task_root='abdul_root',
    task_id='abdul',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT8'],
    DIS_TYPE=['CONSTANT', 3.0586544],
)
model.gli.read_file('abdul.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0001],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['GRADIENT', 0, 0, 9810],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='HEAD',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEO_TYPE=['SURFACE:', 'SURFACE0'],
    SURFACE_FRICTION=[6.67, 0.5, 0.667],
    RILL=[0.001, 0.0001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    POROSITY=[1, 0.2],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.33],
    PERMEABILITY_TENSOR=['ISOTROPIC', 2.95e-13],
    PERMEABILITY_SATURATION=[4, 0, 1.0, 0.336],
    CAPILLARY_PRESSURE=[4, 1.43],
)
model.msh.read_file('abdul.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='OVERLAND_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-10, 1000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['NEWTON', 0.001, 0, 20, 0.0],
    ELE_GAUSS_POINTS=2,
    COUPLING_CONTROL=['LMAX', 1e-12],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[3, 6, 1e-10, 1000, 1.0, 101, 4],
    NON_LINEAR_SOLVER=['PICARD', 1.0, 20, 0.0],
    COUPLING_CONTROL=['LMAX', 1e-12],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    LINEAR_SOLVER=[2, 1, 1e-12, 1000, 1.0, 1, 2],
    COUPLING_CONTROL=['LMAX', 1e-12],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    NOD_VALUES=[
        ['HEAD'],
        ['WDEPTH'],
        ['COUPLING'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    NOD_VALUES=[
        ['WDEPTH'],
        ['HEAD'],
        ['FLUX'],
    ],
    GEO_TYPE=['POINT', 'POINT4'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='OVERLAND_FLOW',
    NOD_VALUES=[
        ['WDEPTH'],
        ['HEAD'],
        ['FLUX'],
    ],
    GEO_TYPE=['POINT', 'POINT5'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE=['POLYLINE', 'OUTPUT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='RICHARDS_FLOW',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='GROUNDWATER_FLOW',
    NOD_VALUES=[
        ['HEAD'],
        ['PRESSURE'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='OVERLAND_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    NUM_TYPE='NEW',
)
model.rfd.read_file('abdul.rfd')
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE', 'TOPO'],
    DIS_TYPE=['CONSTANT_NEUMANN', 1.0],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='OVERLAND_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POLYLINE', 'CRITICALDEPTH'],
    DIS_TYPE=[
        ['CRITICALDEPTH', 1],
        [0.0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['COLUMN', 'TOP'],
    DIS_TYPE=[
        ['CONSTANT', 1],
        ['PCS', 'OVERLAND_FLOW'],
        ['HEAD'],
        [0.0275, 0.001],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_END=20,
    TIME_START=0.0,
    TIME_STEPS=[1, 0.7],
)
gli_ext_file = GLIext(
    file_name='SFC_BC_RIGHT_L1',
    file_ext='.tin',
)
gli_ext_file.read_file('SFC_BC_RIGHT_L1.tin')
model.add_gli_ext(gli_ext_file)
gli_ext_file = GLIext(
    file_name='SFC_BC_LEFT_L1',
    file_ext='.tin',
)
gli_ext_file.read_file('SFC_BC_LEFT_L1.tin')
model.add_gli_ext(gli_ext_file)
model.write_input()
model.run_model()
