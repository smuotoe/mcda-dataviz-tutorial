---
layout: image-right
image: /images/04-seaborn.jpg
backgroundSize: cover
backgroundPosition: center
class: flex flex-col justify-center
---

# Seaborn

<div class="text-green-400 text-lg mt-2">Statistical Visualization Made Easy</div>

---
layout: default
---

# Seaborn in One Slide

<div class="grid grid-cols-2 gap-8">

<div>

### What It Does

- Beautiful defaults out of the box
- Works directly with DataFrames
- Automatic statistical calculations
- Built on top of Matplotlib

</div>

<div>

### The Pattern

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
sns.scatterplot(data=tips,
                x="total_bill",
                y="tip",
                ax=ax)
```

</div>

</div>

<div class="mt-6 p-4 border rounded border-green-500/30 bg-green-500/10">

**Key insight:** Pass `data=` with a DataFrame, then use column names for `x=`, `y=`, `hue=`, etc.

</div>

---
layout: image-right
image: /verification_output/seaborn_histplot.png
backgroundSize: 90%
backgroundPosition: center
---

# Histograms

Show distribution of a single variable.

```python
sns.histplot(
    data=tips,
    x="total_bill",
    kde=True     # Add density curve
)
```

<div class="mt-4 text-sm">

- `kde=True` adds smooth density
- `hue=` colors by category
- `bins=` controls detail level

</div>

---
layout: image-right
image: /verification_output/seaborn_boxplot.png
backgroundSize: 90%
backgroundPosition: center
---

# Box Plots

Compare distributions across categories.

```python
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="time"
)
```

<div class="mt-4 text-sm">

- Shows median, quartiles, outliers
- Great for comparing groups
- Use `hue=` for sub-groups

</div>

---
layout: image-right
image: /verification_output/seaborn_violinplot.png
backgroundSize: 90%
backgroundPosition: center
---

# Violin Plots

See the full distribution shape.

```python
sns.violinplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="time",
    split=True
)
```

<div class="mt-4 text-sm">

- Shows distribution shape via KDE
- `split=True` for side-by-side
- Better than box plots for bimodal data

</div>

---
layout: image-right
image: /verification_output/seaborn_scatter.png
backgroundSize: 90%
backgroundPosition: center
---

# Scatter Plots with Encodings

Map multiple variables to visual properties.

```python
sns.scatterplot(
    data=penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",    # Color
    size="body_mass_g" # Size
)
```

<div class="mt-4 text-sm">

- `hue=` colors by category
- `size=` scales by value
- `style=` changes marker shape

</div>

---
layout: image-right
image: /verification_output/seaborn_regplot.png
backgroundSize: 90%
backgroundPosition: center
---

# Regression Plots

Show relationships with trend lines.

```python
sns.regplot(
    data=tips,
    x="total_bill",
    y="tip",
    ci=95
)
```

<div class="mt-4 text-sm">

- Automatically fits regression
- Shaded area shows 95% CI
- Use `lmplot()` for faceting

</div>

---
layout: image-right
image: /verification_output/seaborn_heatmap.png
backgroundSize: 90%
backgroundPosition: center
---

# Heatmaps

Visualize correlations or matrices.

```python
corr = penguins.select_dtypes(
    "number"
).corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="RdBu_r",
    center=0
)
```

<div class="mt-4 text-sm">

- `annot=True` shows values
- `center=0` for diverging data
- Perfect for correlation matrices

</div>

---
layout: image-right
image: /verification_output/seaborn_pairplot.png
backgroundSize: 90%
backgroundPosition: center
---

# Pair Plots

See all relationships at once.

```python
sns.pairplot(
    penguins,
    hue="species",
    diag_kind="kde"
)
```

<div class="mt-4 text-sm">

- Scatter plots for all pairs
- Distributions on diagonal
- Great for exploratory analysis

</div>

---
layout: default
---

# Seaborn Essentials

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="p-4 border rounded">

### Set a Theme

```python
sns.set_theme(style="whitegrid")
# Options: darkgrid, whitegrid,
#          dark, white, ticks
```

</div>

<div class="p-4 border rounded">

### Custom Palette

```python
sns.set_palette("colorblind")
# Or: Set1, Set2, husl, viridis
```

</div>

</div>

<div class="mt-6 p-4 border rounded bg-green-500/10">

**Remember:** Seaborn is built on Matplotlib. You can always customize further with `ax.set_title()`, `ax.set_xlabel()`, etc.

</div>
