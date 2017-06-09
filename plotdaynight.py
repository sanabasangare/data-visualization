import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime


# Increasing the map size before any drawing methods
plt.figure(figsize=(22, 10))

# map miller projection
map = Basemap(projection='mill', llcrnrlat=-70, urcrnrlat=90,
              llcrnrlon=-180, urcrnrlon=180, resolution='c')

# plot coastlines, draw label meridians and parallels.
map.drawcoastlines()
map.drawparallels(np.arange(-90, 90, 30), labels=[1, 0, 0, 0])
map.drawmeridians(np.arange(map.lonmin, map.lonmax+30, 60),
                  labels=[0, 0, 0, 1])

# fill continents with 'yellow' (with zorder=0)
# color water areas with 'blue'
map.drawmapboundary(fill_color='blue')
map.fillcontinents(color='yellow', lake_color='blue')

# Show darkness on the regions of the map corresponding to
# the time and date specifed as current time in UTC
time = datetime.utcnow()

map.nightshade(time, )

plt.title('Day & Night Map on %s (UTC)' % time.strftime("%d %b %Y %H:%M:%S"))
plt.show()
