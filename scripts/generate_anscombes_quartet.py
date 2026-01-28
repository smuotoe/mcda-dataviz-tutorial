"""Generate Anscombe's Quartet visualization with white background.

Creates a 2x2 subplot showing the four datasets from Anscombe's Quartet,
each with distinct colors and regression lines.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def get_anscombe_data() -> dict[str, dict[str, np.ndarray]]:
    """Return Anscombe's Quartet datasets.

    Returns:
        Dictionary containing four datasets, each with 'x' and 'y' arrays.
    """
    return {
        "I": {
            "x": np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]),
            "y": np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
        },
        "II": {
            "x": np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]),
            "y": np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
        },
        "III": {
            "x": np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]),
            "y": np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
        },
        "IV": {
            "x": np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]),
            "y": np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]),
        },
    }


def create_anscombes_quartet_plot(output_path: Path) -> None:
    """Create and save Anscombe's Quartet visualization.

    Args:
        output_path: Path where the PNG image will be saved.
    """
    data = get_anscombe_data()

    # Configuration for each subplot
    config = {
        "I": {"color": "#1f77b4", "label": "I: Linear"},
        "II": {"color": "#2ca02c", "label": "II: Curved"},
        "III": {"color": "#ff7f0e", "label": "III: Outlier"},
        "IV": {"color": "#9467bd", "label": "IV: Clustered"},
    }

    fig, axes = plt.subplots(2, 2, figsize=(10, 8), facecolor="white")
    fig.suptitle(
        "Same Statistics, Different Patterns",
        fontsize=16,
        fontweight="bold",
        color="#333333",
    )

    positions = [("I", 0, 0), ("II", 0, 1), ("III", 1, 0), ("IV", 1, 1)]

    for dataset_name, row, col in positions:
        ax = axes[row, col]
        x = data[dataset_name]["x"]
        y = data[dataset_name]["y"]
        color = config[dataset_name]["color"]
        label = config[dataset_name]["label"]

        # Set white background for subplot
        ax.set_facecolor("white")

        # Scatter plot
        ax.scatter(x, y, c=color, s=80, alpha=0.8, edgecolors="white", linewidth=1.5)

        # Compute and plot regression line
        slope, intercept, _, _, _ = stats.linregress(x, y)
        x_line = np.linspace(3, 20, 100)
        y_line = slope * x_line + intercept
        ax.plot(x_line, y_line, color=color, linewidth=2, alpha=0.7)

        # Styling
        ax.set_title(label, fontsize=12, fontweight="bold", color="#333333")
        ax.set_xlim(3, 20)
        ax.set_ylim(2, 14)
        ax.grid(True, alpha=0.3, color="#cccccc")
        ax.tick_params(colors="#333333")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#666666")
        ax.spines["bottom"].set_color("#666666")

    plt.tight_layout()
    plt.subplots_adjust(top=0.92)

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save with high resolution
    fig.savefig(output_path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    output_file = script_dir.parent / "slides" / "public" / "images" / "anscombes_quartet.png"
    create_anscombes_quartet_plot(output_file)
    print(f"Saved Anscombe's Quartet plot to: {output_file}")
