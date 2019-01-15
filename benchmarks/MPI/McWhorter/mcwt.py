# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='mcwt_root',
    task_id='mcwt',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'left'],
    DIS_TYPE=['CONSTANT', 5000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'left'],
    DIS_TYPE=['CONSTANT', 200000.0],
)
model.ddc.add_block(
    main_key='DOMAIN',
    ELEMENTS=[
        [15],
        [16],
        [17],
        [18],
        [19],
        [20],
        [44],
        [45],
        [46],
        [47],
        [48],
        [49],
        [73],
        [74],
        [75],
        [76],
        [77],
        [78],
        [100],
        [101],
        [102],
        [103],
        [104],
        [105],
        [106],
        [107],
        [108],
        [130],
        [131],
        [132],
        [133],
        [134],
        [135],
        [136],
        [137],
        [160],
        [161],
        [162],
        [163],
        [164],
        [165],
        [166],
        [167],
    ],
    NODES_INNER=[
        [50],
        [84],
        [85],
        [49],
        [86],
        [48],
        [87],
        [47],
        [88],
        [46],
        [89],
        [45],
        [90],
        [44],
        [112],
        [113],
        [114],
        [115],
        [116],
        [117],
        [118],
        [140],
        [141],
        [142],
        [143],
        [144],
        [145],
        [146],
        [138],
        [166],
        [167],
        [139],
        [168],
        [169],
        [170],
        [171],
        [172],
        [173],
        [174],
        [175],
        [147],
        [195],
        [196],
        [197],
        [198],
        [199],
        [200],
        [201],
        [202],
        [203],
        [18],
        [19],
        [20],
        [21],
        [22],
        [23],
        [24],
        [25],
        [26],
        [204],
    ],
)
model.ddc.add_block(
    main_key='DOMAIN',
    ELEMENTS=[
        [21],
        [22],
        [23],
        [24],
        [25],
        [26],
        [27],
        [28],
        [50],
        [51],
        [52],
        [53],
        [54],
        [55],
        [56],
        [57],
        [79],
        [80],
        [81],
        [82],
        [83],
        [84],
        [85],
        [86],
        [109],
        [110],
        [111],
        [112],
        [113],
        [114],
        [115],
        [138],
        [139],
        [140],
        [141],
        [142],
        [143],
        [144],
        [168],
        [169],
        [170],
        [171],
        [172],
        [173],
    ],
    NODES_INNER=[
        [44],
        [90],
        [91],
        [43],
        [92],
        [42],
        [93],
        [41],
        [94],
        [40],
        [95],
        [39],
        [96],
        [38],
        [97],
        [37],
        [36],
        [2],
        [118],
        [119],
        [120],
        [121],
        [122],
        [123],
        [124],
        [125],
        [35],
        [146],
        [147],
        [148],
        [149],
        [150],
        [151],
        [152],
        [153],
        [34],
        [175],
        [176],
        [177],
        [178],
        [179],
        [180],
        [181],
        [33],
        [203],
        [204],
        [205],
        [206],
        [207],
        [208],
        [209],
        [32],
        [26],
        [27],
        [28],
        [29],
        [30],
        [31],
        [1],
    ],
)
model.ddc.add_block(
    main_key='DOMAIN',
    ELEMENTS=[
        [8],
        [9],
        [10],
        [11],
        [12],
        [13],
        [14],
        [37],
        [38],
        [39],
        [40],
        [41],
        [42],
        [43],
        [65],
        [66],
        [67],
        [68],
        [69],
        [70],
        [71],
        [72],
        [94],
        [95],
        [96],
        [97],
        [98],
        [99],
        [123],
        [124],
        [125],
        [126],
        [127],
        [128],
        [129],
        [152],
        [153],
        [154],
        [155],
        [156],
        [157],
        [158],
        [159],
    ],
    NODES_INNER=[
        [57],
        [77],
        [78],
        [56],
        [79],
        [55],
        [80],
        [54],
        [81],
        [53],
        [82],
        [52],
        [83],
        [51],
        [84],
        [50],
        [105],
        [106],
        [107],
        [108],
        [109],
        [110],
        [111],
        [112],
        [104],
        [132],
        [133],
        [134],
        [135],
        [136],
        [137],
        [138],
        [139],
        [140],
        [160],
        [161],
        [162],
        [163],
        [164],
        [165],
        [166],
        [188],
        [189],
        [190],
        [191],
        [192],
        [193],
        [194],
        [195],
        [167],
        [10],
        [11],
        [12],
        [13],
        [14],
        [15],
        [16],
        [17],
        [18],
        [196],
    ],
)
model.ddc.add_block(
    main_key='DOMAIN',
    ELEMENTS=[
        [0],
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7],
        [29],
        [30],
        [31],
        [32],
        [33],
        [34],
        [35],
        [36],
        [58],
        [59],
        [60],
        [61],
        [62],
        [63],
        [64],
        [87],
        [88],
        [89],
        [90],
        [91],
        [92],
        [93],
        [116],
        [117],
        [118],
        [119],
        [120],
        [121],
        [122],
        [145],
        [146],
        [147],
        [148],
        [149],
        [150],
        [151],
    ],
    NODES_INNER=[
        [3],
        [65],
        [70],
        [64],
        [71],
        [63],
        [72],
        [62],
        [73],
        [61],
        [74],
        [60],
        [75],
        [59],
        [76],
        [58],
        [77],
        [57],
        [66],
        [98],
        [99],
        [100],
        [101],
        [102],
        [103],
        [104],
        [105],
        [67],
        [126],
        [127],
        [128],
        [129],
        [130],
        [131],
        [132],
        [68],
        [154],
        [155],
        [156],
        [157],
        [158],
        [159],
        [160],
        [69],
        [182],
        [183],
        [184],
        [185],
        [186],
        [187],
        [188],
        [0],
        [4],
        [5],
        [6],
        [7],
        [8],
        [9],
        [10],
    ],
)
model.gli.read_file('mcwt.gli')
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 50000.0],
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
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000],
    VISCOSITY=[1, 0.001],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    POROSITY=[1, 0.3],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-10],
    PERMEABILITY_SATURATION=[
        [6, 0.0, 1.0, 2],
        [66, 0.0, 1.0, 2, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 5000],
)
model.msh.read_file('mcwt.msh')
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    ELE_MASS_LUMPING=1,
    ELE_UPWINDING=[0, 1.0],
    LINEAR_SOLVER=[2, 1, 1e-12, 2000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 50, 1.0],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE=['POLYLINE', 'TOP'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [500],
        [1000],
        [2000],
        [4000],
        [7000],
        [10000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [500],
        [1000],
        [2000],
        [4000],
        [7000],
        [10000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE=['POINT', 'POINT4'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.add_block(
    PROJECT=['Buckley-Leverett', 'benchmark', 'one.', 'Prepared', 'by', 'WW'],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 50990.2],
        [0.025, 36055.51],
        [0.05, 29439.2],
        [0.075, 25495.1],
        [0.1, 22803.51],
        [0.125, 20816.66],
        [0.15, 19272.48],
        [0.175, 18027.76],
        [0.2, 16996.73],
        [0.225, 16124.52],
        [0.25, 15374.12],
        [0.275, 14719.6],
        [0.3, 14142.14],
        [0.325, 13627.7],
        [0.35, 13165.61],
        [0.375, 12747.55],
        [0.4, 12366.94],
        [0.425, 12018.5],
        [0.45, 11697.95],
        [0.475, 11401.75],
        [0.5, 11126.97],
        [0.525, 10871.15],
        [0.55, 10632.19],
        [0.575, 10408.33],
        [0.6, 10408.33],
        [0.625, 10408.33],
        [0.65, 10408.33],
        [0.675, 10408.33],
        [0.7, 10408.33],
        [0.725, 10408.33],
        [0.75, 10408.33],
        [0.775, 10408.33],
        [0.8, 10000.0],
        [0.825, 10000.0],
        [0.85, 10000.0],
        [0.875, 10000.0],
        [0.9, 10000.0],
        [0.925, 10000.0],
        [0.95, 10000.0],
        [0.975, 10000.0],
        [1.0, 10000.0],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_CONTROL=[
        ['PI_AUTO_STEP_SIZE'],
        [1, 0.0001, 1e-10, '10s'],
    ],
    TIME_END=10.0,
    TIME_START=0.0,
)
model.write_input()
model.run_model()