

**Path Optimizer** is a web-based tool designed to help you find the most efficient delivery route between multiple locations. It allows users to input a set of delivery locations and the distances between them, then computes the shortest possible path that visits all locations exactly once and returns the optimal route and its total distance. This is particularly useful for logistics, delivery planning, and route optimization tasks.

## 🚀 Live Demo

Check out the deployed app here:  
👉 [https://pathoptimizer-dsm.streamlit.app/](https://pathoptimizer-dsm.streamlit.app/)

---

## Features

- **Interactive UI**: Simple web interface powered by Streamlit.
- **Custom Locations**: Add as many delivery points as you need.
- **Flexible Distance Input**: Enter the distance between each pair of locations manually for precise control.
- **Optimal Route Calculation**: Computes the best route using a brute-force approach (solves the classic Traveling Salesman Problem for small N).
- **Instant Results**: Displays the shortest route and the total distance as soon as you click "Find Best Route".

---

## How It Works

1. **Enter the number of delivery locations** you want to optimize.
2. **Name each location** (e.g., "Warehouse", "Store A", "Store B"...).
3. **Input the distance between each pair** of locations.
4. **Select the starting location** from the dropdown.
5. Click **"Find Best Route"** to get the optimized delivery path and total distance.

The app computes all possible permutations to find the shortest route, making it most suitable for scenarios with a reasonable number of locations (e.g., up to 8-10).

---

## Example

Suppose you need to deliver packages to four locations: A, B, C, and D.

- You enter "4" as the number of delivery locations.
- Name them "A", "B", "C", "D".
- Input the pairwise distances between each location.
- Select your starting location (e.g., "A").
- Click "Find Best Route" to see the shortest possible delivery route and its total distance.

---

## Technologies Used

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/) (for the web interface)
- [itertools](https://docs.python.org/3/library/itertools.html) (for route permutation)

---

## Setup & Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/jeet401/Path_Optimizer.git
   cd Path_Optimizer
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit
   ```

3. **Run the app locally:**
   ```bash
   streamlit run dsm-optimiser.py
   ```

4. Open the given local URL in your browser.

---

## File Structure

- `dsm-optimiser.py` — Main Streamlit application file.

---

## Limitations

- The current approach uses brute-force permutation and is best suited for a small number of locations (typically < 10) due to factorial time complexity.
- For larger datasets, future versions may integrate heuristic or approximation algorithms.

---

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an issue or submit a pull request.

---

## Author

Made with ❤️ by [jeet401](https://github.com/jeet401)
