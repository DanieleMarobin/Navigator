# https://share.streamlit.io/

# https://share.streamlit.io/danielemarobin/monitor/main/Home.py

# Bloomberg API installing process
# https://discuss.streamlit.io/t/installing-packages-from-the-web/27537

# pipreqs --encoding=utf8

import streamlit as st

st.set_page_config(page_title="Navigator",layout="wide",initial_sidebar_state="expanded")

st.markdown("# Navigator")

st.markdown("---")
st.markdown("### Price Analysis")

link='''Seasonals: [Seasonals](https://danielemarobin-seasonals-home.streamlit.app/)'''
roadmap='''
* :green[Done]:
    * Added controls on forward onth range and past years
    * Made sure that the seasonal never goes further than First Notice Day
* :red[To Do]:
    * Visualize and Analyse fund roll
    * Add statistics at the bottom
    * Easily select successful and unsuccessful years        
'''
st.markdown(link)

with st.expander('Seasonals Roadmap'):
    st.markdown(roadmap)

link='* Trade Radar: [Trade Radar](https://danielemarobin-traderadar-home.streamlit.app/)'
st.markdown(link)

link='* Price Models: [Price Models](https://danielemarobin-pricemodels-home.streamlit.app/)'
st.markdown(link)


st.markdown("---")
st.markdown("### Yield Models")

link='* Safra Corn (BRA): [Safra Corn (BRA)](https://danielemarobin-brasafracornyieldmodel-home.streamlit.app/)'
st.markdown(link)

link='* Safrina Corn (BRA): Coming Soon... (I need to rework it, to harmonize it with all the other genetic algo ones)'
st.markdown(link)


st.markdown("---")
st.markdown("### Crops")

link='* Crop Progress and Conditions: [Crop Progress and Conditions](https://danielemarobin-cropprogress-home.streamlit.app/)'
st.markdown(link)

# link='Trade Flow: [Trade Flow](https://danielemarobin-tradeflow-home.streamlit.app/)'
# st.markdown(link)


# st.sidebar.markdown("# Navigator")