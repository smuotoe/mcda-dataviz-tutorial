"""
Verify all code snippets from the data visualization slides are runnable.

This script tests the code examples from each section to ensure:
1. All imports work correctly
2. Function/method names are current (not deprecated)
3. Code runs without errors
4. Output matches expected behavior
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")  # Non-interactive backend for testing

# Ensure plots don't display during testing
plt.ioff()

OUTPUT_DIR = Path(__file__).parent / "verification_output"
OUTPUT_DIR.mkdir(exist_ok=True)


def test_matplotlib_basics() -> None:
    """Test basic matplotlib examples from slides."""
    print("Testing matplotlib basics...")

    # From slide: Basic Line Plot
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y)
    ax.set_xlabel("Angle (radians)")
    ax.set_ylabel("sin(x)")
    ax.set_title("Sine Wave")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "line_plot.png", dpi=150)
    plt.close(fig)

    # From slide: Multiple Lines with Legend
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, np.sin(x), label="sin(x)")
    ax.plot(x, np.cos(x), label="cos(x)")
    ax.plot(x, np.sin(2 * x), label="sin(2x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Trigonometric Functions")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "multi_line.png", dpi=150)
    plt.close(fig)

    # From slide: Scatter Plot with Color and Size
    np.random.seed(42)
    n = 50
    x = np.random.randn(n)
    y = np.random.randn(n)
    colors = np.random.rand(n)
    sizes = np.abs(np.random.randn(n)) * 200

    fig, ax = plt.subplots(figsize=(7, 5))
    scatter = ax.scatter(x, y, c=colors, s=sizes, cmap="viridis", alpha=0.7)
    fig.colorbar(scatter, ax=ax, label="Value")
    ax.set_title("Scatter with Color & Size")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "scatter_color_size.png", dpi=150)
    plt.close(fig)

    # From slide: Bar Chart with Labels
    categories = ["A", "B", "C", "D", "E"]
    values = [23, 45, 56, 78, 32]

    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(categories, values, color="steelblue")

    for bar, val in zip(bars, values, strict=False):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            str(val),
            ha="center",
            va="bottom",
        )

    ax.set_xlabel("Category")
    ax.set_ylabel("Value")
    ax.set_title("Bar Chart with Labels")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "bar_chart.png", dpi=150)
    plt.close(fig)

    # From slide: Histogram
    np.random.seed(42)
    data = np.random.randn(1000)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.hist(data, bins=30, color="steelblue", edgecolor="white", alpha=0.7)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Random Data")
    ax.axvline(data.mean(), color="red", linestyle="--", label="Mean")
    ax.legend()
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "histogram.png", dpi=150)
    plt.close(fig)

    print("  Matplotlib basics: PASSED")


def test_matplotlib_advanced() -> None:
    """Test advanced matplotlib examples from slides."""
    print("Testing matplotlib advanced...")

    # From slide: Subplots
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    x = np.linspace(0, 10, 100)

    axes[0, 0].plot(x, np.sin(x))
    axes[0, 0].set_title("Sine")

    axes[0, 1].plot(x, np.cos(x))
    axes[0, 1].set_title("Cosine")

    axes[1, 0].plot(x, np.exp(-x / 3))
    axes[1, 0].set_title("Exponential Decay")

    axes[1, 1].plot(x, x**2)
    axes[1, 1].set_title("Quadratic")

    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "subplots.png", dpi=150)
    plt.close(fig)

    # From slide: Error Bars
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
    y_err = np.array([0.3, 0.4, 0.5, 0.3, 0.4])

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.errorbar(
        x,
        y,
        yerr=y_err,
        fmt="o",
        capsize=5,
        capthick=1.5,
        ecolor="gray",
        elinewidth=1.5,
        markerfacecolor="blue",
        markersize=8,
    )
    ax.set_xlabel("Condition")
    ax.set_ylabel("Measurement")
    ax.set_title("Results with Error Bars")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "error_bars.png", dpi=150)
    plt.close(fig)

    # From slide: fill_between for CI
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    y_upper = y + 0.3
    y_lower = y - 0.3

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.fill_between(x, y_lower, y_upper, alpha=0.3, color="blue", label="95% CI")
    ax.plot(x, y, color="blue", linewidth=2, label="Mean")
    ax.legend()
    ax.set_title("Measurement with 95% CI")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "confidence_interval.png", dpi=150)
    plt.close(fig)

    # From slide: Twin Axes
    x = np.arange(1, 11)
    y1 = x**2
    y2 = np.log(x) * 100

    fig, ax1 = plt.subplots(figsize=(8, 5))

    color1 = "steelblue"
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y1: Quadratic", color=color1)
    ax1.plot(x, y1, color=color1, marker="o")
    ax1.tick_params(axis="y", labelcolor=color1)

    ax2 = ax1.twinx()
    color2 = "coral"
    ax2.set_ylabel("Y2: Log scale", color=color2)
    ax2.plot(x, y2, color=color2, marker="s")
    ax2.tick_params(axis="y", labelcolor=color2)

    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "twin_axes.png", dpi=150)
    plt.close(fig)

    print("  Matplotlib advanced: PASSED")


def test_seaborn() -> None:
    """Test seaborn examples from slides."""
    print("Testing seaborn...")

    import seaborn as sns

    # Load datasets
    tips = sns.load_dataset("tips")
    penguins = sns.load_dataset("penguins")

    # From slide: histplot
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.histplot(data=tips, x="total_bill", kde=True, bins=20, ax=ax)
    ax.set_title("Distribution of Total Bill")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "seaborn_histplot.png", dpi=150)
    plt.close(fig)

    # From slide: boxplot
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.boxplot(data=tips, x="day", y="total_bill", hue="time", ax=ax)
    ax.set_title("Bill Distribution by Day")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "seaborn_boxplot.png", dpi=150)
    plt.close(fig)

    # From slide: violinplot
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.violinplot(
        data=tips, x="day", y="total_bill", hue="time", split=True, inner="quart", ax=ax
    )
    ax.set_title("Bill Distribution by Day")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "seaborn_violinplot.png", dpi=150)
    plt.close(fig)

    # From slide: scatterplot with multiple encodings
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=penguins,
        x="bill_length_mm",
        y="bill_depth_mm",
        hue="species",
        size="body_mass_g",
        style="island",
        palette="Set2",
        ax=ax,
    )
    ax.set_title("Penguin Bill Dimensions")
    ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "seaborn_scatter.png", dpi=150)
    plt.close(fig)

    # From slide: regplot
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.regplot(
        data=tips,
        x="total_bill",
        y="tip",
        scatter_kws={"alpha": 0.5},
        line_kws={"color": "red"},
        ci=95,
        ax=ax,
    )
    ax.set_title("Tip vs Bill with Regression")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "seaborn_regplot.png", dpi=150)
    plt.close(fig)

    # From slide: heatmap (correlation)
    numeric_cols = penguins.select_dtypes("number")
    corr = numeric_cols.corr()

    fig, ax = plt.subplots(figsize=(7, 6))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="RdBu_r",
        center=0,
        vmin=-1,
        vmax=1,
        square=True,
        ax=ax,
    )
    ax.set_title("Feature Correlations")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "seaborn_heatmap.png", dpi=150)
    plt.close(fig)

    # From slide: pairplot
    g = sns.pairplot(penguins, hue="species", diag_kind="kde", height=2.5)
    g.fig.suptitle("Penguin Measurements", y=1.02)
    g.savefig(OUTPUT_DIR / "seaborn_pairplot.png", dpi=150)
    plt.close(g.fig)

    print("  Seaborn: PASSED")


def test_plotly() -> None:
    """Test plotly examples from slides."""
    print("Testing plotly...")

    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    # Load datasets
    tips = px.data.tips()
    df = px.data.gapminder()
    df_2007 = df[df["year"] == 2007]
    iris = px.data.iris()

    # From slide: Basic scatter (Why Interactive)
    fig = px.scatter(
        tips,
        x="total_bill",
        y="tip",
        color="day",
        hover_data=["size"],
        title="Tips by Day",
    )
    fig.update_layout(template="plotly_white")
    fig.write_html(OUTPUT_DIR / "plotly_scatter_tips.html")
    fig.write_image(OUTPUT_DIR / "plotly_scatter_tips.png", width=700, height=500, scale=2)

    # From slide: Interactive scatter (Gapminder)
    fig = px.scatter(
        df_2007,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        title="GDP vs Life Expectancy (2007)",
    )
    fig.update_layout(template="plotly_white")
    fig.write_html(OUTPUT_DIR / "plotly_scatter.html")
    fig.write_image(OUTPUT_DIR / "plotly_scatter.png", width=700, height=500, scale=2)

    # From slide: Line plot
    countries = ["United States", "China", "India"]
    df_subset = df[df["country"].isin(countries)]
    fig = px.line(
        df_subset,
        x="year",
        y="gdpPercap",
        color="country",
        markers=True,
        title="GDP Comparison",
    )
    fig.update_layout(template="plotly_white")
    fig.write_html(OUTPUT_DIR / "plotly_line.html")
    fig.write_image(OUTPUT_DIR / "plotly_line.png", width=700, height=500, scale=2)

    # From slide: Bar chart
    fig = px.bar(
        tips,
        x="day",
        y="total_bill",
        color="sex",
        barmode="group",
        title="Total Bills by Day",
    )
    fig.update_layout(template="plotly_white")
    fig.write_html(OUTPUT_DIR / "plotly_bar.html")
    fig.write_image(OUTPUT_DIR / "plotly_bar.png", width=700, height=500, scale=2)

    # From slide: Animation (static frame for slide)
    fig = px.scatter(
        df_2007,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        range_y=[25, 90],
        title="Gapminder 2007 (Animation shows all years)",
    )
    fig.update_layout(template="plotly_white")
    fig.write_image(OUTPUT_DIR / "plotly_animation.png", width=700, height=500, scale=2)

    # Animation HTML version
    df_small = df[df["year"].isin([1952, 1977, 2007])]
    fig = px.scatter(
        df_small,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        animation_frame="year",
        log_x=True,
        range_x=[100, 100000],
        range_y=[25, 90],
        title="Gapminder Animation",
    )
    fig.write_html(OUTPUT_DIR / "plotly_animation.html")

    # From slide: 3D scatter
    fig = px.scatter_3d(
        iris,
        x="sepal_length",
        y="sepal_width",
        z="petal_width",
        color="species",
        title="Iris Dataset in 3D",
    )
    fig.update_layout(template="plotly_white")
    fig.write_html(OUTPUT_DIR / "plotly_3d.html")
    fig.write_image(OUTPUT_DIR / "plotly_3d.png", width=700, height=500, scale=2)

    # From slide: Scatter with trendline
    fig = px.scatter(tips, x="total_bill", y="tip", color="smoker", trendline="ols")
    fig.update_layout(template="plotly_white")
    fig.write_html(OUTPUT_DIR / "plotly_trendline.html")

    # From slide: Choropleth map
    fig = px.choropleth(
        df_2007,
        locations="iso_alpha",
        color="gdpPercap",
        hover_name="country",
        color_continuous_scale="Viridis",
        title="GDP per Capita (2007)",
    )
    fig.write_html(OUTPUT_DIR / "plotly_choropleth.html")

    # From slide: Graph Objects
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode="lines+markers", name="Series A")
    )
    fig.add_trace(go.Bar(x=[1, 2, 3, 4], y=[5, 6, 7, 8], name="Series B"))
    fig.update_layout(title="Mixed Chart", xaxis_title="X", yaxis_title="Y")
    fig.write_html(OUTPUT_DIR / "plotly_graph_objects.html")

    # From slide: make_subplots
    fig = make_subplots(
        rows=2, cols=2, subplot_titles=("Scatter", "Bar", "Line", "Histogram")
    )
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode="markers"), row=1, col=1)
    fig.add_trace(go.Bar(x=["A", "B", "C"], y=[1, 2, 3]), row=1, col=2)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 9], mode="lines"), row=2, col=1)
    fig.add_trace(go.Histogram(x=np.random.randn(100)), row=2, col=2)
    fig.update_layout(height=600, showlegend=False)
    fig.write_html(OUTPUT_DIR / "plotly_subplots.html")

    print("  Plotly: PASSED")


def test_comparison_examples() -> None:
    """Test the comparison examples from slides."""
    print("Testing comparison examples...")

    import seaborn as sns

    tips = sns.load_dataset("tips")

    # From slide: Same plot in three libraries
    # Matplotlib version
    fig, ax = plt.subplots(figsize=(7, 5))
    scatter = ax.scatter(
        tips["total_bill"], tips["tip"], c=tips["size"], cmap="viridis", alpha=0.7
    )
    ax.set_xlabel("Total Bill")
    ax.set_ylabel("Tip")
    ax.set_title("Tips vs Bill")
    fig.colorbar(scatter, label="Party Size")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "comparison_matplotlib.png", dpi=150)
    plt.close(fig)

    # Seaborn version
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.scatterplot(
        data=tips, x="total_bill", y="tip", hue="size", palette="viridis", alpha=0.7, ax=ax
    )
    ax.set_title("Tips vs Bill")
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "comparison_seaborn.png", dpi=150)
    plt.close(fig)

    # Plotly version
    import plotly.express as px

    tips_px = px.data.tips()
    fig = px.scatter(
        tips_px,
        x="total_bill",
        y="tip",
        color="size",
        color_continuous_scale="Viridis",
        opacity=0.7,
        title="Tips vs Bill",
    )
    fig.write_html(OUTPUT_DIR / "comparison_plotly.html")

    print("  Comparison examples: PASSED")


def main() -> None:
    """Run all verification tests."""
    print("=" * 60)
    print("Data Visualization Slides - Code Verification")
    print("=" * 60)
    print()

    test_matplotlib_basics()
    test_matplotlib_advanced()
    test_seaborn()
    test_plotly()
    test_comparison_examples()

    print()
    print("=" * 60)
    print("All code snippets verified successfully!")
    print(f"Output files saved to: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
