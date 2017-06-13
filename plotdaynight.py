import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime


def plot_day_night(plt):
    # Increasing the map size before any drawing methods
    plt.figure(figsize=(20, 10))

    # map projection
    map = Basemap(projection='robin',
    # map = Basemap(projection='mill', 
                  # llcrnrlon=-180,llcrnrlat=-90,
                  # urcrnrlon=-180, urcrnrlat=90,
                  lat_0=0, lon_0=0,
                  resolution='c')

    # plot coastlines, draw countries, label meridians and parallels.
    map.drawcoastlines(linewidth=0.25)
    map.drawcountries(linewidth=0.25)
    map.drawparallels(np.arange(-90, 91, 60), labels=[1, 0, 0, 0])
    map.drawmeridians(np.arange(map.lonmin, map.lonmax +30, 60),
                      labels=[0, 0, 0, 1])

    # fill continents 'coral' (with zorder=0), color wet areas 'aqua'
    map.drawmapboundary(fill_color='#00FFFF')
    map.fillcontinents(color='#FFFF00', lake_color='#00FFFF')

    # Show darkness on the regions of the map corresponding to
    # the time and date specifed as current time in UTC
    time = datetime.utcnow()

    map.nightshade(time, color='k', delta=0.25,
                   alpha=0.25, ax=None, zorder=2)

    plt.title('Day & Night Map on %s (UTC)' %
              time.strftime("%d %b %Y %H:%M:%S"))

    plt.show()


if __name__ == "__main__":

    plot_day_night(plt)
