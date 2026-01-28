---
layout: image-right
image: /images/02-matplotlib.jpg
backgroundSize: cover
backgroundPosition: center
class: flex flex-col justify-center
---

# Matplotlib

<div class="text-blue-400 text-lg mt-2">The Foundation of Python Visualization</div>

---
layout: default
---

# The Basic Pattern

Every Matplotlib plot follows the same pattern:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()     # 1. Create figure and axes
ax.plot(x, y)                 # 2. Plot your data
ax.set_xlabel("X Label")      # 3. Add labels
ax.set_ylabel("Y Label")
ax.set_title("Title")
plt.savefig("plot.png")       # 4. Save or show
```

<div class="mt-6 p-4 border rounded border-blue-500/30 bg-blue-500/10">

**Key insight:** `fig` is the canvas, `ax` is where you draw. Always use `fig, ax = plt.subplots()` to start.

</div>

---
layout: image-right
image: /verification_output/line_plot.png
backgroundSize: 90%
backgroundPosition: center
---

# Line Plots

Connect data points with lines.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sine Wave")
```

<div class="mt-4 text-sm">

- Great for continuous data
- Shows trends over time
- Use markers with `marker="o"`

</div>

---
layout: image-right
image: /verification_output/multi_line.png
backgroundSize: 90%
backgroundPosition: center
---

# Multiple Lines

Compare series with a legend.

```python
fig, ax = plt.subplots()

ax.plot(x, np.sin(x), label="sin")
ax.plot(x, np.cos(x), label="cos")
ax.legend()
```

<div class="mt-4 text-sm">

- Use `label=` for each line
- Call `ax.legend()` to show
- Colors auto-assigned

</div>

---
layout: image-right
image: /verification_output/scatter_color_size.png
backgroundSize: 90%
backgroundPosition: center
---

# Scatter Plots

Show relationships between variables.

```python
fig, ax = plt.subplots()

scatter = ax.scatter(
    x, y,
    c=colors,      # Color by value
    s=sizes,       # Size by value
    cmap="viridis"
)
fig.colorbar(scatter)
```

<div class="mt-4 text-sm">

- `c=` maps color to data
- `s=` maps size to data
- Add colorbar for reference

</div>

---
layout: image-right
image: /verification_output/bar_chart.png
backgroundSize: 90%
backgroundPosition: center
---

# Bar Charts

Compare categories.

```python
categories = ["A", "B", "C", "D"]
values = [23, 45, 56, 32]

fig, ax = plt.subplots()
ax.bar(categories, values)
```

<div class="mt-4 text-sm">

- Use `ax.bar()` for vertical
- Use `ax.barh()` for horizontal
- Add value labels on top with `ax.text()`

</div>

---
layout: image-right
image: /verification_output/histogram.png
backgroundSize: 90%
backgroundPosition: center
---

# Histograms

Show data distributions.

```python
import numpy as np

data = np.random.randn(1000)

fig, ax = plt.subplots()
ax.hist(data, bins=30)
ax.axvline(data.mean(),
           color="red",
           linestyle="--")
```

<div class="mt-4 text-sm">

- `bins=` controls granularity
- Show mean/median with `axvline()`
- Use `alpha=0.7` for overlapping

</div>

---
layout: image-right
image: /verification_output/subplots.png
backgroundSize: 90%
backgroundPosition: center
---

# Subplots

Multiple plots in one figure.

```python
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, np.sin(x))
axes[0, 1].plot(x, np.cos(x))
axes[1, 0].bar(cats, vals)
axes[1, 1].hist(data)

plt.tight_layout()
```

<div class="mt-4 text-sm">

- Access with `axes[row, col]`
- `tight_layout()` fixes spacing

</div>

---
layout: default
---

# Saving Figures

<div class="grid grid-cols-2 gap-6">

<div>

### Export Code

```python
fig.savefig("plot.png", dpi=300)
fig.savefig("plot.pdf")
fig.savefig("plot.svg")
```

<div class="mt-4 p-3 border-l-4 border-blue-500 bg-blue-500/10 text-sm">

Always use `dpi=300` for print quality.

</div>

### Common Options

```python
fig.savefig("plot.png",
    dpi=300,              # Resolution
    bbox_inches="tight",  # Remove whitespace
    transparent=True,     # Clear background
    facecolor="white"     # Or set bg color
)
```

</div>

<div>

### Format Guide

<table class="w-full text-sm border border-gray-600">
<thead>
<tr class="border-b-2 border-blue-500 bg-blue-500/20">
<th class="text-left py-2 px-3 border-r border-gray-600">Format</th>
<th class="text-left py-2 px-3 border-r border-gray-600">Best For</th>
<th class="text-left py-2 px-3">Notes</th>
</tr>
</thead>
<tbody>
<tr class="border-b border-gray-600">
<td class="py-2 px-3 font-mono border-r border-gray-600">PNG</td>
<td class="py-2 px-3 border-r border-gray-600">Web, presentations</td>
<td class="py-2 px-3 opacity-70">Raster, good compression</td>
</tr>
<tr class="border-b border-gray-600">
<td class="py-2 px-3 font-mono border-r border-gray-600">PDF</td>
<td class="py-2 px-3 border-r border-gray-600">Publications, print</td>
<td class="py-2 px-3 opacity-70">Vector, scales perfectly</td>
</tr>
<tr>
<td class="py-2 px-3 font-mono border-r border-gray-600">SVG</td>
<td class="py-2 px-3 border-r border-gray-600">Web, editing later</td>
<td class="py-2 px-3 opacity-70">Vector, editable in Illustrator</td>
</tr>
</tbody>
</table>

<div class="mt-6 p-3 border rounded bg-gray-800/50 text-sm">

**Pro tip:** Use `bbox_inches="tight"` to automatically crop whitespace around your figure.

</div>

</div>

</div>

---
layout: default
---

# Matplotlib Essentials

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="p-4 border rounded">

### Common Customizations

```python
ax.set_xlim(0, 10)        # Axis limits
ax.set_ylim(-1, 1)
ax.grid(True, alpha=0.3)  # Grid lines
ax.set_aspect("equal")    # Square plot
```

</div>

<div class="p-4 border rounded">

### Line Styles

```python
ax.plot(x, y, "r--")      # Red dashed
ax.plot(x, y, "b.-")      # Blue dot-dash
ax.plot(x, y, "go")       # Green circles
```

</div>

</div>

<div class="mt-6 p-4 border rounded bg-blue-500/10">

**Remember:** Matplotlib gives you full control. If something can be customized, Matplotlib can do it.

</div>
