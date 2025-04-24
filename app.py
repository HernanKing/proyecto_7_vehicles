
import pandas as pd
import plotly.express as px
import streamlit as st
        
df_vehicles_us = pd.read_csv('vehicles_us.csv')

st.header('Aplicación de vehículos Americanos')

show_hist = st.checkbox('Mostrar histograma de kilometraje')
show_scatter = st.checkbox('Mostrar gráfico de dispersión (kilometraje vs. precio)')

if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos (kilometraje)')
    fig_hist = px.histogram(df_vehicles_us, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write('Creación de un gráfico de dispersión analizando relación precio y kilometraje de los vehículos')
    fig_scatter = px.scatter(df_vehicles_us, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)