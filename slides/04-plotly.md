---
layout: image-right
image: /images/05-plotly.jpg
backgroundSize: cover
backgroundPosition: center
class: flex flex-col justify-center
---

# Plotly

<div class="text-orange-400 text-lg mt-2">Interactive Visualizations for the Web</div>

---
layout: default
---

# Why Interactive?

<div class="grid grid-cols-2 gap-4">

<div>

```python
import plotly.express as px

tips = px.data.tips()

fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    color="day",
    hover_data=["size"]
)
fig.show()
```

<div class="text-xs opacity-70 mt-2">

**Try it:** hover for details, zoom by dragging, double-click to reset

</div>

</div>

<div>

<iframe src="./plotly/plotly_scatter_tips.html" class="w-full h-80 border rounded"></iframe>

</div>

</div>

---
layout: default
---

# Interactive Scatter Plot

<div class="grid grid-cols-2 gap-4">

<div>

```python
import plotly.express as px

df = px.data.gapminder()
df_2007 = df[df["year"] == 2007]

fig = px.scatter(
    df_2007,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True
)
```

<div class="text-xs mt-2">

- Hover to see country name
- Click legend to toggle continents
- Use toolbar to zoom/download

</div>

</div>

<div>

<iframe src="./plotly/plotly_scatter.html" class="w-full h-80 border rounded"></iframe>

</div>

</div>

---
layout: default
---

# Line Charts

<div class="grid grid-cols-2 gap-4">

<div>

```python
countries = ["United States", "China", "India"]
df_subset = df[df["country"].isin(countries)]

fig = px.line(
    df_subset,
    x="year",
    y="gdpPercap",
    color="country",
    markers=True
)
```

<div class="text-xs mt-2">

- Hover shows exact values
- Click legend to hide/show lines
- Use `markers=True` for data points

</div>

</div>

<div>

<iframe src="./plotly/plotly_line.html" class="w-full h-80 border rounded"></iframe>

</div>

</div>

---
layout: default
---

# Bar Charts

<div class="grid grid-cols-2 gap-4">

<div>

```python
tips = px.data.tips()

fig = px.bar(
    tips,
    x="day",
    y="total_bill",
    color="sex",
    barmode="group"  # or "stack"
)
```

<div class="text-xs mt-2">

- Hover shows individual bar values
- Click legend to filter categories
- Use `barmode="group"` or `barmode="stack"`

</div>

</div>

<div>

<iframe src="./plotly/plotly_bar.html" class="w-full h-80 border rounded"></iframe>

</div>

</div>

---
layout: default
---

# Animations

<div class="grid grid-cols-2 gap-4">

<div>

```python
df = px.data.gapminder()

fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    animation_frame="year",
    log_x=True,
    range_y=[25, 90]
)
```

<div class="text-xs mt-2">

- `animation_frame=` column to animate
- `range_x=`, `range_y=` fix axes
- Famous "Hans Rosling" style

</div>

</div>

<div>

<iframe src="./plotly/plotly_animation.html" class="w-full h-80 border rounded"></iframe>

<div class="text-xs text-center mt-1 opacity-70">Press play or drag the slider</div>

</div>

</div>

---
layout: default
---

# 3D Plots

<div class="grid grid-cols-2 gap-4">

<div>

```python
df = px.data.iris()

fig = px.scatter_3d(
    df,
    x="sepal_length",
    y="sepal_width",
    z="petal_width",
    color="species"
)
```

<div class="text-xs mt-2">

- Drag to rotate the view
- Scroll to zoom in/out
- Great for 3+ dimensional data
- Use sparingly - 2D often clearer

</div>

</div>

<div>

<iframe src="./plotly/plotly_3d.html" class="w-full h-80 border rounded"></iframe>

</div>

</div>

---
layout: default
---

# Saving Plotly Figures

<div class="grid grid-cols-2 gap-8">

<div>

### Interactive HTML

```python
fig.write_html("plot.html")
```

- Opens in any browser
- Full interactivity preserved
- Can email or embed in websites

</div>

<div>

### Static Images

```python
# Requires: pip install kaleido
fig.write_image("plot.png")
fig.write_image("plot.pdf")
```

- Good for presentations
- Loses interactivity
- Same as Matplotlib output

</div>

</div>

<div class="mt-6 p-4 border rounded bg-orange-500/10">

**Tip:** Use HTML for sharing data exploration. Use PNG/PDF when interactivity is not needed.

</div>

---
layout: default
---

# Plotly Essentials

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="p-4 border rounded">

### Themes

```python
fig = px.scatter(df, x="x", y="y",
                 template="plotly_white")
# Options: plotly, plotly_white,
#          plotly_dark, ggplot2
```

</div>

<div class="p-4 border rounded">

### Custom Layout

```python
fig.update_layout(
    title="My Title",
    xaxis_title="X Label",
    yaxis_title="Y Label"
)
```

</div>

</div>

<div class="mt-6 p-4 border rounded bg-orange-500/10">

**Remember:** Plotly Express is for quick plots. For complex customization, Plotly also has `graph_objects` (not covered here).

</div>
