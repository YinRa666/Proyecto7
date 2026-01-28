import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header('Análisis Exploratorio de Datos de Vehículos')

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# --- SECCIÓN DE HISTOGRAMA ---
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Distribución de la columna Odómetro (kilometraje)')
    
    # Crear histograma con graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Frecuencia de Kilometraje en el Inventario',
                      xaxis_title='Millas',
                      yaxis_title='Cantidad de Vehículos')
    
    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN DE GRÁFICO DE DISPERSIÓN ---
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Relación entre el Odómetro y el Precio del vehículo')
    
    # Crear gráfico de dispersión con plotly express (es más rápido para scatter plots)
    # Filtramos un poco los datos para que el gráfico no sea lento
    fig_scatter = px.scatter(car_data, x="odometer", y="price", 
                             title="Análisis de Depreciación: Millas vs Precio",
                             labels={'odometer': 'Kilometraje (millas)', 'price': 'Precio ($)'},
                             opacity=0.5)
    
    # Mostrar gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)