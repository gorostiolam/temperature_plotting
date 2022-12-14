import pandas as pd
from matplotlib import pyplot as plt


def compute_mean(data):
    """Compute the mean of a list of numbers

    Args:
        data (list): a list of numbers

    Returns:
        float: the mean value of the list
    """
    mean = sum(data)/ len(data)
    return mean

def read_data(filename, colname, num_measurements):
    """Read data from a file and select a column

    Args:
        filename (str): The name of the input file
        colname (str): The name of the column that will be used
        num_measurements (int): The number of measurements used

    Returns:
        pandas.core.series.Series: the data from a single column of a pandas df
    """
    data = pd.read_csv(filename, nrows=num_measurements)
    data_read = data[colname]
    return data_read

def create_name(num):
    """Create a name for an outputfile

    Args:
        num (int): Number that identifies the type of run

    Returns:
        str: A name for a png file
    """
    name = f"plot_{str(num)}.png"
    return name

def plot_data(data, mean, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.plot(data, "r-")
    ax.axhline(y=mean, color="b", linestyle="--")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return(fig, ax)

def save_plot(fig, num):
    name = create_name(num)
    fig.savefig(name)
    fig.clf

def main():
    for num_measurements in [25, 100, 500]:
        temperatures = read_data("data/temperatures.csv", "Air temperature (degC)", num_measurements)
        mean = compute_mean(temperatures)
        fig, ax = plot_data(data = temperatures,
                            mean = mean,
                            xlabel = "measurements",
                            ylabel = "air temperature (deg C)")
        save_plot(fig, num_measurements)


if __name__ == "__main__":
    main()
