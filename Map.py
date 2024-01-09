import folium

orel = [52.9671, 36.0643]

zoom_start_defined = 15
min_zoom_defined = 12
orel_map = folium.Map(location=orel,
                      zoom_start=zoom_start_defined,
                      min_zoom=min_zoom_defined,
                      max_bounds=True)