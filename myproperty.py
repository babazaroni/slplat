
from slplat_utils import get_path_points

marker_vertical = ["n 0 w 5"]

path_proposed_parcel_c = ["n 55 21 57 e 144.73"]
path_split_ab = ["n 4 5 1 w 39.37","n 88 20 9 e 4.16","n 6 26 34 e 28.2","n 65 6 36 e 22.93","n 25 w 42"]

path_2016_lot_line = [
    "s 38 14 e 3.52",
    "s 38 39 45 e 11.48",
    "pob",
    "n 86 28 37 e 20.26",   #L8
    "n 39 52 45 e 24",      #L7
    "n 62 51 e 115.58",
    "s 79 4 21 e 26",      #L15
    "s 84 4 31 e 61.02",
    "n 68 28 33 e 55.22",
    "s 4 55 w 41.32",
    "s 4 55 w 112.86",
    "s 31 8 24 w 70.1",
    "n 39 10 19 w 116.33",
    [path_proposed_parcel_c],
    "s 83 11 5 w 24.32",
    [path_split_ab],
    "s 85 24 10 w 18.28",
    #[marker_vertical],
    "s 85 24 10 w 60.91",
    "s 72 41 20 w 12.74",
    "n 45 53 w 78.37"


]

path_1977_pd_120_parcel_c = [
    "s 38 14 e 3.52",
    "s 38 39 45 e 11.48",
    "n 86 28 37 e 20.26",
    "n 39 52 45 e 24",
    "n 62 51 e 70",
    "n 62 51 e 45.58",
    "s 79 4 21 e 26",
    "s 84 4 31 e 48.35",
    "pob",
    "s 84 4 31 e 12.67",
    "n 68 58 40 e 55.73", # could be 55.23
    "s 6 10 w 154.66",
    "n 33 3 14 w 112.52",
    "n 15 7 59 e 42.7"
]

#1963 Hoffmann
#parcel 1
path_1963_hoffmann_parcel_1 = [
    "s 35 40 w 15",
    "s 45 53 e 78.37",
    "n 72 41 20 e 12.74",
    "n 85 24 10 e 37.15",
    "n 85 24 10 e 2.27",
    "n 85 24 10 e 39.77",
    "n 83 11 05 e 23.75",
    "n 38 49 04 w 20.89",
    "s 68 00 w 6.75",

    #r 30 5.67
    "s 73.414451164 w 5.66156468111",

    "n 7 26 30 e 19.92",
    "n 8 48 w 12",

    #r 20 31.42
    "n 36.2058348075 e 28.2871514749",

    "n 81 12 e 36",

    #r 20 23.02
    "s 65.8262788902 e 21.7701727535",

    "s 33 03 14 e 112.52",
    "n 5 10 e 154.66",
    "s 68 58 40 w 55.23",
    "n 84 04 31 w 61.02",
    "n 79 04 21 w 26",
    "s 62 51 w 115.58",
    "s 39 52 45 w 24",
    "s 86 28 37 w 20.26",
    "n 38 39 45 w 11.48",
    "n 38 14 w 3.52"
]

#1963 Hoffmann
#parcel 2 easement
path_1963_hoffmann_parcel_2 = [
    "n 38 49 04 w 116.78",
    "pob",
    "n 38 49 04 w 15.67",
    "n 68 0 e 48.59",

    #l 10 3.49
    "n 58.001886475 e 3.47231505162",

    "n 48 0 e 25.48",
    "s 33 04 14 e 15.19",
    "s 48 00 w 23.12",

    #r 25 8.73
    "s 58.003843103 w 8.68571165299",
    "s 68 00 w 44.06",
]


#1963 Hoffmann
#parcel 3
path_1963_hoffmann_parcel_3 = [
    "s 35 40 w 15",
    "s 45 53 e 78.37",
    "n 72 41 20 e 12.74",
    "n 85 24 10 e 37.15",
    "n 85 24 10 e 2.27",
    "pob",
    "n 85 24 10 e 39.77",
    "n 83 11 05 e 23.75",
    "s 38 49 04 e 116.78",
    "s 65 27 w 45",
    "s 48 04 w 96.02",
    "n 8 10 30 w 166.19",
]

path_pob_1963_hoffman_parcel_3_se_corner = [
       "s 35 40 w 15",
    "s 45 53 e 78.37",
    "n 72 41 20 e 12.74",
    "n 85 24 10 e 37.15",
    "n 85 24 10 e 2.27",
    "n 85 24 10 e 39.77",
    "n 83 11 05 e 23.75",
    "s 38 49 04 e 116.78",
]

#1965 Morse Deed Parcel A
path_1965_Morse_Deed_Parcel_A = [
    "s 35 40  w 15",
    "s 45 53 e 78.37",
    "n 72 41 20 e 12.74",
    "n 85 24 10 e 60.91",

    "n 8 48 w 62.11",
    "n 5 42 w 36.75",

    "s 62 51 w 70",
    "s 39 52 45 w 24",
    "s 86 28 37 w 20.26",
    "n 38 39 45 w 11.48",
    "n 38 14 w 3.52"
]

#1965 Morse Deed Easement
path_1965_Morse_Easement = [
    "s 35 40  w 15",
    "s 45 53 e 78.37",
    "n 72 41 20 e 12.74",
    "n 85 24 10 e 60.91",

    "n 8 48 w 42.11",
    "s 11 w 21.42",

    "s 71 40 4 w 14.18",
    "s 85 24 10 w 35.99",

    #"s 85 24 10 w arc r 17 17",
    "n 65.9493324657 w 16.3004683125",

    "n 45 53 w 40.14",

    "s 86 28 37 w 6.87",
    "n 38 39 45 w 11.48",
    "n 38 14 w 3.52"

]

# 1969 Arkley to Morse
# Parcel 1

path_1969_Arkley_Morse_Parcel_1 = [
    "s 35 40 w 15",
    "s 45 53 e 78.37",
    "n 72 41 20 e 12.74",
    "n 85 24 10 e 37.15",
    "n 85 24 10 e 2.27",
    "n 85 24 10 e 39.77",
    "n 83 11 05 e 23.75",
    "pob",
    "n 38 49 4 w 20.89",
    "s 68 00 w 6.75",

    #r 30 5.67
    's 73.414451164 w 5.66156468111',

    "n 7 26 30 e 19.92",
    "n 8 48 w 12",

    #r 20 31.42
    'n 36.2058348075 e 28.2871514749',

    "n 81 12 e 36",

    #r 20 23.02
    "s 65.8262788902 e 21.7701727535",
    #S 43 50 37 E 7.63
    #S 65 49 34 E 7.63
    #S 87 48 31 E 7.63

    "s 33 3 14 e 112.52",
    "s 31 10 w 70",
    "n 38 49 4 w 116.78"
]
# 1969 Arkley to Morse
#parcel 2
path_1969_Arkley_Morse_Parcel_2 = [
    "s 35 40 w 15",
    "s 45 53 e 78.37",
    "n 72 41 20 e 12.74",
    "n 85 24 10 e 37.15",
    "n 85 24 10 e 2.27",
    "n 85 24 10 e 39.77",
    "n 83 11 5 e 23.75",
    "n 38 49 4 w 20.89",
    "s 68 0 w 6.75",

    #r 30 5.67
    #'s 73.414451164 w 5.66156468111',
    "S 69 48 17 W 1.89",
    "S 73 24 52 W 1.89",
    "S 77 1 26 W 1.89",

    "s 85 24 10 w 61.19",
    "s 89 12 20 w 20.89",

    #r 17.25 13.52
    #"n 68.3411418642 w 13.1765960954",
    "N 83 18 36 W 4.49",
    "N 68 20 28 W 4.49",
    "N 53 22 20 W 4.49",

    "n 45 53 w 44.55",
    "s 86 28 37 w 2.85",
    "n 38 39 45 w 11.48",
    "n 38 14 w 3.52"
]
# 1969 Arkley to Morse
#parcel 3
path_1969_Arkley_Morse_Parcel_3 = [
    "s 8 10 30 e .27",
    "n 85 24 10 e 39.77",
    "n 83 11 5 e 23.75",
    "s 68 0 w 11.8",

    #r 50 9.45
    #"s 73.414451164 w 9.43594113518",
    "S 69 48 17 W 3.15",
    "S 73 24 52 W 3.15",
    "S 77 1 26 W 3.15",

    #S 77 1 26 W 3.15
    #S 73 24 52 W 3.15
    #S 69 48 17 W 3.15

    "s 78 50 w 42.06",
    "n 8 10 30 w 9.73",
]

#1999 57 Panoramic
#Parcel B
path_1999_Morse_Morse_Parcel_B = [
    "s 5 10 w 41.32",
    "s 58 12 20 w 145.66",
    "s 38 49 4 e 6.61",
    "s 83 11 5 w 23.75",
    "s 85 24 10 w 18.28",
    "n 8 48 w 42.1",
    "n 38 14 44 e 26.95",
    "n 6 e 45",
    "n 62 51 e 24.58",
    "s 79 4 21 e 26",
    "s 84 4 31 e 61.02",
    "n 68 58 40 e 55.23"
]

#1999 57 Paoramic
#turn around easement
path_1999_Morse_Morse_Parcel_B_Easement = [
    "n 8 48 w 15.03",
    "pob",
    "n 85 24 10 e 19.38",
    "n 7 27 13 e 20.03",
    "n 8 48 w 7.43",
    "s 85 24 10 w 25",
    "s 8 48 e 27.07"
]



path_pob_parcel_b = [
    "s 35 40  w 15",
    "s 45 53 e 78.37",
    "n 72 41 20 e 12.74",
    "n 85 24 10 e 60.91",
]

path_pob_nw_parcel_c = [ # from pd 120
    "s 38 14 e 3.52",
    "s 38 39 45 e 11.48",
    "n 86 28 37 e 20.26",
    "n 39 52 45 e 24",
    "n 62 51 e 70",
    "n 62 51 e 45.58",
    "s 79 4 21 e 26",
    "s 84 4 31 e 48.35",
    "s 84 4 31 e 12.67",
    "n 68 58 40 e 55.73", # could be 55.23
]


def last_point(segments):
    seg = segments[-1]
    return [seg[0][-1],seg[1][-1]]


pob_station_14 = (0,0)

segments = get_path_points(pob_station_14,path_pob_parcel_b,1,-1) # change y coordinate to match matplotlib
pob_parcel_b = last_point(segments)

segments = get_path_points(pob_station_14,path_pob_nw_parcel_c,1,-1) # change y coordinate to match matplotlib
pob_nw_parcel_c = last_point(segments)

segments = get_path_points(pob_station_14,path_pob_1963_hoffman_parcel_3_se_corner,1,-1)
pob_1963_hoffman_parcel_3_se_corner = last_point(segments)
pob_se_crnr = pob_1963_hoffman_parcel_3_se_corner

pob_unknown = [0,25]


unknowwn_origin_info = {'pos_x':-10,'pos_y':30,'text':'unknown origin'}

class plot_info():
    def __init__(self,text,origin,path,aux_info = None):
        self.text = text
        self.origin = origin
        self.path = path
        self.selected = False
        self.aux_info = aux_info

pix = []

pix.append(plot_info("1963 Hoffman Parcel 1",           pob_station_14,     path_1963_hoffmann_parcel_1))
pix.append(plot_info("1963 Hoffman Parcel 2 easement",  pob_se_crnr,        path_1963_hoffmann_parcel_2))
pix.append(plot_info("1963 Hoffman Parcel 3",           pob_station_14,     path_1963_hoffmann_parcel_3))
pix.append(plot_info("1965 Morse Parcel A",             pob_station_14,     path_1965_Morse_Deed_Parcel_A))
pix.append(plot_info("1965 Morse Easement",             pob_station_14,     path_1965_Morse_Easement))
pix.append(plot_info("1969 Arkley Morse Parcel 1",      pob_station_14,     path_1969_Arkley_Morse_Parcel_1))
pix.append(plot_info("1969 Arkley Morse Parcel 2",      pob_station_14,     path_1969_Arkley_Morse_Parcel_2))
pix.append(plot_info("1969 Arkley Morse Parcel 3",      pob_unknown,        path_1969_Arkley_Morse_Parcel_3, unknowwn_origin_info))
pix.append(plot_info("1977 Kamm Morse PD 120 Parcel C", pob_station_14,     path_1977_pd_120_parcel_c))
pix.append(plot_info("1999 Morse Morse Parcel B",       pob_nw_parcel_c,    path_1999_Morse_Morse_Parcel_B))
pix.append(plot_info("1999 Morse Morse Parcel B Easement",pob_parcel_b,     path_1999_Morse_Morse_Parcel_B_Easement))
pix.append(plot_info("2016 Lot Line Adjustment",        pob_station_14,     path_2016_lot_line))