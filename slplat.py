# displays plats which are often found in property deeds.


import streamlit as st
import math
import matplotlib.pyplot as plt
import matplotlib as mpl

from slplat_utils import get_path_points

#import plat descriptors from definition file here
from myproperty import pix

st.set_page_config(layout='wide')
mpl.rcParams['lines.linewidth'] = 1

fig, ax = plt.subplots()
ax.axis('equal')

for pi in pix:
    if st.sidebar.checkbox(pi.text,False):
        pi.selected = True
        segments = get_path_points(pi.origin,pi.path,1,-1) # change y coordinate to match matplotlib
        for segment in segments:
            ax.plot(segment[0],segment[1])

        if pi.aux_info:
            ax.text(pi.aux_info['pos_x'],pi.aux_info['pos_y'],pi.aux_info['text'])
    else:
        pi.selected = False


st.pyplot(fig)

for pi in pix:
    if pi.selected:
        st.text('{}: {} {}'.format(pi.text,pi.origin,pi.path))

