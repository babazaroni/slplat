# displays plats which are often found in property deeds.


import streamlit as st
import math
import matplotlib.pyplot as plt
import matplotlib as mpl

from slplat_utils import get_path_points,get_as_mb

#import plat descriptors from definition file here
from myproperty import pix
#pix = []

st.set_page_config(layout='wide')
mpl.rcParams['lines.linewidth'] = 1

fig, ax = plt.subplots()
ax.axis('equal')

#segments = {}
#segments['X']= [0,1,23,78]
#segments['Y']= [0,1,14,23]
#ax.plot([0,1],[0,1])

for pi in pix:
    if st.sidebar.checkbox(pi.text,False):
        pi.selected = True
        pi.segments,properties = get_path_points(pi.origin,pi.path)

        for segment,property in zip(pi.segments,properties):
            ax.plot(segment['x'],segment['y'],**property)

        if pi.aux_info:
            ax.text(pi.aux_info['pos_x'],pi.aux_info['pos_y'],pi.aux_info['text'])
    else:
        pi.selected = False


st.pyplot(fig)

for pi in pix:
    if pi.selected:
        st.text(pi.text)
        mb_text = ""
        for mb in get_as_mb(pi.segments):
            mb_text += mb + '\n'
        st.text(mb_text)

