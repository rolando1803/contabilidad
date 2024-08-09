import streamlit as st
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/rolando1803/contabilidad/main/plan.csv')
st.write(df)

if st.button('Insert Data'):
  # Replace with your actual data insertion logic
  new_data = {'Cuenta': [1000], 'Nombre': ['New Account'], 'Tipo': ['Activo']}
  new_df = pd.DataFrame(new_data)
  df = pd.concat([df, new_df], ignore_index=True)
  st.write(df)