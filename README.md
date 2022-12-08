# Electric-Field-Visualization
> This project was made for Shwartz-Raisman Institute of Technology competition.

The project aim is to visualize Electric field lines with python. There are two main possible implementations:
- Matplotlib
- Pygame

# Matplotlib Implementation

## Installation
In order to install the required packages run:
```bash
cd venv/bin/Activate.ps1; pip install requirments.txt 
```
For numpy individual installation (might cause problems trying to download with pip):
```bash
py -3.10 -mpip install pipwin
py -3.10 -mpipwin refresh
py -3.10 -mpipwin install numpy
```
 The installation process will be much shorter and easier in python <= 3.8.
 
## Scientific explanation 
With matplotlib the implementation is quite staright forward. We generate randomly a couple of chargers on the grid based on the system arg. Then, we can calculate the field - create several matrixes using numpy to represent the Electric Field on every point on the grid, and calculate it using a function. Now we can pass the matrixes with the field's values to matplotlib and get the graph with the charges and field lines.


**For E_y:**
$$\large E_y = \frac{q * K * sin(a)}{r^2}\ $$ $$\Large -->$$  
$$\large E_y = \frac{q * K * dy/r}{r^2}\ $$ $$\Large -->$$
$$\large E_y = \frac{q * K * dy}{r^3}\ $$ 

<p>
We can ignore K because we try to find the sum of all fields that are a multiply of K and the ratio will remain the same.
Final Formula for Ey: 
</p>
$$\Large E_y = \frac{q * dy}{r^3}\ $$ 


# Usage
Run command:
```bash
python3 matplotlib_implementation.py <ARGS>
```

### Example run:
![image](https://user-images.githubusercontent.com/101902014/206561069-f9c47ede-5634-41a2-ac04-239c345dbf4f.png)


# Pygame Implementation
