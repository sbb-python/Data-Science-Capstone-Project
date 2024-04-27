import folium

# Location of SDPI's headquarters (example coordinates)
sdpi_location = [40.7608, -111.8910]  # Example coordinates for Salt Lake City, Utah

# Create a map centered at SDPI's headquarters
m = folium.Map(location=sdpi_location, zoom_start=10)

# Add a marker for SDPI's headquarters
folium.Marker(location=sdpi_location, popup="SDPI Headquarters").add_to(m)

# Save the map to an HTML file
m.save("sdpi_map.html")
