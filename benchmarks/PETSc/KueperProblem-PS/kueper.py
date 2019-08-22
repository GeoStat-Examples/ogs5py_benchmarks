# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='kueper_root',
    task_id='kueper',
    output_dir='out',
)
model.msh.read_file('kueper.msh')
model.gli.read_file('kueper.gli')
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
    GEO_TYPE=['POINT', 'POINT2'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT3'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='SATURATION2',
    GEO_TYPE=['POLYLINE', 'SOURCE'],
    DIS_TYPE=['CONSTANT', 0.38],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='PS_GLOBAL',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
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
    GEO_TYPE=['POLYLINE', 'SOURCE'],
    DIS_TYPE=['CONSTANT', 0.38],
)
model.st.add_block(
    main_key='SOURCE_TERM',
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    POROSITY=[1, 0.4],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5.04e-10],
    PERMEABILITY_SATURATION=[
        [6, 0.078, 1.0, 3.86],
        [66, 0.0, 1.0, 3.86, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 369.73],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    POROSITY=[1, 0.39],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 2.05e-10],
    PERMEABILITY_SATURATION=[
        [6, 0.069, 1.0, 3.51],
        [66, 0.0, 1.0, 3.51, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 434.45],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    POROSITY=[1, 0.39],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 5.26e-11],
    PERMEABILITY_SATURATION=[
        [6, 0.098, 1.0, 2.49],
        [66, 0.0, 1.0, 2.49, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 1323.95],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    POROSITY=[1, 0.41],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 8.19e-12],
    PERMEABILITY_SATURATION=[
        [6, 0.189, 1.0, 3.3],
        [66, 0.0, 1.0, 3.3, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 3246.15],
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
    PCS_TYPE='SATURATION2',
    DENSITY=[1, 1630.0],
    VISCOSITY=[1, 0.0009],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='PS_GLOBAL',
    ELE_MASS_LUMPING=1,
    ELE_UPWINDING=[0, 1.0],
    LINEAR_SOLVER=['petsc', 'bcgs', 'bjacobi', 1e-07, 2000, 1.0],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 15, 1.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='PS_GLOBAL',
    TIME_END=311,
    TIME_START=0.0,
    TIME_STEPS=[5, 1.0],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='PS_GLOBAL',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['SATURATION1'],
        ['SATURATION2'],
        ['PRESSURE_CAP'],
    ],
    GEO_TYPE=['POINT', 'POINT4'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
