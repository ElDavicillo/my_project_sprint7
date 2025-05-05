import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos una vez
car_data = pd.read_csv("vehicles_us.csv")  # leer los datos

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # al hacer clic en el botón
    # Escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un gráfico de dispersión
fig_scatter = px.scatter(car_data, x="odometer", y="price")

# Mostrar el gráfico de dispersión en Streamlit
st.plotly_chart(fig_scatter, use_container_width=True)
