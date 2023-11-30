

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code


dct = {
    'sofa': {
        'colours': ['red', 'blue', 'green'],
        'number_of_seats': ['1 seat', '2 seater', '3 seater'],
        'main_material': ['leather', 'fabric', 'velvet', 'wood'],
        'back_style': ['scatter back', 'button back']
    },
    'table': {
        'wood_type': ['oak', 'pine', 'teak'],
        'table_top_material': ['glass', 'ceramic', 'wood'],
        'main_material': ['leather', 'fabric', 'velvet', 'wood'],
        'leg_material': ['wood', 'metal', 'plastic'],
    },
    'tv console': {
        'number_of_doors': ['0 doors', '1 door', '2 doors'],
        'number_of_drawers': ['0 drawers','1 draw', '2 drawers', '3 drawers','4 drawers'],
        'style': ['industrial', 'modern', 'scandi'],
    },
    'rug': {
        'pattern': ['striped', 'geometric'],
        'pile_type': ['short', 'long'],
    }
}


product_type = st.selectbox('Select a product type', ('sofa', 'table', 'tv console', 'rug'))

if product_type:
    product_attributes = dct[product_type]
    for k, values in product_attributes.items():
        values = tuple(values)
        attribute = st.multiselect(f'Choose {k} (multiselect)', values)