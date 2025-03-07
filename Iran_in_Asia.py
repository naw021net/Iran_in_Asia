import geopandas as gpd
import matplotlib.pyplot as plt

# بارگیری نقشه جهان
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# انتخاب قاره آسیا
asia = world[world.continent == 'Asia']

# انتخاب کشور ایران
iran = world[world.name == 'Iran']

# ایجاد نقشه
fig, ax = plt.subplots(1, 1, figsize=(15, 10))

# نمایش نقشه آسیا
asia.plot(ax=ax, color='lightgray', edgecolor='black')

# نمایش کشور ایران با رنگ آبی کمرنگ
iran.plot(ax=ax, color='lightblue', edgecolor='black')

# تنظیم عنوان نقشه
ax.set_title('نقشه آسیا با رنگ‌آمیزی ایران')

# نمایش نقشه
plt.show()