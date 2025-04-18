import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from geopy.distance import geodesic

@st.cache_data
def load_data():
    df = pd.read_csv("accident_dataset_UK.csv")
    df = df.dropna(subset=["latitude", "longitude"])
    return df

df = load_data()

st.title("Interactive Accident Hotspot Explorer")

st.markdown("🗺️ Click on the map to see accident hotspots around that point (within 10 km).")

map_center = [52.3555, -1.1743]

m = folium.Map(location=map_center, zoom_start=6)

click_location = st_folium(m, height=500, width="100%", returned_objects=["last_clicked"])

if click_location and click_location["last_clicked"]:
    lat_click = click_location["last_clicked"]["lat"]
    lon_click = click_location["last_clicked"]["lng"]
    st.success(f"You clicked at ({lat_click:.4f}, {lon_click:.4f})")

    radius_km = 10

    def is_within_radius(row):
        accident_loc = (row["latitude"], row["longitude"])
        click_loc = (lat_click, lon_click)
        return geodesic(accident_loc, click_loc).km <= radius_km

    nearby_df = df[df.apply(is_within_radius, axis=1)]

    st.write(f"🔍 Found {len(nearby_df)} accidents within {radius_km} km of the clicked location.")
    if not nearby_df.empty:
        heat_data = [
            [row["latitude"], row["longitude"]] for _, row in nearby_df.iterrows()
        ]
        folium_map = folium.Map(location=[lat_click, lon_click], zoom_start=12)
        HeatMap(heat_data, radius=10).add_to(folium_map)
        st_data = st_folium(folium_map, height=500, width="100%")
    else:
        st.warning("No accident data found in this area.")
