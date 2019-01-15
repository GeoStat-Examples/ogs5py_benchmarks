# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='cmp8_root',
    task_id='cmp8',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 2],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='H2O',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='H[+]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='OH[-]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='HCO3[-]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO3[2-]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ca[2+]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Mg[2+]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Cl[-]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 2.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CaOH[+]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='MgOH[+]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CaCO3',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CaHCO3[+]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='MgCO3',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='MgHCO3[+]',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Calcite_CaCO3_s',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Dolomite_CaMg(CO3)2_s',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 0],
)
model.gli.read_file('cmp8.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 2],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='H2O',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='H[+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='OH[-]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='HCO3[-]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO3[2-]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.123],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CO2',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Ca[2+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.123],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Mg[2+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Cl[-]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CaOH[+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='MgOH[+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CaCO3',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='CaHCO3[+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='MgCO3',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='MgHCO3[+]',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Calcite_CaCO3_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.05741],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='Dolomite_CaMg(CO3)2_s',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.krc.add_block(
    main_key='KINREACTIONDATA',
    SOLVER_TYPE=2,
    RELATIVE_ERROR=1e-06,
    MIN_TIMESTEP=1e-11,
    INITIAL_TIMESTEP=0.1,
    DEBUG_OUTPUT=[],
    NO_REACTIONS=[],
    ACTIVITY_MODEL=3,
    SCALE_DCDT=[],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='Calcite',
    CHEMAPPNAME='CAL2',
    MINERALNAME='Calcite_CaCO3_s',
    TYPE='Mineralkinetics',
    EQUATION=['Calcite_CaCO3_s', '=', 'Ca[2+]', '+', 'CO3[2-]'],
    EQUILIBRIUM_CONSTANT=['UNIFORM', -8.48],
    RATE_EXPONENTS=[1.0, 1.0],
    REACTIVE_SURFACE_AREA=[0, 3.2],
    PRECIPITATION_FACTOR=1,
    BASETERM=[-5.709965389, 23500],
    MECHANISMTERM=[
        [-0.299988938, 14400],
        ['H[+]', 1.0],
    ],
    PRODUCTIONSTOCH=[
        ['Ca[2+]', -1.0],
        ['CO3[2-]', -1.0],
    ],
)
model.krc.add_block(
    main_key='REACTION',
    NAME='Dolomite',
    CHEMAPPNAME='DOL2',
    MINERALNAME='Dolomite_CaMg(CO3)2_s',
    TYPE='Mineralkinetics',
    EQUATION=['Dolomite_CaMg(CO3)2_s', '=', 'Ca[2+]', '+', 'Mg[2+]', '+', 2, 'CO3[2-]'],
    EQUILIBRIUM_CONSTANT=['UNIFORM', -17.09],
    RATE_EXPONENTS=[1.0, 1.0],
    REACTIVE_SURFACE_AREA=[0, 0.32],
    PRECIPITATION_FACTOR=1,
    BASETERM=[-7.53, 52200],
    MECHANISMTERM=[
        [-3.19, 36100],
        ['H[+]', 0.5],
    ],
    PRODUCTIONSTOCH=[
        ['Ca[2+]', -1.0],
        ['Mg[2+]', -1.0],
        ['CO3[2-]', -2.0],
    ],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='H2O',
    MOBILE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='H[+]',
    MOBILE=1,
    VALENCE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='OH[-]',
    MOBILE=1,
    VALENCE=-1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='HCO3[-]',
    MOBILE=1,
    VALENCE=-1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO3[2-]',
    MOBILE=1,
    VALENCE=-2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CO2',
    MOBILE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Ca[2+]',
    MOBILE=1,
    VALENCE=2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Mg[2+]',
    MOBILE=1,
    VALENCE=2,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Cl[-]',
    MOBILE=1,
    VALENCE=-1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CaOH[+]',
    MOBILE=1,
    VALENCE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='MgOH[+]',
    MOBILE=1,
    VALENCE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CaCO3',
    MOBILE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='CaHCO3[+]',
    MOBILE=1,
    VALENCE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='MgCO3',
    MOBILE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='MgHCO3[+]',
    MOBILE=1,
    VALENCE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Calcite_CaCO3_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='Dolomite_CaMg(CO3)2_s',
    MOBILE=0,
    TRANSPORT_PHASE=1,
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
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.32],
    VOL_MAT=[1, 0.68],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.157e-12],
    MASS_DISPERSION=[1, 0.0067, 0.1],
    DENSITY=[1, 1800.0],
)
model.msh.read_file('cmp8.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1800.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
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
        ['Mg[2+]'],
        ['Ca[2+]'],
        ['Cl[-]'],
        ['CO3[2-]'],
        ['HCO3[-]'],
        ['CO2'],
        ['Calcite_CaCO3_s'],
        ['Dolomite_CaMg(CO3)2_s'],
    ],
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['CO3[2-]'],
        ['Ca[2+]'],
        ['Mg[2+]'],
        ['Cl[-]'],
        ['HCO3[-]'],
        ['CO2'],
        ['Calcite_CaCO3_s'],
        ['Dolomite_CaMg(CO3)2_s'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT_LINE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 2],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['HEAD'],
        ['CO3[2-]'],
        ['Ca[2+]'],
        ['Mg[2+]'],
        ['Cl[-]'],
        ['HCO3[-]'],
        ['CO2'],
        ['Calcite_CaCO3_s'],
        ['Dolomite_CaMg(CO3)2_s'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 2],
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
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.rei.add_block(
    main_key='REACTION_INTERFACE',
    MOL_PER='VOLUME',
    WATER_CONCENTRATION='CONSTANT',
    PRESSURE=['CONSTANT', 1.0],
    TEMPERATURE=['CONSTANT', 298.15],
    RESIDUAL='REMOVE',
)
model.rfd.add_block(
    ITERATION_PROPERTIES_CONCENTRATION=[
        [0],
        [0, 100, 1e-06, 0],
    ],
)
model.rfd.add_block(
    REFERENCE_CONDITIONS=[9.81, 0.0, 101325.0],
)
model.rfd.add_block(
    APRIORI_REFINE_ELEMENT=[0, 0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT', -2.9976852e-06],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_STEPS=[10, 100.0],
    TIME_END=21000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[10, 100.0],
    TIME_END=21000.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()
