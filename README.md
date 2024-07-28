Dijkstra's Algorithm Visualizer
===============================

Explore the shortest paths between India's iconic destinations with this interactive visualizer powered by Dijkstra's algorithm. Perfect for learners and travelers alike, this tool offers a clear, visual understanding of how algorithmic pathfinding works in a real-world context.

Key Features
------------
- Interactive UI: Select start and end destinations from a dropdown to visualize the shortest route.
- Real-Time Visualization: Highlights the shortest path on a graph using Matplotlib.
- Algorithmic Learning: Demonstrates Dijkstra's algorithm with clear path and distance annotations.

Technical Details
-----------------
- Graph Construction: Utilizes NetworkX to model destinations as nodes and roads as weighted edges.
- Widgets for Interaction: Employs ipywidgets for a dynamic user interface within Jupyter Notebooks.
- Distance Calculations: Computes paths based on predefined road distances between destinations.

Installation
------------
To run the visualizer, ensure you have the required packages installed:

    pip install matplotlib networkx ipywidgets

How to Use
----------
1. Clone the Repository:

    git clone https://github.com/rahul5892/DIJSTRAS-ALGORITHM-VISUALIZER.git
    cd DIJSTRAS-ALGORITHM-VISUALIZER

2. Run in Jupyter Notebook:
   - Open `dijstras_visualizer.ipynb` in Jupyter Notebook.
   - Select your start and end destinations using the dropdowns.
   - Click "Find Shortest Path" to visualize the route and distance.

Contributing
------------
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request. Let's make learning algorithms fun and accessible for everyone.

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.
