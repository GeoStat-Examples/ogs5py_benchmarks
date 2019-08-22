# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='1D_TPF_resS_flow_root',
    task_id='1D_TPF_resS_flow',
    output_dir='out',
)
model.msh.read_file('1D_TPF_resS_flow.msh')
model.gli.read_file('1D_TPF_resS_flow.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='PS_GLOBAL',
    NUM_TYPE='dPcdSwGradSnw',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 98100],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT4'],
    DIS_TYPE=['CONSTANT', 93195.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 98067],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION1',
    GEO_TYPE=['POLYLINE', 'S_1'],
    DIS_TYPE=['CONSTANT', 0.899997748],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION1',
    GEO_TYPE=['POLYLINE', 'S_2'],
    DIS_TYPE=['CONSTANT', 0.899997748],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE=['POLYLINE', 'S_1'],
    DIS_TYPE=['CONSTANT', 0.100002252],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE=['POLYLINE', 'S_2'],
    DIS_TYPE=['CONSTANT', 0.100002252],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'RIGHTPLINE'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.25],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.54249e-11],
    PERMEABILITY_SATURATION=[
        [61, 0.2, 1.0, 3.86],
        [66, 0.2, 1.0, 3.86, 0.0],
    ],
    CAPILLARY_PRESSURE=[6, 0.0],
    MASS_DISPERSION=[1, 0.5, 1e-10],
    DENSITY=[1, 2650.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 999.7],
    VISCOSITY=[1, 0.001307],
    PHASE_DIFFUSION=[1, 7.66e-10],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='SATURATION2',
    DENSITY=[1, 999.7],
    VISCOSITY=[1, 0.001307],
    PHASE_DIFFUSION=[1, 7.66e-10],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='PS_GLOBAL',
    ELE_MASS_LUMPING=1,
    ELE_UPWINDING=[0, 1.0],
    LINEAR_SOLVER=[2, 1, 1e-12, 2000, 1.0, 1, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 15, 1.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='PS_GLOBAL',
    TIME_STEPS=[3, 21600.0],
    TIME_END=864000000.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SATURATION1'],
        ['SATURATION2'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT_LINE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
