# https://share.streamlit.io/

# https://share.streamlit.io/danielemarobin/monitor/main/Home.py

# Bloomberg API installing process
# https://discuss.streamlit.io/t/installing-packages-from-the-web/27537

# pipreqs --encoding=utf8

import streamlit as st

st.set_page_config(page_title="Navigator",layout="wide",initial_sidebar_state="expanded")

cols_size=[1,5]
st.markdown("# Navigator")

st.markdown("---")
st.markdown("### Price Analysis")
if True:
    project = 'Seasonals'
    if True:    
        col1,col2 = st.columns(cols_size)

        link=f'''* [{project}](https://danielemarobin-seasonals-home.streamlit.app/)'''
        roadmap='''
        * :green[Done this week]:
            * Added controls on forward onth range and past years
            * Made sure that the seasonal never goes further than First Notice Day
        * :red[To Do]:
            * Visualize and Analyse fund roll
        '''
        with col1:
            st.markdown(link)

        with col2:
            with st.expander(f'{project} Roadmap'):
                st.markdown(roadmap)

    project = 'Trade Radar'
    if True:    
        col1,col2 = st.columns(cols_size)

        link=f'''* [{project}](https://danielemarobin-traderadar-home.streamlit.app/)'''
        roadmap='''
        * :green[Done this week]:
            * No recent changes
        * :red[To Do]:
            * Put filters on Price percentile    
        '''
        with col1:
            st.markdown(link)

        with col2:
            with st.expander(f'{project} Roadmap'):
                st.markdown(roadmap)

    project = 'Price Models'
    if True:    
        col1,col2 = st.columns(cols_size)

        link=f'''* [{project}](https://danielemarobin-pricemodels-home.streamlit.app/)'''
        roadmap='''
        * :green[Done this week]:
            * No recent changes
        * :red[To Do]:
            * Fix an issue that arises in the heatmap when some months are excluded from the analysis
            * Change the way the variables are calculated (to better reflect the seasonals calculation)
        '''
        with col1:
            st.markdown(link)

        with col2:
            with st.expander(f'{project} Roadmap'):
                st.markdown(roadmap)


st.markdown("---")
st.markdown("### Yield Models")
if True:  
    # danielemarobin-argcornyieldmodel
    project = 'ARG Corn Yield'
    if True:    
        col1,col2 = st.columns(cols_size)

        link=f'''* [{project}](https://danielemarobin-argcornyieldmodel-home.streamlit.app/)'''
        roadmap='''
        * :green[Done this week]:
            * Created the full Model
        * :red[To Do]:
            * Get a better model (as this one, is giving some crazy low yield number)
        '''
        with col1:
            st.markdown(link)

        with col2:
            with st.expander(f'{project} Roadmap'):
                st.markdown(roadmap)

    project = 'BRA Safra Corn'
    if True:    
        col1,col2 = st.columns(cols_size)

        link=f'''* [{project}](https://danielemarobin-brasafracornyieldmodel-home.streamlit.app/)'''
        roadmap='''
        * :green[Done this week]:
            * No recent changes
        * :red[To Do]:
            * Keep it updated with development in other crops yield models
        '''
        with col1:
            st.markdown(link)

        with col2:
            with st.expander(f'{project} Roadmap'):
                st.markdown(roadmap)

    project = 'BRA Safrina Corn'
    if True:    
        col1,col2 = st.columns(cols_size)

        link=f'''* [{project}](https://danielemarobin-brasafrinacornyieldmodel-home.streamlit.app/)'''
        roadmap='''
        * :green[Done this week]:
            * Made sure that the data pipeline runs smooth (hist weather, GFS and ECMWF both operational and ensemble)
            * Calculated and checked that the yearly national yield calculaion matches the CONAB one
        * :red[To Do]:
            * Select the final moodel and keep it up and running at every weather run
        '''
        with col1:
            st.markdown(link)

        with col2:
            with st.expander(f'{project} Roadmap'):
                st.markdown(roadmap)


st.markdown("---")
st.markdown("### Crops")
if True:    
    project = 'Crop Progress and Conditions'
    if True:    
        col1,col2 = st.columns(cols_size)

        link=f'''* [{project}](https://danielemarobin-cropprogress-home.streamlit.app/)'''
        roadmap='''
        * :green[Done this week]:
            * No recent changes
        * :red[To Do]:
            * Evaluate R-squared of the simple 'delta condition vs delta yield' model from the beginning of the season till the end, to understand when the model starts to become significant
        '''
        with col1:
            st.markdown(link)

        with col2:
            with st.expander(f'{project} Roadmap'):
                st.markdown(roadmap)


st.markdown("---")
st.markdown("### Acreage")
if True:    
    project = 'US Acreage'
    if True:    
        col1,col2 = st.columns(cols_size)

        link=f'''* {project} coming soon...'''
        roadmap='''
        * :green[Done this week]:
            * Defined project and project deadline
        * :red[To Do]:
            * Create model and provide estimate
        '''
        with col1:
            st.markdown(link)

        with col2:
            with st.expander(f'{project} Roadmap'):
                st.markdown(roadmap)


st.markdown("---")
st.markdown("### US Corn Quarterly Stocks Estimate (F&R Model)")
if True:    
    project = 'US Quarterly Stocks Estimate'
    if True:    
        col1,col2 = st.columns(cols_size)

        link=f'''* {project} coming soon...'''
        roadmap='''
        * :green[Done]:
            * Created the forecast model
        * :red[To Do]:
            * Make the model estimate easily accessible from this platform
        '''
        with col1:
            st.markdown(link)

        with col2:
            with st.expander(f'{project} Roadmap'):
                st.markdown(roadmap)


st.markdown("---")
st.markdown("### Satellite Imagery Analysis")
if True:    
    project = 'Satellite Imagery Analysis'
    if True:    
        col1,col2 = st.columns(cols_size)

        link=f'''* {project} coming soon...'''
        roadmap='''
        * :green[Done]:
            * Created a simple tool to download all satellite images for a certain period and area based on different criteria
            * Created a classification model that given as input a series of satellite pictures, classifies the crop
            * Unfortunately the above model can only be applied to small areas (due to the limits that Google Earth has in place)
        * :red[To Do]:
            * Make the above intermediate results and analysis available to everyone for brainstorming and ideas generation
            * Find a way to overcome the current data and computation limitation
            * Create a simple model for planting progress (based on the difference between images taken days apart)
        '''
        with col1:
            st.markdown(link)

        with col2:
            with st.expander(f'{project} Roadmap'):
                st.markdown(roadmap)                
