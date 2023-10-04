import streamlit as st
import  streamlit_vertical_slider  as sv
from colour import SDS_ILLUMINANTS
import colour
from colour import colour_rendering_index, sd_blackbody,SpectralDistribution,XYZ_to_RGB,sd_to_XYZ
from colour.quality import spectral_similarity_index
from colour.plotting import plot_visible_spectrum,plot_single_sd,plot_single_colour_swatch
import matplotlib.pyplot as plt
import pandas as pd
def sd_RGB(sd):
    illuminant = SDS_ILLUMINANTS['D65']
    cmfs = colour.MSDS_CMFS["CIE 1931 2 Degree Standard Observer"]
    xyz = sd_to_XYZ(sd,cmfs, illuminant)

    # Convert XYZ to RGB
    rgb = colour.XYZ_to_sRGB(xyz )    
    return rgb

sd = SDS_ILLUMINANTS["FL2"]
cri = colour_rendering_index(sd)
d65 = SDS_ILLUMINANTS['D65']
k6500 = sd_blackbody(6500)
#cri = colour_rendering_index(k6500)
ssi = spectral_similarity_index(sd,d65)
led_co = st.sidebar.empty()
led_c1,led_c2 = led_co.columns([1,5])
i=0
led_c1.color_picker(f'**Led{i+1}**', '#aac988')
led_c2.slider('**CRI**', min_value=0., max_value=1., step=0.01)
st.markdown(f'## CRI= :blue[{cri:.2f}] SSI(d65)=:blue[{ssi:.2f}]')
#sd = SpectralDistribution(d65, name='D65')
figure, _axes = plot_single_sd(d65,show_plot = False)
st.pyplot(figure)
sd_RGB = sd_RGB(sd)
st.write(sd_RGB)
figure, _axes = plot_single_colour_swatch(sd_RGB,show_plot = False)
st.pyplot(figure)
#sd_RGB = sd.to_RGB()
