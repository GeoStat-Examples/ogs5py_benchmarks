# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='lag2d_root',
    task_id='lag2d',
    output_dir='out',
)
model.msh.read_file('lag2d.msh')
model.gli.read_file('lag2d.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='RICHARDS_FLOW',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    RELOAD=[3, 250],
)
model.rfd.read_file('lag2d.rfd')
model.cct.add_block(
    main_key='COMMUNICATION_TABLE',
    MYRANK=0,
    NNEIGHBORS=1,
    NEIGHBOR=[
        [1],
        [120],
        [52, 5081],
        [65, 5264],
        [65, 5265],
        [65, 6059],
        [131, 6059],
        [174, 4961],
        [174, 5058],
        [175, 4961],
        [175, 5167],
        [377, 5033],
        [377, 5079],
        [377, 5332],
        [378, 5033],
        [378, 5034],
        [427, 5081],
        [427, 5543],
        [427, 6519],
        [428, 5543],
        [480, 5079],
        [508, 5087],
        [508, 5088],
        [508, 5420],
        [632, 5114],
        [632, 5115],
        [714, 5214],
        [714, 6404],
        [714, 6551],
        [715, 5186],
        [715, 5214],
        [881, 5768],
        [894, 5186],
        [894, 6198],
        [901, 5058],
        [1083, 5079],
        [1083, 5209],
        [1083, 6059],
        [1102, 5543],
        [1102, 5544],
        [1102, 5545],
        [1201, 5422],
        [1287, 5312],
        [1287, 5313],
        [1287, 5713],
        [1406, 5420],
        [1406, 5422],
        [1406, 6274],
        [1462, 5545],
        [1462, 6198],
        [1681, 5088],
        [1681, 5424],
        [1695, 5080],
        [1695, 5081],
        [1695, 5422],
        [1698, 5432],
        [1698, 5433],
        [1698, 5837],
        [1698, 6339],
        [1744, 5312],
        [1744, 5424],
        [1806, 5420],
        [1861, 5512],
        [1861, 5901],
        [1862, 5512],
        [1862, 5842],
        [1866, 5842],
        [2033, 5264],
        [2033, 5986],
        [2288, 5058],
        [2288, 5888],
        [2288, 6505],
        [2366, 5088],
        [2496, 6437],
        [2594, 5448],
        [2594, 5862],
        [2594, 6437],
        [2678, 5040],
        [2678, 5041],
        [2678, 5768],
        [2695, 6177],
        [2828, 5433],
        [2899, 5448],
        [2953, 5040],
        [2953, 5155],
        [2953, 5842],
        [3009, 5115],
        [3009, 5430],
        [3029, 6339],
        [3172, 5167],
        [3172, 5986],
        [3209, 5114],
        [3209, 5901],
        [3954, 5768],
        [4199, 5448],
        [4199, 5449],
        [4199, 6431],
        [4248, 5430],
        [4248, 6165],
        [4248, 6334],
        [4251, 5498],
        [4251, 5888],
        [4251, 6177],
        [4324, 5034],
        [4324, 6366],
        [4324, 6431],
        [4392, 5034],
        [4467, 5433],
        [4467, 5722],
        [4467, 5768],
        [4475, 6165],
        [4489, 5019],
        [4489, 6177],
        [4489, 6339],
        [4540, 6165],
        [4540, 6166],
        [4653, 6166],
        [4653, 6551],
        [4673, 5713],
        [4673, 6475],
        [4678, 5040],
        [4757, 5713],
    ],
)
model.cct.add_block(
    main_key='COMMUNICATION_TABLE',
    MYRANK=1,
)
model.cct.append_to_block(
    NNEIGHBORS=2,
)
model.cct.append_to_block(
    NEIGHBOR=[
        [0],
        [120],
        [4961, 174],
        [4961, 175],
        [5019, 4489],
        [5033, 377],
        [5033, 378],
        [5034, 378],
        [5034, 4324],
        [5034, 4392],
        [5040, 2678],
        [5040, 2953],
        [5040, 4678],
        [5041, 2678],
        [5058, 174],
        [5058, 901],
        [5058, 2288],
        [5079, 377],
        [5079, 480],
        [5079, 1083],
        [5080, 1695],
        [5081, 52],
        [5081, 427],
        [5081, 1695],
        [5087, 508],
        [5088, 508],
        [5088, 1681],
        [5088, 2366],
        [5114, 632],
        [5114, 3209],
        [5115, 632],
        [5115, 3009],
        [5155, 2953],
        [5167, 175],
        [5167, 3172],
        [5186, 715],
        [5186, 894],
        [5209, 1083],
        [5214, 714],
        [5214, 715],
        [5264, 65],
        [5264, 2033],
        [5265, 65],
        [5312, 1287],
        [5312, 1744],
        [5313, 1287],
        [5332, 377],
        [5420, 508],
        [5420, 1406],
        [5420, 1806],
        [5422, 1201],
        [5422, 1406],
        [5422, 1695],
        [5424, 1681],
        [5424, 1744],
        [5430, 3009],
        [5430, 4248],
        [5432, 1698],
        [5433, 1698],
        [5433, 2828],
        [5433, 4467],
        [5448, 2594],
        [5448, 2899],
        [5448, 4199],
        [5449, 4199],
        [5498, 4251],
        [5512, 1861],
        [5512, 1862],
        [5543, 427],
        [5543, 428],
        [5543, 1102],
        [5544, 1102],
        [5545, 1102],
        [5545, 1462],
        [5713, 1287],
        [5713, 4673],
        [5713, 4757],
        [5722, 4467],
        [5768, 881],
        [5768, 2678],
        [5768, 3954],
        [5768, 4467],
        [5837, 1698],
        [5842, 1862],
        [5842, 1866],
        [5842, 2953],
        [5862, 2594],
        [5888, 2288],
        [5888, 4251],
        [5901, 1861],
        [5901, 3209],
        [5986, 2033],
        [5986, 3172],
        [6059, 65],
        [6059, 131],
        [6059, 1083],
        [6165, 4248],
        [6165, 4475],
        [6165, 4540],
        [6166, 4540],
        [6166, 4653],
        [6177, 2695],
        [6177, 4251],
        [6177, 4489],
        [6198, 894],
        [6198, 1462],
        [6274, 1406],
        [6334, 4248],
        [6339, 1698],
        [6339, 3029],
        [6339, 4489],
        [6366, 4324],
        [6404, 714],
        [6431, 4199],
        [6431, 4324],
        [6437, 2496],
        [6437, 2594],
        [6475, 4673],
        [6505, 2288],
        [6519, 427],
        [6551, 714],
        [6551, 4653],
    ],
)
model.cct.append_to_block(
    NEIGHBOR=[
        [3],
        [128],
        [6609, 17179],
        [6650, 14790],
        [6650, 15205],
        [6658, 14848],
        [6659, 14848],
        [6755, 15630],
        [6755, 16962],
        [6756, 16962],
        [6790, 14999],
        [6790, 15000],
        [6790, 16586],
        [6900, 15860],
        [6980, 15195],
        [7012, 15182],
        [7012, 15183],
        [7012, 16514],
        [7034, 15195],
        [7034, 15196],
        [7051, 15205],
        [7100, 14848],
        [7100, 15336],
        [7100, 15779],
        [7100, 16311],
        [7276, 15428],
        [7276, 15429],
        [7281, 15468],
        [7281, 15687],
        [7281, 17756],
        [7282, 15468],
        [7282, 15630],
        [7415, 14788],
        [7415, 15860],
        [7476, 14999],
        [7476, 16441],
        [7477, 14999],
        [7552, 15364],
        [7552, 15365],
        [7552, 15960],
        [7588, 15779],
        [7612, 14848],
        [7612, 15195],
        [7612, 15794],
        [7638, 17343],
        [7638, 17992],
        [7653, 15009],
        [7653, 15017],
        [7653, 15018],
        [7816, 15961],
        [7816, 15982],
        [7816, 16441],
        [8030, 17980],
        [8051, 16842],
        [8079, 15364],
        [8081, 15960],
        [8093, 16842],
        [8093, 17980],
        [8093, 18010],
        [8206, 15428],
        [8206, 15679],
        [8206, 16782],
        [8207, 15679],
        [8270, 16586],
        [8298, 14995],
        [8298, 14997],
        [8298, 16515],
        [8322, 15205],
        [8322, 17179],
        [8340, 16513],
        [8340, 16514],
        [8547, 17756],
        [8586, 15183],
        [8586, 15679],
        [8643, 15860],
        [8643, 16841],
        [8643, 16842],
        [8677, 15779],
        [8677, 16851],
        [8677, 17852],
        [8712, 14788],
        [8712, 14790],
        [8921, 16850],
        [8921, 17139],
        [8921, 17852],
        [8933, 15009],
        [8933, 15270],
        [9004, 17139],
        [9029, 16191],
        [9029, 16784],
        [9029, 16962],
        [9043, 15009],
        [9047, 15429],
        [9047, 17139],
        [9082, 14997],
        [9082, 15018],
        [9182, 16191],
        [9182, 17179],
        [9225, 15960],
        [9260, 15183],
        [9298, 15960],
        [9298, 15961],
        [9441, 16513],
        [9479, 15196],
        [9479, 17343],
        [9515, 17852],
        [9522, 16643],
        [9522, 17756],
        [9564, 15377],
        [9564, 15460],
        [9564, 17792],
        [9582, 17954],
        [9582, 18006],
        [9583, 17978],
        [9583, 18006],
        [9607, 16513],
        [9607, 16586],
        [9607, 16755],
        [9680, 17978],
        [9680, 17992],
        [9717, 17792],
        [9717, 17954],
        [9722, 15460],
        [9728, 16515],
        [9728, 17919],
        [9732, 15270],
        [9732, 15378],
        [9732, 15460],
        [9741, 17919],
        [9741, 17980],
    ],
)
model.cct.add_block(
    main_key='COMMUNICATION_TABLE',
    MYRANK=2,
    NNEIGHBORS=1,
    NEIGHBOR=[
        [3],
        [122],
        [9883, 18382],
        [9883, 19192],
        [9884, 18290],
        [9884, 19192],
        [9884, 19194],
        [9935, 18076],
        [9935, 19562],
        [9936, 18076],
        [9936, 18183],
        [9936, 18290],
        [10080, 18836],
        [10080, 19026],
        [10080, 19421],
        [10081, 18280],
        [10081, 19026],
        [10081, 19282],
        [10107, 18277],
        [10107, 18279],
        [10286, 18149],
        [10286, 18151],
        [10286, 18550],
        [10482, 18266],
        [10482, 18267],
        [10522, 18280],
        [10551, 18290],
        [10580, 18381],
        [10741, 18369],
        [10741, 18370],
        [10741, 19292],
        [10781, 18381],
        [10781, 18382],
        [10840, 18568],
        [10840, 18723],
        [10842, 18567],
        [10842, 18568],
        [10889, 18412],
        [10889, 18600],
        [10890, 18412],
        [10896, 18412],
        [10896, 18790],
        [11122, 18279],
        [11340, 18369],
        [11393, 18279],
        [11393, 19545],
        [11393, 19614],
        [11450, 19545],
        [11486, 18266],
        [11519, 18277],
        [11519, 18790],
        [11565, 18351],
        [11565, 18400],
        [11565, 19046],
        [11587, 18267],
        [11587, 18836],
        [11693, 18165],
        [11693, 18351],
        [11693, 18710],
        [11694, 18710],
        [11843, 18351],
        [11990, 19046],
        [11991, 19046],
        [11991, 19175],
        [11991, 19176],
        [12041, 18266],
        [12041, 18827],
        [12041, 19448],
        [12248, 18151],
        [12248, 18897],
        [12334, 18970],
        [12334, 18971],
        [12367, 18669],
        [12367, 18917],
        [12378, 18280],
        [12378, 18785],
        [12412, 18381],
        [12589, 18993],
        [12590, 18993],
        [12590, 19436],
        [12590, 19537],
        [12667, 18971],
        [12667, 19238],
        [12667, 19259],
        [12844, 18723],
        [12844, 18993],
        [12864, 19172],
        [12864, 19343],
        [12931, 19259],
        [12931, 19529],
        [12975, 19545],
        [13037, 18567],
        [13037, 18669],
        [13054, 18783],
        [13054, 19545],
        [13054, 19548],
        [13087, 18710],
        [13087, 19292],
        [13087, 19615],
        [13113, 18600],
        [13113, 18970],
        [13155, 19172],
        [13155, 19562],
        [13240, 18917],
        [13240, 19176],
        [13402, 18381],
        [13402, 19436],
        [13464, 18550],
        [13464, 18584],
        [13464, 18785],
        [13483, 18151],
        [13648, 19316],
        [13648, 19317],
        [13855, 19316],
        [13855, 19448],
        [14044, 18897],
        [14044, 19440],
        [14087, 19343],
        [14087, 19529],
        [14100, 19292],
        [14324, 18897],
        [14391, 19317],
        [14391, 19548],
        [14586, 18550],
    ],
)
model.cct.add_block(
    main_key='COMMUNICATION_TABLE',
    MYRANK=3,
)
model.cct.append_to_block(
    NNEIGHBORS=2,
)
model.cct.append_to_block(
    NEIGHBOR=[
        [1],
        [128],
        [14788, 7415],
        [14788, 8712],
        [14790, 6650],
        [14790, 8712],
        [14848, 6658],
        [14848, 6659],
        [14848, 7100],
        [14848, 7612],
        [14995, 8298],
        [14997, 8298],
        [14997, 9082],
        [14999, 6790],
        [14999, 7476],
        [14999, 7477],
        [15000, 6790],
        [15009, 7653],
        [15009, 8933],
        [15009, 9043],
        [15017, 7653],
        [15018, 7653],
        [15018, 9082],
        [15182, 7012],
        [15183, 7012],
        [15183, 8586],
        [15183, 9260],
        [15195, 6980],
        [15195, 7034],
        [15195, 7612],
        [15196, 7034],
        [15196, 9479],
        [15205, 6650],
        [15205, 7051],
        [15205, 8322],
        [15270, 8933],
        [15270, 9732],
        [15336, 7100],
        [15364, 7552],
        [15364, 8079],
        [15365, 7552],
        [15377, 9564],
        [15378, 9732],
        [15428, 7276],
        [15428, 8206],
        [15429, 7276],
        [15429, 9047],
        [15460, 9564],
        [15460, 9722],
        [15460, 9732],
        [15468, 7281],
        [15468, 7282],
        [15630, 6755],
        [15630, 7282],
        [15679, 8206],
        [15679, 8207],
        [15679, 8586],
        [15687, 7281],
        [15779, 7100],
        [15779, 7588],
        [15779, 8677],
        [15794, 7612],
        [15860, 6900],
        [15860, 7415],
        [15860, 8643],
        [15960, 7552],
        [15960, 8081],
        [15960, 9225],
        [15960, 9298],
        [15961, 7816],
        [15961, 9298],
        [15982, 7816],
        [16191, 9029],
        [16191, 9182],
        [16311, 7100],
        [16441, 7476],
        [16441, 7816],
        [16513, 8340],
        [16513, 9441],
        [16513, 9607],
        [16514, 7012],
        [16514, 8340],
        [16515, 8298],
        [16515, 9728],
        [16586, 6790],
        [16586, 8270],
        [16586, 9607],
        [16643, 9522],
        [16755, 9607],
        [16782, 8206],
        [16784, 9029],
        [16841, 8643],
        [16842, 8051],
        [16842, 8093],
        [16842, 8643],
        [16850, 8921],
        [16851, 8677],
        [16962, 6755],
        [16962, 6756],
        [16962, 9029],
        [17139, 8921],
        [17139, 9004],
        [17139, 9047],
        [17179, 6609],
        [17179, 8322],
        [17179, 9182],
        [17343, 7638],
        [17343, 9479],
        [17756, 7281],
        [17756, 8547],
        [17756, 9522],
        [17792, 9564],
        [17792, 9717],
        [17852, 8677],
        [17852, 8921],
        [17852, 9515],
        [17919, 9728],
        [17919, 9741],
        [17954, 9582],
        [17954, 9717],
        [17978, 9583],
        [17978, 9680],
        [17980, 8030],
        [17980, 8093],
        [17980, 9741],
        [17992, 7638],
        [17992, 9680],
        [18006, 9582],
        [18006, 9583],
        [18010, 8093],
    ],
)
model.cct.append_to_block(
    NEIGHBOR=[
        [2],
        [122],
        [18076, 9935],
        [18076, 9936],
        [18149, 10286],
        [18151, 10286],
        [18151, 12248],
        [18151, 13483],
        [18165, 11693],
        [18183, 9936],
        [18266, 10482],
        [18266, 11486],
        [18266, 12041],
        [18267, 10482],
        [18267, 11587],
        [18277, 10107],
        [18277, 11519],
        [18279, 10107],
        [18279, 11122],
        [18279, 11393],
        [18280, 10081],
        [18280, 10522],
        [18280, 12378],
        [18290, 9884],
        [18290, 9936],
        [18290, 10551],
        [18351, 11565],
        [18351, 11693],
        [18351, 11843],
        [18369, 10741],
        [18369, 11340],
        [18370, 10741],
        [18381, 10580],
        [18381, 10781],
        [18381, 12412],
        [18381, 13402],
        [18382, 9883],
        [18382, 10781],
        [18400, 11565],
        [18412, 10889],
        [18412, 10890],
        [18412, 10896],
        [18550, 10286],
        [18550, 13464],
        [18550, 14586],
        [18567, 10842],
        [18567, 13037],
        [18568, 10840],
        [18568, 10842],
        [18584, 13464],
        [18600, 10889],
        [18600, 13113],
        [18669, 12367],
        [18669, 13037],
        [18710, 11693],
        [18710, 11694],
        [18710, 13087],
        [18723, 10840],
        [18723, 12844],
        [18783, 13054],
        [18785, 12378],
        [18785, 13464],
        [18790, 10896],
        [18790, 11519],
        [18827, 12041],
        [18836, 10080],
        [18836, 11587],
        [18897, 12248],
        [18897, 14044],
        [18897, 14324],
        [18917, 12367],
        [18917, 13240],
        [18970, 12334],
        [18970, 13113],
        [18971, 12334],
        [18971, 12667],
        [18993, 12589],
        [18993, 12590],
        [18993, 12844],
        [19026, 10080],
        [19026, 10081],
        [19046, 11565],
        [19046, 11990],
        [19046, 11991],
        [19172, 12864],
        [19172, 13155],
        [19175, 11991],
        [19176, 11991],
        [19176, 13240],
        [19192, 9883],
        [19192, 9884],
        [19194, 9884],
        [19238, 12667],
        [19259, 12667],
        [19259, 12931],
        [19282, 10081],
        [19292, 10741],
        [19292, 13087],
        [19292, 14100],
        [19316, 13648],
        [19316, 13855],
        [19317, 13648],
        [19317, 14391],
        [19343, 12864],
        [19343, 14087],
        [19421, 10080],
        [19436, 12590],
        [19436, 13402],
        [19440, 14044],
        [19448, 12041],
        [19448, 13855],
        [19529, 12931],
        [19529, 14087],
        [19537, 12590],
        [19545, 11393],
        [19545, 11450],
        [19545, 12975],
        [19545, 13054],
        [19548, 13054],
        [19548, 14391],
        [19562, 9935],
        [19562, 13155],
        [19614, 11393],
        [19615, 13087],
    ],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'LEFT_BOUNDARY'],
    DIS_TYPE=['GRADIENT', 0.0, 0.0, 9810.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT6293'],
    DIS_TYPE=['CONSTANT', -48049],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Al',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 2.26925051393488e-05],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-Ba',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 8.67288448415206e-05],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-C',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.866918912101625],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Ca',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 13.6134562529146],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-Cl',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 161.638419925808],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Fe',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.0538995973716032],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-H',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.829658768452354],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Inrt',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-K',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 1.34861719358752],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='10-Mg',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 6.85977069482896],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-Na',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 238.213695960189],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='12-O',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 239.540294130793],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='13-S',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 59.1494396193851],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='14-Si',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.180594231503969],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='15-Sr',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.0929257106197199],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='16-Zz',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['GRADIENT', 0.0, 0.0, 9810.0, ',', 'reference', 'position,', 'reference', 'value,', 'gradient'],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Al',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1179.54801223741],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-Ba',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0796837988327211],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-C',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 49.803571523175],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Ca',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 50.1315775121793],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-Cl',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 37.0041418974872],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Fe',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 170.08206952062],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-H',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 34075.0765245024],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Inrt',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1343.405108282],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-K',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 5.29777698366072],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='10-Mg',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 219.815152062716],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-Na',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 279.858674381246],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='12-O',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 76177.8644392331],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='13-S',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 33.4519194201324],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='14-Si',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 28317.0895708634],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='15-Sr',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.156686756755766],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='16-Zz',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Al',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 13.8732668983621],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-Ba',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 0.000975557087116634],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-C',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 2.40462219077058],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Ca',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 3.86928574002538],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-Cl',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 47.9127566651589],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Fe',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 7.24955624918647],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-H',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 33310.953969574],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Inrt',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 2033.09713759164],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-K',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 0.831199610280173],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='10-Mg',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 5.4283227340815],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-Na',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 52.063799613034],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='12-O',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 74180.5879713793],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='13-S',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 10.8034069824917],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='14-Si',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 28729.3410299741],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='15-Sr',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 0.0643855600474336],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='16-Zz',
    GEO_TYPE=['SURFACE', 'GRAVEL'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='1-Al',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 164.947321673364],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='2-Ba',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 0.0404878446840055],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='3-C',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 113.226371964233],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='4-Ca',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 3673.73666279417],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='5-Cl',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 0.0492592566728664],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='6-Fe',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 75.045724843465],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='7-H',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 33400.8271640642],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='8-Inrt',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 85.6911954303],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='9-K',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 14.5514927470889],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='10-Mg',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 65.6866271150311],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='11-Na',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 19.3726296499201],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='12-O',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 78216.5013393632],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='13-S',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 85.5895046914679],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='14-Si',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 28455.91134012606],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='15-Sr',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 4.80877037006526],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='16-Zz',
    GEO_TYPE=['SURFACE', 'CONCRETE'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='RICHARDS_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'RIGHT_BOUNDARY'],
    DIS_TYPE=['CONSTANT_NEUMANN', 5e-11],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[15, 0.1],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-12],
    PERMEABILITY_FUNCTION_POROSITY=[3, 0.2, 1e-12],
    PERMEABILITY_SATURATION=[4, 0.3, 1.0, 0.6],
    CAPILLARY_PRESSURE=[4, 2.45],
    MASS_DISPERSION=[1, 0.01, 0.01],
    DENSITY=[1, 1800.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[15, 0.1],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-12],
    PERMEABILITY_FUNCTION_POROSITY=[3, 0.3, 1e-12],
    PERMEABILITY_SATURATION=[4, 0.001, 1.0, 0.6667],
    CAPILLARY_PRESSURE=[4, 2.45],
    MASS_DISPERSION=[1, 0.01, 0.01],
    DENSITY=[1, 1800.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
    POROSITY=[15, 0.25],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-16],
    PERMEABILITY_FUNCTION_POROSITY=[3, 0.2292, 1e-16],
    PERMEABILITY_SATURATION=[4, 0.3, 1.0, 0.6],
    CAPILLARY_PRESSURE=[4, 2.4525],
    MASS_DISPERSION=[1, 0.01, 0.01],
    DENSITY=[1, 1800.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1800.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1800.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 1800.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='1-Al',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='2-Ba',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='3-C',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='4-Ca',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='5-Cl',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='6-Fe',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='7-H',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='8-Inrt',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='9-K',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='10-Mg',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='11-Na',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='12-O',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='13-S',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='14-Si',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='15-Sr',
    MOBILE=1,
    DIFFUSION=[9, 1.5e-09, 1.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='16-Zz',
    MOBILE=0,
)
model.gem.add_block(
    main_key='GEM_PROPERTIES',
    GEM_INIT_FILE='bensan-dat.lst',
)
model.gem.append_to_block(
    GEM_THREADS=4,
)
model.gem.append_to_block(
    FLAG_POROSITY_CHANGE=1,
)
model.gem.append_to_block(
    MIN_POROSITY=1e-06,
)
model.gem.append_to_block(
    MAX_POROSITY=1.0,
)
model.gem.append_to_block(
    FLAG_COUPLING_HYDROLOGY=1,
)
model.gem.append_to_block(
    CALCULATE_BOUNDARY_NODES=0,
)
model.gem.append_to_block(
    TEMPERATURE_GEM=298.15,
)
model.gem.append_to_block(
    GEM_SMART=0,
)
model.gem.append_to_block(
    MAX_FAILED_NODES=100,
)
model.gem.append_to_block(
    MY_SMART_GEMS=-1e-30,
)
model.gem.append_to_block(
    TRANSPORT_B=1,
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['Kaolinite', 1, 1, 0.0, 0.0, 0.0, -11.31, -13.18, -17.05, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 'H+', 0.777, 0.0, -0.472],
        [1, 3000000.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['Quartz', 1, 1, 0.0, 0.0, 0.0, 0.0, -13.99, -16.29, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 'H+', 0.0, 0.0, -0.5],
        [1, 0.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['Sand', 1, 1, 0.0, 0.0, 0.0, 0.0, -13.99, -16.29, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 'H+', 0.0, 0.0, -0.5],
        [1, 2143.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['Gravel', 1, 1, 0.0, 0.0, 0.0, 0.0, -13.99, -16.29, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 'H+', 0.0, 0.0, -0.5],
        [1, 120.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['Gibbsite', 1, 1, 0.0, 0.0, 0.0, -7.65, -11.5, -16.65, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 'H+', 0.992, 0.0, -0.784],
        [1, 100.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['SS_Montmor', 5, 1, 0.0, 0.0, 0.0, -10.98, -12.78, -16.52, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 'H+', 0.34, 0.0, -0.4],
        [1, 3000000.0],
        [7, 2.0, 2.0, 2.0, 1.0, 2.0, 1.0, 2.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['IlliteEx', 5, 1, 0.0, 0.0, 0.0, -10.98, -12.78, -16.52, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 'H+', 0.34, 0.0, -0.4],
        [1, 3000000.0],
        [5, 3.0, 2.0, 2.0, 1.0, 1.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['Phillipsite', 5, 1, 0.0, 0.0, 0.0, 0.0, -10.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 'H+', 0.0, 0.0, 0.0],
        [1, 100.0],
        [3, 2.0, 1.0, 1.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['Analcime', 1, 1, 0.0, 0.0, 0.0, 0.0, -10.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 'H+', 0.0, 0.0, 0.0],
        [1, 100.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['Mordenite', 1, 1, 0.0, 0.0, 0.0, 0.0, -10.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 'H+', 0.0, 0.0, 0.0],
        [1, 100.0],
    ],
)
model.gem.append_to_block(
    KINETIC_GEM=[
        ['Laumontite', 1, 1, 0.0, 0.0, 0.0, 0.0, -10.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 'H+', 0.0, 0.0, 0.0],
        [1, 100.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='RICHARDS_FLOW',
    ELE_UPWINDING=0.5,
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=['petsc', 'bcgs', 'bjacobi', 1e-10, 10000, 1.0],
    NON_LINEAR_SOLVER=['PICARD', 0.001, 10, 0.0],
    ELE_GAUSS_POINTS=3,
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=['petsc', 'bcgs', 'bjacobi', 1e-14, 2000, 1.0],
    ELE_GAUSS_POINTS=3,
    FEM_FCT=[1, 0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='RICHARDS_FLOW',
    TIME_START=0.0,
    TIME_END=10.0,
    TIME_CONTROL=[
        ['SELF_ADAPTIVE'],
        [10001, 1.1],
        [10001, 0.8],
        ['MAX_TIME_STEP'],
        [1000000.0],
        ['MIN_TIME_STEP'],
        [10.0],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_START=0.0,
    TIME_END=10.0,
    TIME_CONTROL=[
        ['SELF_ADAPTIVE'],
        [80, 1.1],
        [85, 0.8],
        ['MAX_TIME_STEP'],
        [1000000.0],
        ['MIN_TIME_STEP'],
        [10.0],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['1-Al'],
        ['2-Ba'],
        ['3-C'],
        ['4-Ca'],
        ['5-Cl'],
        ['6-Fe'],
        ['7-H'],
        ['8-Inrt'],
        ['9-K'],
        ['10-Mg'],
        ['11-Na'],
        ['12-O'],
        ['13-S'],
        ['14-Si'],
        ['15-Sr'],
        ['16-Zz'],
        ['PRESSURE1'],
        ['SATURATION1'],
    ],
    ELE_VALUES=[
        ['PERMEABILITY'],
        ['POROSITY'],
        ['VELOCITY'],
        ['VELOCITY1_X'],
        ['VELOCITY1_Y'],
        ['VELOCITY1_Z'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='VTK',
    TIM_TYPE=['STEPS', 250],
)
model.gem_init.add(
    name='bensan-dat',
    file_ext='.lst',
)
model.gem_init.read_file('bensan-dat.lst')
model.asc.add(
    name='lag2d_m_bIC_gem_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_bIC_gem_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_5-Cl_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_5-Cl_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_7-H_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_7-H_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_11-Na_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_11-Na_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_2-Ba_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_2-Ba_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_3-C_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_3-C_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_1-Al_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_1-Al_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_15-Sr_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_15-Sr_primary_value_2.asc')
model.asc.add(
    name='lag2d_m_bIC_gem_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_bIC_gem_1.asc')
model.asc.add(
    name='lag2d_m_porosity_gem_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_porosity_gem_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_6-Fe_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_6-Fe_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_16-Zz_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_16-Zz_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_13-S_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_13-S_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_3-C_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_3-C_primary_value_2.asc')
model.asc.add(
    name='lag2d_RICHARDS_FLOW_PRESSURE1_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_RICHARDS_FLOW_PRESSURE1_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_9-K_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_9-K_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_13-S_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_13-S_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_12-O_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_12-O_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_16-Zz_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_16-Zz_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_6-Fe_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_6-Fe_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_6-Fe_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_6-Fe_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_7-H_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_7-H_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_15-Sr_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_15-Sr_primary_value_3.asc')
model.asc.add(
    name='lag2d_m_xDC_gem_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_xDC_gem_1.asc')
model.asc.add(
    name='lag2d_m_porosity_gem_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_porosity_gem_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_4-Ca_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_4-Ca_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_10-Mg_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_10-Mg_primary_value_0.asc')
model.asc.add(
    name='lag2d_m_porosity_gem_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_porosity_gem_0.asc')
model.asc.add(
    name='lag2d_RICHARDS_FLOW_PRESSURE1_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_RICHARDS_FLOW_PRESSURE1_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_4-Ca_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_4-Ca_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_7-H_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_7-H_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_14-Si_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_14-Si_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_12-O_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_12-O_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_9-K_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_9-K_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_5-Cl_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_5-Cl_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_12-O_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_12-O_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_4-Ca_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_4-Ca_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_5-Cl_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_5-Cl_primary_value_3.asc')
model.asc.add(
    name='lag2d_time_gem_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_time_gem_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_10-Mg_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_10-Mg_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_8-Inrt_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_8-Inrt_primary_value_1.asc')
model.asc.add(
    name='lag2d_time_gem_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_time_gem_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_9-K_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_9-K_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_16-Zz_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_16-Zz_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_14-Si_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_14-Si_primary_value_0.asc')
model.asc.add(
    name='lag2d_m_fluid_volume_gem_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_fluid_volume_gem_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_5-Cl_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_5-Cl_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_7-H_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_7-H_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_16-Zz_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_16-Zz_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_11-Na_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_11-Na_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_13-S_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_13-S_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_14-Si_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_14-Si_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_6-Fe_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_6-Fe_primary_value_2.asc')
model.asc.add(
    name='lag2d_m_xDC_gem_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_xDC_gem_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_3-C_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_3-C_primary_value_0.asc')
model.asc.add(
    name='lag2d_m_xDC_gem_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_xDC_gem_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_11-Na_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_11-Na_primary_value_2.asc')
model.asc.add(
    name='lag2d_m_bIC_gem_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_bIC_gem_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_11-Na_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_11-Na_primary_value_0.asc')
model.asc.add(
    name='lag2d_RICHARDS_FLOW_PRESSURE1_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_RICHARDS_FLOW_PRESSURE1_primary_value_3.asc')
model.asc.add(
    name='lag2d_RICHARDS_FLOW_PRESSURE1_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_RICHARDS_FLOW_PRESSURE1_primary_value_1.asc')
model.asc.add(
    name='lag2d_m_fluid_volume_gem_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_fluid_volume_gem_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_9-K_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_9-K_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_8-Inrt_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_8-Inrt_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_1-Al_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_1-Al_primary_value_2.asc')
model.asc.add(
    name='lag2d_time_gem_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_time_gem_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_3-C_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_3-C_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_12-O_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_12-O_primary_value_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_2-Ba_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_2-Ba_primary_value_0.asc')
model.asc.add(
    name='lag2d_m_bIC_gem_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_bIC_gem_3.asc')
model.asc.add(
    name='lag2d_m_fluid_volume_gem_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_fluid_volume_gem_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_15-Sr_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_15-Sr_primary_value_1.asc')
model.asc.add(
    name='lag2d_m_fluid_volume_gem_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_fluid_volume_gem_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_2-Ba_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_2-Ba_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_10-Mg_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_10-Mg_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_1-Al_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_1-Al_primary_value_1.asc')
model.asc.add(
    name='lag2d_time_gem_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_time_gem_0.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_14-Si_primary_value_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_14-Si_primary_value_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_8-Inrt_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_8-Inrt_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_13-S_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_13-S_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_1-Al_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_1-Al_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_4-Ca_primary_value_2',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_4-Ca_primary_value_2.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_2-Ba_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_2-Ba_primary_value_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_15-Sr_primary_value_0',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_15-Sr_primary_value_0.asc')
model.asc.add(
    name='lag2d_m_xDC_gem_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_xDC_gem_3.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_10-Mg_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_10-Mg_primary_value_3.asc')
model.asc.add(
    name='lag2d_m_porosity_gem_1',
    file_ext='.asc',
)
model.asc.read_file('lag2d_m_porosity_gem_1.asc')
model.asc.add(
    name='lag2d_MASS_TRANSPORT_8-Inrt_primary_value_3',
    file_ext='.asc',
)
model.asc.read_file('lag2d_MASS_TRANSPORT_8-Inrt_primary_value_3.asc')
model.write_input()
model.run_model()
