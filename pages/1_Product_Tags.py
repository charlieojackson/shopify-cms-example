

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code


dct = {
    'sofa': {
        'colours': ['red', 'blue', 'green'],
        'number_of_seats': ['1 seat', '2 seater', '3 seater'],
    },
    'table': {
        'wood_type': ['oak', 'pine', 'teak'],
        'table_top_material': ['glass', 'ceramic', 'wood'],
    },
    'tv console': {
        'number_of_doors': ['0 doors', '1 door', '2 doors'],
        'number_of_drawers': ['0 drawers','1 draw', '2 drawers', '3 drawers','4 drawers'],
    }
}


product_type = st.selectbox('Select a product type', ('sofa', 'table', 'tv console'))

if product_type:
    product_attributes = dct[product_type]
    for k, values in product_attributes.items():
        values = tuple(values)
        attribute = st.multiselect(f'Choose a {k}', values)