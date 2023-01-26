import random
import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--charges", required=True, help="Number of charges to be displayed")
parser.add_argument("-r", "--random", default="True", help="Random distribution of charges. True for random False for symmetric")
args = parser.parse_args()


def E(q, coordinates: list, x, y):
    """Calculate electric field

        Args:

            q (float): the electric charge
            coordinates (list[float, float]): list of [x,y] coordinates of the charger
            x (float): x coordinate of the current point
            y (float): y coordinate of the current point

        Returns:
            The electric field in point(x,y) in (Ex, Ey) format
        """

    r_3 = np.hypot(x - coordinates[0], y - coordinates[1]) ** 3
    return q * (x - coordinates[0]) / r_3, q * (y - coordinates[1]) / r_3


if __name__ == "__main__":
    # creating grid
    nx, ny = 64, 64
    x = np.linspace(-2, 2, nx)
    y = np.linspace(-2, 2, ny)
    X, Y = np.meshgrid(x, y)

    # Create a multiple with nq charges of alternating sign, equally spaced
    # on the unit circle.

    nq = 2 ** int(args.charges)
    charges = []

    for i in range(int(args.charges)):
        q = i % 2 * 2 - 1
        if args.random == "True":
            charges.append((q, (random.choice(x), random.choice(y))))
        else:
            charges.append((q, (np.cos(2 * np.pi * i / nq), np.sin(2 * np.pi * i / nq))))

    # Electric field vector, E=(Ex, Ey), as separate components
    Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))

    # Calculate the electric field for each point on the grid
    for charge in charges:
        ex, ey = E(*charge, x=X, y=Y)
        Ex += ex
        Ey += ey

    fig = plt.figure()
    ax = fig.add_subplot()

    # Plot the streamlines with an appropriate colormap and arrow style
    color = 2 * np.log(np.hypot(Ex, Ey))
    ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
                  density=2, arrowstyle='->', arrowsize=1.5)

    # Add filled circles for the charges themselves: red for positive and blue for negative
    charge_colors = {True: '#aa0000', False: '#0000aa'}
    for q, pos in charges:
        ax.add_artist(Circle(pos, 0.05, color=charge_colors[q > 0]))

    # Add labels and axis limits
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    plt.show()
