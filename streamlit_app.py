#!/usr/bin/env python3
"""
Olist Business Activity Map - Toss Style Dashboard (Deployment Version)
An interactive map showing customer distribution, seller locations, and shipping flows across Brazil.
"""

import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Olist Business Activity Map",
    page_icon="🇧🇷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    """Load custom CSS styling"""
    css = """
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&display=swap');

    /* --- Main Font and Background --- */
    html, body, [class*="st-"] {
        font-family: 'Noto Sans', sans-serif;
    }
    .stApp {
        background-color: #FFFFFF;
    }

    /* --- Main Title --- */
    h1 {
        font-size: 2.5rem;
        font-weight: 700;
        color: #000000;
        text-align: center;
        padding-top: 2rem;
        padding-bottom: 0.5rem;
    }

    /* --- Subheader --- */
    h2, h3 {
        color: #333D4B;
        font-weight: 700;
    }

    /* --- Radio Buttons --- */
    .stRadio > label {
        font-size: 1.1rem;
        font-weight: 700;
        color: #4E5968;
    }

    /* --- Legend Box --- */
    .legend-box {
        background: #F8F9FA;
        border: 1px solid #E9ECEF;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }

    /* --- Footer --- */
    .footer {
        text-align: center;
        color: #808080;
        font-size: 0.875rem;
        padding: 2rem 0;
        border-top: 1px solid #E9ECEF;
        margin-top: 3rem;
    }
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

@st.cache_data
def create_demo_data():
    """Create comprehensive demo data for the dashboard"""
    # Major Brazilian cities with realistic data
    cities_data = [
        {"city": "São Paulo", "state": "SP", "lat": -23.5505, "lng": -46.6333, "customers": 15234, "sellers": 3421},
        {"city": "Rio de Janeiro", "state": "RJ", "lat": -22.9068, "lng": -43.1729, "customers": 8567, "sellers": 1834},
        {"city": "Belo Horizonte", "state": "MG", "lat": -19.9167, "lng": -43.9345, "customers": 5234, "sellers": 892},
        {"city": "Brasília", "state": "DF", "lat": -15.8267, "lng": -47.9218, "customers": 4123, "sellers": 634},
        {"city": "Salvador", "state": "BA", "lat": -12.9714, "lng": -38.5014, "customers": 3567, "sellers": 523},
        {"city": "Fortaleza", "state": "CE", "lat": -3.7319, "lng": -38.5267, "customers": 3234, "sellers": 445},
        {"city": "Curitiba", "state": "PR", "lat": -25.4284, "lng": -49.2733, "customers": 2891, "sellers": 467},
        {"city": "Recife", "state": "PE", "lat": -8.0476, "lng": -34.8770, "customers": 2567, "sellers": 378},
        {"city": "Porto Alegre", "state": "RS", "lat": -30.0346, "lng": -51.2177, "customers": 2345, "sellers": 412},
        {"city": "Manaus", "state": "AM", "lat": -3.1190, "lng": -60.0217, "customers": 1987, "sellers": 234},
        {"city": "Belém", "state": "PA", "lat": -1.4554, "lng": -48.5044, "customers": 1765, "sellers": 198},
        {"city": "Campinas", "state": "SP", "lat": -22.9099, "lng": -47.0626, "customers": 1654, "sellers": 287},
        {"city": "Florianópolis", "state": "SC", "lat": -27.5954, "lng": -48.5480, "customers": 1543, "sellers": 256},
        {"city": "Ribeirão Preto", "state": "SP", "lat": -21.1775, "lng": -47.8100, "customers": 1432, "sellers": 198},
        {"city": "Goiânia", "state": "GO", "lat": -16.6868, "lng": -49.2648, "customers": 1321, "sellers": 176}
    ]
    
    # Create customer locations
    customer_locations = pd.DataFrame([
        {
            "customer_state": city["state"],
            "customer_city": city["city"],
            "customer_lat": city["lat"],
            "customer_lng": city["lng"],
            "customer_id": city["customers"],
            "type": "customer"
        }
        for city in cities_data
    ])
    
    # Create seller locations
    seller_locations = pd.DataFrame([
        {
            "seller_state": city["state"],
            "seller_city": city["city"],
            "seller_lat": city["lat"],
            "seller_lng": city["lng"],
            "seller_id": city["sellers"],
            "type": "seller"
        }
        for city in cities_data
    ])
    
    # Create shipping flows (more realistic patterns)
    shipping_flows = []
    for i, origin in enumerate(cities_data):
        for j, dest in enumerate(cities_data):
            if i != j:
                # More flows from bigger cities
                flow_probability = origin["sellers"] / 10000
                if np.random.random() < flow_probability:
                    shipping_flows.append({
                        "customer_lat": dest["lat"],
                        "customer_lng": dest["lng"],
                        "seller_lat": origin["lat"],
                        "seller_lng": origin["lng"]
                    })
    
    shipping_flows_df = pd.DataFrame(shipping_flows)
    if len(shipping_flows_df) > 50:
        shipping_flows_df = shipping_flows_df.sample(n=50, random_state=42)
    
    return customer_locations, seller_locations, shipping_flows_df

def create_distribution_map(customer_locations, seller_locations):
    """Create geographic distribution map"""
    layers = []
    
    if customer_locations is not None and not customer_locations.empty:
        customer_layer = pdk.Layer(
            "ScatterplotLayer",
            data=customer_locations,
            get_position=["customer_lng", "customer_lat"],
            get_color=[49, 130, 246, 200],
            get_radius=5000,
            radius_min_pixels=3,
            radius_max_pixels=20,
            pickable=True,
        )
        layers.append(customer_layer)
    
    if seller_locations is not None and not seller_locations.empty:
        seller_layer = pdk.Layer(
            "ScatterplotLayer",
            data=seller_locations,
            get_position=["seller_lng", "seller_lat"],
            get_color=[239, 68, 68, 200],
            get_radius=8000,
            radius_min_pixels=4,
            radius_max_pixels=25,
            pickable=True,
        )
        layers.append(seller_layer)
    
    view_state = pdk.ViewState(
        latitude=-14.235,
        longitude=-51.9253,
        zoom=4.5,
        pitch=0,
        bearing=0,
    )
    
    return pdk.Deck(
        map_style="light",
        initial_view_state=view_state,
        layers=layers,
        tooltip={
            "html": "<b>Type:</b> {type}<br/>"
                   "<b>Count:</b> {customer_id}{seller_id}<br/>"
                   "<b>City:</b> {customer_city}{seller_city}<br/>"
                   "<b>State:</b> {customer_state}{seller_state}",
            "style": {"backgroundColor": "#333D4B", "color": "white", "fontSize": "12px"}
        }
    )

def create_shipping_flows_map(shipping_flows):
    """Create shipping flows arc map"""
    if shipping_flows is None or shipping_flows.empty:
        return None
    
    arc_layer = pdk.Layer(
        "ArcLayer",
        data=shipping_flows,
        get_source_position=["seller_lng", "seller_lat"],
        get_target_position=["customer_lng", "customer_lat"],
        get_source_color=[239, 68, 68, 180],
        get_target_color=[49, 130, 246, 180],
        auto_highlight=True,
        width_scale=0.001,
        get_width=2,
        width_min_pixels=1,
        width_max_pixels=4,
    )
    
    view_state = pdk.ViewState(
        latitude=-14.235,
        longitude=-51.9253,
        zoom=4.2,
        pitch=45,
        bearing=0,
    )
    
    return pdk.Deck(
        map_style="light",
        initial_view_state=view_state,
        layers=[arc_layer],
        tooltip={
            "html": "<b>🚚 Shipping Flow</b><br/>"
                   "🔴 From: Seller<br/>"
                   "🔵 To: Customer",
            "style": {"backgroundColor": "#333D4B", "color": "white", "fontSize": "12px"}
        }
    )

# Load custom CSS
load_css()

# Main title
st.markdown("""
<h1>🇧🇷 Olist Business Activity Map</h1>
""", unsafe_allow_html=True)

# Subtitle
st.markdown("""
<div style="text-align: center; color: #4E5968; font-size: 1.1rem; margin-bottom: 2rem;">
An interactive map showing customer distribution, seller locations, and shipping flows across Brazil
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Load demo data
with st.spinner("Loading Brazil e-commerce data..."):
    customer_locations, seller_locations, shipping_flows = create_demo_data()

st.success("✅ Demo data loaded successfully")

# Main content container
with st.container():
    # View selector
    st.subheader("Select a View")
    
    view_option = st.radio(
        "Choose visualization type:",
        ["Geographic Distribution", "Shipping Flows"],
        horizontal=True
    )
    
    # Legend section
    col1, col2 = st.columns(2)
    
    if view_option == "Geographic Distribution":
        with col1:
            st.markdown("""
            <div class="legend-box">
                <h4>Geographic Distribution Legend</h4>
                <p>🔵 <strong>Customers</strong> - Customer locations by city</p>
                <p>🔴 <strong>Sellers</strong> - Seller locations by city</p>
                <p><em>Size indicates relative volume</em></p>
            </div>
            """, unsafe_allow_html=True)
    
    elif view_option == "Shipping Flows":
        with col2:
            st.markdown("""
            <div class="legend-box">
                <h4>Shipping Flows Legend</h4>
                <p>🔴 <strong>Origin</strong> - Seller locations</p>
                <p>🔵 <strong>Destination</strong> - Customer locations</p>
                <p><em>Lines show shipping connections</em></p>
            </div>
            """, unsafe_allow_html=True)
    
    # Map visualization
    st.markdown("### Interactive Map")
    
    if view_option == "Geographic Distribution":
        map_obj = create_distribution_map(customer_locations, seller_locations)
        if map_obj:
            st.pydeck_chart(map_obj, use_container_width=True)
        else:
            st.error("Unable to create distribution map")
    
    elif view_option == "Shipping Flows":
        map_obj = create_shipping_flows_map(shipping_flows)
        if map_obj:
            st.pydeck_chart(map_obj, use_container_width=True)
        else:
            st.error("Unable to create shipping flows map")

    # Key Insights Section
    st.markdown("---")
    st.subheader("Key Insights")
    
    # Calculate metrics
    total_customers = customer_locations['customer_id'].sum() if customer_locations is not None else 0
    total_sellers = seller_locations['seller_id'].sum() if seller_locations is not None else 0
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Primary Hub",
            value="São Paulo (SP)",
            help="Main business activity center"
        )
    
    with col2:
        st.metric(
            label="Total Customers",
            value=f"{total_customers:,}",
            help="Total customer count across Brazil"
        )
    
    with col3:
        st.metric(
            label="Total Sellers",
            value=f"{total_sellers:,}",
            help="Total seller count across Brazil"
        )

# Footer
st.markdown("---")
st.markdown(
    """
    <div class="footer">
        <p>Olist Data Analytics Dashboard | Powered by Streamlit & Pydeck</p>
        <p>🚀 <strong>Deployed with Toss-inspired design</strong></p>
    </div>
    """,
    unsafe_allow_html=True
)