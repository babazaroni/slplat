# displays plats which are often found in property deeds.


import streamlit as st
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from slplat_utils import *

#import your plat descriptors from your definition file here
from myproperty import pix


st.set_page_config(layout='wide')

mpl.rcParams['lines.linewidth'] = 1



print('starting')

fig3, ax3 = plt.subplots()
ax3.axis('equal')


for pi in pix:
    if st.sidebar.checkbox(pi.text,False):
        pi.selected = True
        segments = get_path_points(pi.origin,pi.path,1,-1) # change y coordinate to match matplotlib
        for segment in segments:
            ax3.plot(segment[0],segment[1])

        if pi.aux_info:
            ax3.text(pi.aux_info['pos_x'],pi.aux_info['pos_y'],pi.aux_info['text'])
    else:
        pi.selected = False

st.pyplot(fig3)

for pi in pix:
    if pi.selected:
        st.text('{}: {} {}'.format(pi.text,pi.origin,pi.path))

