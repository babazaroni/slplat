
from slplat_utils import get_path_points

# Straignt Lines
#
# The standard way is to specify a bearig by it's offset from north or south and the direction of the offset, west or east.
# The offset is specified by degrees, followed by optional minutes, seconds and even finer divisions by 60 if desired
# After the bearing, you can specify the distance.

# Circular Curves
#
# There are two ways to enter curves:
# 1 if your curve is tangent to the current bearing, then specify tangent and give direction, left or right, radius and length
# 2 if your curve is not tangent, then you can specify the bearing to the center of the circle with the delta from the current bearing
#   Then specify radius and length, followed by the direction of the curve clockwise(cw) or counter clockwise(ccw)
#   You can specify a tangent curve with delta by specifying "delta 90" or "delta 270"



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
    #"s 68 00 w 6.75 delta 90 radius 30 length 5.67 cw",
    "s 68 00 w 6.75 tangent right radius 30 length 5.67",

    "n 7 26 30 e 19.92",

    #"n 8 48 w 12 delta 90 radius 20 length 31.42 cw",
    "n 8 48 w 12 tangent right radius 20 length 31.42",


    #"n 81 12 e 36 delta 90 radius 20 length 23.02 cw",
    "n 81 12 e 36 tangent right radius 20 length 23.02",


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
    "n 68 0 e 48.59 tangent left radius 10 length 3.49",

    "n 48 0 e 25.48",
    "s 33 04 14 e 15.19",
    "s 48 00 w 23.12 tangent right radius 25 length 8.73",
    
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

    #"s 85 24 10 w 35.99 delta 90 radius 17 length 17 cw",
    "s 85 24 10 w 35.99 tangent right radius 17 length 17",

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
    #"s 68 00 w 6.75 delta 90 radius 30 length 5.67 cw",
    "s 68 00 w 6.75 tangent right radius 30 length 5.67",

    "n 7 26 30 e 19.92",
    #"n 8 48 w 12 delta 90 radius 20 length 31.42 cw",
    "n 8 48 w 12 tangent right radius 20 length 31.42",

    #"n 81 12 e 36 delta 90 radius 20 length 23.02 cw",
    "n 81 12 e 36 tangent right radius 20 length 23.02",

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
    #"s 68 0 w 6.75 delta 90 radius 30 length 5.67 cw",
    "s 68 0 w 6.75 tangent right radius 30 length 5.67",

    "s 85 24 10 w 61.19",
    #"s 89 12 20 w 20.89 delta 90 radius 17.25 length 13.52 cw",
    "s 89 12 20 w 20.89 tangent right radius 17.25 length 13.52",

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
    #"s 68 0 w 11.8 delta 90 radius 50 length 9.45 cw",
    "s 68 0 w 11.8 tangent right radius 50 length 9.45",

    "s 78 50 w 42.06",
    "n 8 10 30 w 9.73",
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
    "n 45 53 w 78.37 delta 74 13 43 radius 15 length 19.43 ccw",
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

path_radius_debug = [
    "s 0 w 20",
    "s 90 w 20",
#    "n 0 e 20 delta 90 radius 10 length 62.83 ccw",

#    "n 0 e 20 delta 90 radius 10 length 31.4 ccw",
 #   "n 0 e 20 delta 90 radius 10 length 15.7079632679 cw"
    "n 0 e 20 tangent left radius 10 length 15"

]


def last_point(segments):
    seg = segments[-1]
    return [seg[0][-1],seg[1][-1]]

#setup various origins

orig_station_14 = (0,0)

segments = get_path_points(orig_station_14,path_pob_parcel_b,1,-1) # change y coordinate to match matplotlib
orig_parcel_b = last_point(segments)

segments = get_path_points(orig_station_14,path_pob_nw_parcel_c,1,-1) # change y coordinate to match matplotlib
orig_nw_parcel_c = last_point(segments)

segments = get_path_points(orig_station_14,path_pob_1963_hoffman_parcel_3_se_corner,1,-1)
orig_1963_hoffman_parcel_3_se_corner = last_point(segments)
orig_se_crnr = orig_1963_hoffman_parcel_3_se_corner

orig_unknown = [0,25]

unknowwn_origin_info = {'pos_x':-10,'pos_y':30,'text':'unknown origin'}

class plot_info():
    def __init__(self,text,origin,path,aux_info = None):
        self.text = text
        self.origin = origin
        self.path = path
        self.selected = False
        self.aux_info = aux_info

pix = []

pix.append(plot_info("1963 Hoffman Parcel 1",           orig_station_14,     path_1963_hoffmann_parcel_1))
pix.append(plot_info("1963 Hoffman Parcel 2 easement",  orig_se_crnr,        path_1963_hoffmann_parcel_2))
pix.append(plot_info("1963 Hoffman Parcel 3",           orig_station_14,     path_1963_hoffmann_parcel_3))
pix.append(plot_info("1965 Morse Parcel A",             orig_station_14,     path_1965_Morse_Deed_Parcel_A))
pix.append(plot_info("1965 Morse Easement",             orig_station_14,     path_1965_Morse_Easement))
pix.append(plot_info("1969 Arkley Morse Parcel 1",      orig_station_14,     path_1969_Arkley_Morse_Parcel_1))
pix.append(plot_info("1969 Arkley Morse Parcel 2",      orig_station_14,     path_1969_Arkley_Morse_Parcel_2))
pix.append(plot_info("1969 Arkley Morse Parcel 3",      orig_unknown,        path_1969_Arkley_Morse_Parcel_3, unknowwn_origin_info))
pix.append(plot_info("1977 Kamm Morse PD 120 Parcel C", orig_station_14,     path_1977_pd_120_parcel_c))
pix.append(plot_info("1999 Morse Morse Parcel B",       orig_nw_parcel_c,    path_1999_Morse_Morse_Parcel_B))
pix.append(plot_info("1999 Morse Morse Parcel B Easement",orig_parcel_b,     path_1999_Morse_Morse_Parcel_B_Easement))
pix.append(plot_info("2016 Lot Line Adjustment",        orig_station_14,     path_2016_lot_line))
pix.append(plot_info("path radius_debug",               orig_station_14,     path_radius_debug))
