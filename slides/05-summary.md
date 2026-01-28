---
layout: image-right
image: /images/06-summary.jpg
backgroundSize: cover
backgroundPosition: center
class: flex flex-col justify-center
---

# Summary

<div class="text-lg opacity-80 mt-2">Comparing the libraries and key takeaways</div>

---
layout: default
---

# Quick Comparison

<table class="w-full text-sm border border-gray-600">
<thead>
<tr class="bg-gray-700/50">
<th class="text-left py-1.5 px-3 border-r border-gray-600"></th>
<th class="text-left py-1.5 px-3 border-r border-gray-600 text-blue-400">Matplotlib</th>
<th class="text-left py-1.5 px-3 border-r border-gray-600 text-green-400">Seaborn</th>
<th class="text-left py-1.5 px-3 text-orange-400">Plotly</th>
</tr>
</thead>
<tbody>
<tr class="border-b border-gray-600">
<td class="py-1.5 px-3 border-r border-gray-600 font-semibold">Best For</td>
<td class="py-1.5 px-3 border-r border-gray-600">Publications, full control</td>
<td class="py-1.5 px-3 border-r border-gray-600">Quick stats, beautiful defaults</td>
<td class="py-1.5 px-3">Web, exploration</td>
</tr>
<tr class="border-b border-gray-600">
<td class="py-1.5 px-3 border-r border-gray-600 font-semibold">Learning</td>
<td class="py-1.5 px-3 border-r border-gray-600">Moderate</td>
<td class="py-1.5 px-3 border-r border-gray-600">Easy</td>
<td class="py-1.5 px-3">Easy</td>
</tr>
<tr class="border-b border-gray-600">
<td class="py-1.5 px-3 border-r border-gray-600 font-semibold">Interactivity</td>
<td class="py-1.5 px-3 border-r border-gray-600">No</td>
<td class="py-1.5 px-3 border-r border-gray-600">No</td>
<td class="py-1.5 px-3">Yes</td>
</tr>
<tr class="border-b border-gray-600">
<td class="py-1.5 px-3 border-r border-gray-600 font-semibold">3D/Animation</td>
<td class="py-1.5 px-3 border-r border-gray-600">Complex</td>
<td class="py-1.5 px-3 border-r border-gray-600">No</td>
<td class="py-1.5 px-3">Easy</td>
</tr>
<tr>
<td class="py-1.5 px-3 border-r border-gray-600 font-semibold">Output</td>
<td class="py-1.5 px-3 border-r border-gray-600">PNG, PDF, SVG</td>
<td class="py-1.5 px-3 border-r border-gray-600">Via Matplotlib</td>
<td class="py-1.5 px-3">HTML, PNG</td>
</tr>
</tbody>
</table>

<div class="grid grid-cols-3 gap-3 mt-4 text-xs">

<div class="p-2 border-l-4 border-blue-500 bg-blue-500/10 rounded">

**Use Matplotlib when:**
- You need pixel-perfect control
- Creating publication figures
- PDF/print output

</div>

<div class="p-2 border-l-4 border-green-500 bg-green-500/10 rounded">

**Use Seaborn when:**
- Exploring data quickly
- Need statistical plots
- Want beautiful defaults

</div>

<div class="p-2 border-l-4 border-orange-500 bg-orange-500/10 rounded">

**Use Plotly when:**
- Users need to interact
- Building dashboards
- Sharing via web

</div>

</div>

---
layout: default
---

# The Cheat Sheet

<div class="grid grid-cols-3 gap-4 text-sm">

<div class="p-3 border rounded">

### Matplotlib

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x, y)
ax.scatter(x, y)
ax.bar(cats, vals)
ax.hist(data)

fig.savefig("plot.png", dpi=300)
```

</div>

<div class="p-3 border rounded">

### Seaborn

```python
import seaborn as sns

sns.histplot(data=df, x="col")
sns.boxplot(data=df, x="a", y="b")
sns.scatterplot(data=df, x="a",
                y="b", hue="c")
sns.heatmap(corr, annot=True)
sns.pairplot(df, hue="cat")
```

</div>

<div class="p-3 border rounded">

### Plotly

```python
import plotly.express as px

px.scatter(df, x="a", y="b")
px.line(df, x="x", y="y")
px.bar(df, x="cat", y="val")
px.scatter(df, ...,
           animation_frame="year")

fig.write_html("plot.html")
```

</div>

</div>

---
layout: image-right
image: /images/07-exercises.jpg
backgroundSize: cover
backgroundPosition: center
class: flex flex-col justify-center
---

# Exercises

<div class="text-lg opacity-80 mt-2">Hands-on practice with all three libraries</div>

---
layout: default
---

# Practice Exercises

<div class="text-sm opacity-70 mb-3">Hands-on exercises to practice what you have learned.</div>

<div class="grid grid-cols-2 gap-4 text-sm">

<div>

### Exercise 1: Matplotlib Basics
- Create a line plot of a sine wave
- Add axis labels and title
- Save as PNG with 300 DPI

### Exercise 2: Multiple Plots
- Create a 2x2 subplot grid
- Add different plot types to each
- Use `tight_layout()` for spacing

### Exercise 3: Seaborn Statistical
- Load the penguins dataset
- Create a boxplot by species
- Add a hue for sex

</div>

<div>

### Exercise 4: Seaborn Correlation
- Compute correlation matrix
- Create annotated heatmap
- Use diverging colormap

### Exercise 5: Plotly Interactive
- Create scatter with hover data
- Add color by category
- Export as HTML

### Exercise 6: Plotly Animation
- Use gapminder dataset
- Animate through years
- Fix axis ranges

</div>

</div>

<div class="mt-4 p-3 border rounded text-sm">

**File**: `exercises/visualization-exercises.ipynb` - Open in Jupyter Notebook or VS Code

</div>

---
layout: default
---

# Resources

<div class="grid grid-cols-3 gap-6">

<div class="p-4 border rounded">

### Matplotlib

- [Gallery](https://matplotlib.org/stable/gallery/)
- [Cheatsheets](https://matplotlib.org/cheatsheets/)
- [Tutorials](https://matplotlib.org/stable/tutorials/)

</div>

<div class="p-4 border rounded">

### Seaborn

- [Gallery](https://seaborn.pydata.org/examples/)
- [Tutorial](https://seaborn.pydata.org/tutorial.html)
- [API Reference](https://seaborn.pydata.org/api.html)

</div>

<div class="p-4 border rounded">

### Plotly

- [Examples](https://plotly.com/python/)
- [Express Guide](https://plotly.com/python/plotly-express/)
- [Dash (Dashboards)](https://dash.plotly.com/)

</div>

</div>

<div class="mt-8 p-4 border rounded bg-gray-800/50 text-center">

**Next step:** Try recreating a visualization from one of the galleries using your own data.

</div>
