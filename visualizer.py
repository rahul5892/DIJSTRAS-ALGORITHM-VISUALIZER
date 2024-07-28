import matplotlib.pyplot as plt
import networkx as nx
import ipywidgets as widgets
from IPython.display import display, HTML

# Define the top 5 destinations in India
destinations = [
    "Taj Mahal, Agra",
    "Jaipur, Rajasthan",
    "Varanasi, Uttar Pradesh",
    "Kerala Backwaters",
    "Ranthambore National Park, Rajasthan"
]

# Define the road distances between the cities in kilometers
# Note: Distances are approximate and may vary based on the specific routes taken
road_distances = {
    ("Taj Mahal, Agra", "Jaipur, Rajasthan"): 240,
    ("Taj Mahal, Agra", "Varanasi, Uttar Pradesh"): 605,
    ("Taj Mahal, Agra", "Kerala Backwaters"): 2300,
    ("Taj Mahal, Agra", "Ranthambore National Park, Rajasthan"): 600,
    ("Jaipur, Rajasthan", "Varanasi, Uttar Pradesh"): 800,
    ("Jaipur, Rajasthan", "Kerala Backwaters"): 2800,
    ("Jaipur, Rajasthan", "Ranthambore National Park, Rajasthan"): 150,
    ("Varanasi, Uttar Pradesh", "Kerala Backwaters"): 2500,
    ("Varanasi, Uttar Pradesh", "Ranthambore National Park, Rajasthan"): 870,
    ("Kerala Backwaters", "Ranthambore National Park, Rajasthan"): 2300,
}

# Function to find the shortest path between two cities using Dijkstra's algorithm
def shortest_path(graph, start, end):
    return nx.shortest_path(graph, start, end, weight="weight")

# Create a graph
G = nx.Graph()

# Add nodes (cities) to the graph
for city in destinations:
    G.add_node(city)

# Add edges (connections between cities) to the graph
for (city1, city2), distance in road_distances.items():
    G.add_edge(city1, city2, weight=distance)

# Dropdown widgets for selecting initial and final destinations
initial_dropdown = widgets.Dropdown(options=destinations, description="Initial Destination:", layout=widgets.Layout(width='400px'))
final_dropdown = widgets.Dropdown(options=destinations, description="Final Destination:", layout=widgets.Layout(width='400px'))

# Button widget to trigger the calculation and display of the shortest path
button = widgets.Button(description="Find Shortest Path", layout=widgets.Layout(width='200px'))
button.style.button_color = 'lightblue'

# Output widget to display the result
output = widgets.Output()

# Define function to handle button click event
def on_button_clicked(b):
    initial_city = initial_dropdown.value
    final_city = final_dropdown.value

    # Find the shortest path between the initial and final destinations
    path = shortest_path(G, initial_city, final_city)

    # Calculate total distance of the shortest path
    total_distance = sum(road_distances.get((path[i], path[i + 1]), road_distances.get((path[i + 1], path[i]))) for i in range(len(path) - 1))

    # Display the result
    with output:
        # Clear previous output
        output.clear_output()

        # Print shortest path and total distance
        print(f"Shortest Path: {' -> '.join(path)}")
        print(f"Total Distance: {total_distance} km")

        # Draw the graph with the shortest path highlighted
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
        for i in range(len(path) - 1):
            city1 = path[i]
            city2 = path[i + 1]
            distance = road_distances.get((city1, city2), road_distances.get((city2, city1)))
            plt.text((pos[city1][0] + pos[city2][0]) / 2, (pos[city1][1] + pos[city2][1]) / 2, f"{distance} km", fontsize=8, fontweight="bold", color="red", ha="center")
        plt.title(f"Shortest Path and Distance from {initial_city} to {final_city}")
        plt.axis("off")
        plt.show()

# Attach button click event handler
button.on_click(on_button_clicked)

# Display widgets
display(widgets.VBox([widgets.HBox([initial_dropdown, final_dropdown]), button, output]))
