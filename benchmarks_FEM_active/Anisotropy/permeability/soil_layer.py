# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='soil_layer_root',
    task_id='soil_layer',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT2'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'POLYLINE11'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.gli.read_file('soil_layer.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Tracer',
    GEO_TYPE=['POLYLINE', 'POLYLINE11'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Tracer',
    MOBILE=1,
    TRANSPORT_PHASE=0,
    DIFFUSION=[1, 6e-10],
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
    NAME='LAYER0',
    GEO_TYPE=['LAYER', 0],
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ANISOTROPIC', 5.5e-15, 4.5e-15, 4.5e-15, 5.5e-15],
    MASS_DISPERSION=[1, 0.0, 0.0],
    DENSITY=[1, 2000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='LAYER1',
    GEO_TYPE=['LAYER', 0],
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ANISOTROPIC', 5.5e-15, 4.5e-15, 4.5e-15, 5.5e-15],
    MASS_DISPERSION=[1, 0.0, 0.0],
    DENSITY=[1, 2000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='LAYER2',
    GEO_TYPE=['LAYER', 0],
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ANISOTROPIC', 5.5e-15, 4.5e-15, 4.5e-15, 5.5e-15],
    MASS_DISPERSION=[1, 0.0, 0.0],
    DENSITY=[1, 2000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='LAYER3',
    GEO_TYPE=['LAYER', 0],
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ANISOTROPIC', 5.5e-15, 4.5e-15, 4.5e-15, 5.5e-15],
    MASS_DISPERSION=[1, 0.0, 0.0],
    DENSITY=[1, 2000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='LAYER4',
    GEO_TYPE=['LAYER', 0],
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ANISOTROPIC', 5.5e-15, 4.5e-15, 4.5e-15, 5.5e-15],
    MASS_DISPERSION=[1, 0.0, 0.0],
    DENSITY=[1, 2000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='LAYER5',
    GEO_TYPE=['LAYER', 0],
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ANISOTROPIC', 5.5e-15, 4.5e-15, 4.5e-15, 5.5e-15],
    MASS_DISPERSION=[1, 0.0, 0.0],
    DENSITY=[1, 2000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    NAME='LAYER6',
    GEO_TYPE=['LAYER', 0],
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 1.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ANISOTROPIC', 5.5e-15, 4.5e-15, 4.5e-15, 5.5e-15],
    MASS_DISPERSION=[1, 0.0, 0.0],
    DENSITY=[1, 2000.0],
)
model.msh.read_file('soil_layer.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
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
        ['PRESSURE1'],
        ['Tracer'],
    ],
    GEO_TYPE='DOMAIN',
    TIM_TYPE=['STEPS', 1],
    DAT_TYPE='PVD',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.st.add_block(
    main_key='SOURCE_TERM',
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[30, 10000000.0],
    TIME_START=0.0,
    TIME_END=300000000.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[30, 10000000.0],
    TIME_START=0.0,
    TIME_END=300000000.0,
)
model.write_input()
model.run_model()
