

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code


dct = {
    'sofa': {
        'colours': ['red', 'blue', 'green'],
        'number_of_seats': ['red', 'blue', 'green'],
    },
    'table': {
        'colours': ['red', 'blue', 'green'],
        'table_top_material': ['glass', 'ceramic', 'wood'],
    },
    'tv console': {
        'colours': ['red', 'blue', 'green'],
        'number_of_drawers': ['1 draw', '2 drawers', '3 drawers','4 drawers'],
    }
}


product_type = st.selectbox('Select a product type', ('sofa', 'table', 'tv console'))

if product_type:
    product_attributes = dct[product_type]
    for k, values in product_attributes.items():
        values = tuple(values)
        attribute = st.selectbox(f'Choose a {k}', values)