
from slplat_utils import get_path_points,plot_info,last_point

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
#
# Misc Entries
#   pob   Point of beginning.  Segments before are not displayed, but used to calculate beginning of plat
#   array An array of entries describes a branch.  After the branch is displayed, the plotting resumes from start of branch



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
    #"s 68 00 w 6.75 delta 90 radius 30 length 5.67 cw",  #method 2 for a tangent curve
    "s 68 00 w 6.75 tangent right radius 30 length 5.67", #method 1 for a tangent curve

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
    "n 38 14 w 3.52",

]


#1963 Hoffmann
#parcel 2 easement
path_1963_hoffmann_parcel_2 = [
    "n 38 49 04 w 116.78",
    "pob",  # point of beginning.  Previous entries are not displayed
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

path_1964_hoffmann_subdivides_54_56 = [
    "s 35 40 w 15",
    "s 45 53 e 78.37",
    "n 72 41 20 e 12.74",
    "n 85 24 10 e 37.15",
    "n 85 24 10 e 2.27",
    "pob",
    "n 85 24 10 e 34.50",
    ["s 18 2 15 e 131.28"], # A branch is displayed.
    "n 85 24 10 e 4.27",    # This entry resumes from beginning of branch
    "n 83 11 05 e 23.75",
    "s 38 49 04 e 116.78",
    "s 65 27 w 45",
    "s 48 04 w 27.5",
    ["n 18 2 15 w 131.28"],
    "s 48 04 w 68.52",
    "n 8 10 30 w 166.19",

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
    "n 39 10 19 w 116.33",    # this is segment leading to a branch point
    [path_proposed_parcel_c], # branch happens here
    "s 83 11 5 w 24.32",      # this line continues on from the branch point
    [path_split_ab],
    "s 85 24 10 w 18.28",
    #[marker_vertical],
    "s 85 24 10 w 60.91",
    "s 72 41 20 w 12.74",
    "n 45 53 w 78.37 delta 74 13 43 radius 15 length 19.43 ccw",  # an example of non tangent curve
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

path_2016_Pyle_easement = [
    # Beginning at the most western corner of Parcel A, as shown on 
    # Lot Line Adjustment 314 recorded November 16, 2016, at Series 
    # Number 2016299641, in Official Records of the County
    # of Alameda, thence along the southwestern, southern and eastern lines of said Parcel A, 
    #
    # the following courses: 
    #
    # South 45° 53' East, 78.37 feet; 
    "s 45 53 e 78.37",
    # North 72° 41' 20" East, 12.74 feet; 
    "n 72 41 20 e 12.74", 
    # North 85° 24' 10" East, 79.19 feet; and 
    "n 85 24 10 e 79.19",
    # North 04° 05" 01' West, 15.00 feet; thence 
    "n 04 05 01 w 15.00",
    # South 85° 24' 10" West, 42.15 feet; thence 
    "s 85 24 10 w 42.15",
    # North 88° 52' 35" West, 45.49 feet; thence 
    "n 88 52 35 w 45.49",
    # North 45° 53' 00" West, 47.15 feet to the northern line of said Parcel A; 
    "n 45 53 00 w 47.15",
    # thence along the northern lines of Parcel A the following courses: 
    # South 86° 28' 37" West, 6.87 feet; and 
    "s 86 28 37 w 6.87",
    # along the arc of a curve concave to the north, 
    #    with a tangent bearing of South 51 ° 26' 18" West, 
    #    a radius of 15.00 feet, and a
    #    central angle of 74° 13' 43", 
    #    an arc length of 19.43 feet to the_point of beginning.
    "s 51 26 18 w tangent right radius 15 length 19.43"
]

path_54_Pano_easement = [
    # A portion of that certain parcel of land described in Deed from the Regents of the University of California, a corporation, to Michael L. Kamm and wife, dated July 15, 1953, recorded July 28, 1953, under Recoder's Series No. AH-67256, Book 7092, Page 477, Alameda County Records, bounded as follows: 
    # Beginning at Station 14 in the center line of Panoramic Way, as said Station and Way are shown on the map of "University Terrace", filed August 14, 1888, Map Book 10, Page 30, Alameda County Records; 
    # running thence along the exterior boundary line of the said Kamm parcel of land the two following courses and distance; 
    # South 35° 40' West 15.00 feet to an angle point thereon and thence
    "s 35 40 w 15.00", 
    # South 45° 53' East 78.37 feet; thence 
    "s 45 53 e 78.37",
    # North 72° 41' 20" East 12.74 feet; thence 
    "n 72 41 20 e 12.74",
    # North 85° 24' 10" East 37.15 feet to the most Western corner of that certain parcel of land designated as Parcel Three in Quitclaim Deed from Anne Barnett to Michael L. Kamm and Lenore K. Kamm, his wife, dated April 7, 1959, recorded June 18, 1959, under Recorder's Series No. AQ-72502, Book 9063, Page 509, Alameda County Records; thence 
    "n 85 24 10 e 37.15",
    # along the Southern boundary line thereof, 
    # North 85° 24' 10" East 22.27 feet to the Northwestern corner of that certain parcel of land designated as Parcel Two in Quitclaim Deed from Anne Barnett to Michael L. Kamm and wife, under Recorder's Series No. AQ-72502, Alameda County Records; thence 
    "n 85 24 10 e 22.27",
    # along the Northern boundary line thereof the two following courses and distances; 
    # North 85° 24' 10" East 39.77 feet and thence 
    "n 85 24 10 e 39.77",
    # North 83° 11' 05" East 23.75 feet to a point on the Southwestern boundary line of that certain parcel of land designated as Parcel One in Deed from Michael L. Kamm and wife, to Theresa Clark, dated August 27, 1953, recorded September 1, 1953, under Recorder's No. AH-77538, Book 7121, Page 221, Alameda County Records; thence 
    # Likely Error in the description: 23.75 seems too long, changed to 3.75
    "n 83 11 05 e 3.75",
    # along the said last mentioned line 
    # North 38° 49' 04" West 20.89 feet to the most Eastern corner of that certain parcel of land designated as Parcel One in Deed from Michael L. Kamm and wife, to Thomas H. Arkley and wife, dated September 30, 1958, recorded November 6, 1958, under Recorder's Series No. AP-115872, Book 8837, Page 97, Alameda County Records; thence 
    "n 38 49 04 W 20.89",
    # along the exterior boundary line of the said last, mentioned parcel of land the following courses and distances; 
    # South 680 00' West 6.70 feet and thence 
    "S 68 00 W 6.70",
    # Westerly along the arc of a curve to the right with a radius of 30.00 feet tangent to the said last mentioned course, a distance of 5.67 feet to the most Eastern corner of that certain easement designated as Parcel Two, in the said last mentioned Deed to Thomas H. Arkley and wife, under Recorder's Series No. AP-115872, Alameda County Records; thence 
    "S 68 00 W tangent right radius 30 length 5.67",
    # along the Northern boundary line thereof the two following courses and distance: 
    # South 850 24' 10" West 61.19 feet, and thence 
    "S 85 24 10 W 61.19",
    # South 890 12' 20" West 20.89 feet to the most Eastern corner of that certain parcel of land described in Quitclaim Deed from Thomas E. Arkley and wife, to Michael L. Kamm and wife, dated September 30, 1958, recorded November 6, 1958, under Recorder Series No. AP-115870, Book 8837, Page 95, Alameda County Records; thence 
    "S 89 12 20 W 20.89",
    # along the exterior boundary line of the said last mentioned parcel of land the two following courses and distances; 
    # Westerly and Northwesterly along the arc of a curve to the right with a radius of 17.25 feet, tangent to the said last mentioned course, 13.52 feet and thence 
    "S 89 12 20 W tangent right radius 17.25 length 13.52",
    # North 450 53' West 44.55 feet to the most Western corner of the said last mentioned parcel of land; thence 
    "N 45 53 W 44.55",
    # along the Northern and Northeastern boundary lines of the said parcel of land described in Deed to Michael L. Kamm and wife, under Recorder's Series No. AH-67256, Alameda County Records, being also the Southern and Southwestern lines of Panoramic Way as described in instrument to City of Berkeley; dated February 1, 1936, recorded June 17, 1936, under Recorder's Series No. GG-31103, Book 3332, Page 308, Alameda County Records, the two following courses and distances; 
    # South 860 28' 37" West 2.85 feet and thence 
    "S 86 28 37 W 2.85",
    # North 380 39' 45" West 11.48 feet; thence 
    "N 38 39 45 W 11.48",
    # North 380 14' West 3.52 feet to the point of beginning.
    "N 38 14 W 3.52"
]

path_pob_Arkley_Morse_Parcel_3 = [ # starts at station 14
    # South 35° 40' West 15.00 feet to an angle point thereon and thence
    "s 35 40 w 15.00", 
    # South 45° 53' East 78.37 feet; thence 
    "s 45 53 e 78.37",
    # North 72° 41' 20" East 12.74 feet; thence 
    "n 72 41 20 e 12.74",
    # North 85° 24' 10" East 37.15 feet to the most Western corner of that certain parcel of land designated as Parcel Three in Quitclaim Deed from Anne Barnett to Michael L. Kamm and Lenore K. Kamm, his wife, dated April 7, 1959, recorded June 18, 1959, under Recorder's Series No. AQ-72502, Book 9063, Page 509, Alameda County Records; thence 
    "n 85 24 10 e 37.15"
    ]

path_radius_debug = [
    "s 45 w 10",
    "n 45 w 10",
    "n 45 e 10",
    "s 45 e 10"
]
path_radius_debug = [
    "s 55 w 10",
    "n 65 w 10",
    "n 55 e 10",
    "s 65 e 10"
]



#setup various origins

orig_station_14 = (0,0)
orig_unknown = [0,25]

segments = get_path_points(orig_station_14,path_pob_parcel_b)
orig_parcel_b = last_point(segments)

segments = get_path_points(orig_station_14,path_pob_nw_parcel_c)
orig_nw_parcel_c = last_point(segments)

segments = get_path_points(orig_station_14,path_pob_1963_hoffman_parcel_3_se_corner)
orig_1963_hoffman_parcel_3_se_corner = last_point(segments)
orig_se_crnr = orig_1963_hoffman_parcel_3_se_corner

segments = get_path_points(orig_station_14, ["s 35 40 w 15"])
pob_parcel_A_2016 = last_point(segments)

segments = get_path_points(orig_station_14, path_pob_Arkley_Morse_Parcel_3)
pob_Arkley_Morse_Parcel_3 = last_point(segments)

pix = [
    plot_info("1963 Hoffman Parcel 1",              orig_station_14,     path_1963_hoffmann_parcel_1),
    plot_info("1963 Hoffman Parcel 2 easement",     orig_se_crnr,        path_1963_hoffmann_parcel_2),
    plot_info("1963 Hoffman Parcel 3",              orig_station_14,     path_1963_hoffmann_parcel_3),
    plot_info("1964 Hoffmann divides 54 56",        orig_station_14,     path_1964_hoffmann_subdivides_54_56),
    plot_info("1965 Morse Parcel A",                orig_station_14,     path_1965_Morse_Deed_Parcel_A),
    plot_info("1965 Morse Easement",                orig_station_14,     path_1965_Morse_Easement),
    plot_info("1969 Arkley Morse Parcel 1",         orig_station_14,     path_1969_Arkley_Morse_Parcel_1),
    plot_info("1969 Arkley Morse Parcel 2",         orig_station_14,     path_1969_Arkley_Morse_Parcel_2),
    plot_info("1969 Arkley Morse Parcel 3",         pob_Arkley_Morse_Parcel_3,           path_1969_Arkley_Morse_Parcel_3),
    plot_info("1977 Kamm Morse PD 120 Parcel C",    orig_station_14,     path_1977_pd_120_parcel_c),
    plot_info("1999 Morse Morse Parcel B",          orig_nw_parcel_c,    path_1999_Morse_Morse_Parcel_B),
    plot_info("1999 Morse Morse Parcel B Easement", orig_parcel_b,       path_1999_Morse_Morse_Parcel_B_Easement),
    plot_info("2016 Lot Line Adjustment",           orig_station_14,     path_2016_lot_line),
    plot_info("2016 Pyle Easement",                 pob_parcel_A_2016,   path_2016_Pyle_easement),
    plot_info("2003 54 Panoramic Easement",         orig_station_14,    path_54_Pano_easement),
    plot_info("path radius_debug",                  orig_station_14,     path_radius_debug),
]
