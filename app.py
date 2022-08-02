import streamlit as st;
import time

from streamlit.elements.time_widgets import TimeValue
"#  Manutenção"
"##  inserção de dados"

hora = st.time_input('Horário')
title1 = st.text_input('Tensão L1')
title2 = st.text_input('Tensão L2')
title3 = st.text_input('Tensão L3')

st.write('Às ', hora, 'As tensoes de entrada sao:',title1,'KV, ',title2,'KV, ',title3,'KV' )
   


