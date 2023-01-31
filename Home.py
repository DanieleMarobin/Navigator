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

link='Seasonals: [Seasonals](https://danielemarobin-seasonals-home.streamlit.app/)'
st.markdown(link)

link='Trade Radar: [Trade Radar](https://danielemarobin-traderadar-home.streamlit.app/)'
st.markdown(link)

link='Price Models: [Price Models](https://danielemarobin-pricemodels-home.streamlit.app/)'
st.markdown(link)


st.markdown("---")
st.markdown("### Yield Models")

link='Safra Corn Yield Model: [Safra Corn Yield Model](https://danielemarobin-brasafracornyieldmodel-home.streamlit.app/)'
st.markdown(link)


st.markdown("---")
st.markdown("### Crops")

link='Crop Progress and Conditions: [Crop Progress and Conditions](https://danielemarobin-cropprogress-home.streamlit.app/)'
st.markdown(link)

# link='Trade Flow: [Trade Flow](https://danielemarobin-tradeflow-home.streamlit.app/)'
# st.markdown(link)


# st.sidebar.markdown("# Navigator")