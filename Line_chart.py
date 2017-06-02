import matplotlib.pyplot as plt
from collections import Counter


def line_graph(plt):

    # years observed since 2000
    years = [2000, 2002, 2005, 2007, 2010, 2012, 2014, 2015]

    # total number of websites on the world wide web
    # (source: Internet Live Stats)
    websites = [17, 38, 64, 121, 206, 697, 968, 863]

    # create a line chart with years on x-axis and number of websites on y-axis
    plt.plot(years, websites, color='blue', marker='o', linestyle='solid',
             linewidth=2)

    # adjust the x and y axis markers
    plt.xlim(2000, 2015)
    plt.ylim(10, 1000)

    # add a title to the chart
    plt.title("Total number of websites online")

    # add a label to the y-axis
    plt.ylabel("Websites (millions)")

    plt.show()

if __name__ == "__main__":

    line_graph(plt)
