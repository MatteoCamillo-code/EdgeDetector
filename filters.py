# filters.py
import numpy as np

# --- 1D Filters ---

BACKWARD = np.array([0, 1, -1], dtype=float)

FORWARD = np.array([-1, 1, 0], dtype=float)

CENTRAL = np.array([-1, 0, 1], dtype=float)

# --- Gradient(edge) Filters ---
SOBEL_X = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=float)

SOBEL_Y = np.array([
    [-1, -2, -1],
    [0,  0,  0],
    [1,  2,  1]
], dtype=float)

PREWITT_X = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=float)

PREWITT_Y = np.array([
    [-1, -1, -1],
    [0,  0,  0],
    [1,  1,  1]
], dtype=float)

# --- Other Filters ---
LAPLACIAN = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
], dtype=float)

GAUSSIAN_3X3 = (1 / 16) * np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
], dtype=float)


# Optional: convenient lookup dictionary
FILTERS = {
    "backward": BACKWARD,
    "forward": FORWARD,
    "central": CENTRAL,
    "sobel_x": SOBEL_X,
    "sobel_y": SOBEL_Y,
    "prewitt_x": PREWITT_X,
    "prewitt_y": PREWITT_Y,
    "laplacian": LAPLACIAN,
    "gaussian_3x3": GAUSSIAN_3X3
}

def get_filter(name: str) -> np.ndarray:
    """Retrieve a predefined filter by name."""
    name = name.lower()
    if name not in FILTERS:
        raise ValueError(f"Unknown filter name: '{name}'. Available: {list(FILTERS.keys())}")
    return FILTERS[name]
