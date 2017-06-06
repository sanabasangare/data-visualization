import matplotlib.pyplot as plt
from collections import Counter


def bar_chart(plt):

    # Increasing the size of the chart figure
    plt.figure(figsize=(20, 10))

    # years observed since 2000
    years = [2000, 2002, 2005, 2007, 2010, 2012, 2014, 2015]

    # total number of websites on the world wide web
    # (source: Internet Live Stats)
    num_websites = [17, 38, 64, 121, 206, 697, 968, 863]

    # bars are by default width 0.8, adding 0.1 centers each bar
    xs = [i + 0.1 for i, _ in enumerate(years)]

    # plot bars with left x-coordinates [xs], heights [num_websites]
    plt.bar(xs, num_websites, color='green')
    plt.ylabel("# of Websites (millions)")
    plt.title("Total number of websites online")

    # label x-axis with the years at bar centers
    plt.xticks([i + 0.1 for i, _ in enumerate(years)],
               years, color='blue')

    plt.show()


if __name__ == "__main__":

    bar_chart(plt)
