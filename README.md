# Electric-Field-Visualization
> This project was made for Shwartz-Raisman Institute of Technology competition.

The project aim is to visualize Electric field lines with python. There are two main possible implementations:
- Matplotlib
- Pygame

With matplotlib the implementation is quite staright forward. We generate randomly a couple of chargers on the grid based on the system arg. Then, we can calculate the field - create several matrixes using numpy to represent the Electric Field on every point on the grid, and calculate it using a function. Now we can give the matrixes with the field's values to matplotlib and get the graph.

usage:
```bash
python3 matplotlib_implementation.py <ARGS>
```

For Ey:
q * K * sin(a) / r ** 2  -->
  q * K * dy/r / r  ** 2   -->
    q * K * dy / r ** 3
We can ignore K because we try to find the sum of all fields that are a multiply of K and the ratio will remain the same.
Final Formula: q * dy / r ** 3 

```bash
python -m venv venv

py -3.10 -mpip install pipwin
py -3.10 -mpipwin refresh
py -3.10 -mpipwin install numpy
```

Example run:


