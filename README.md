# Electric-Field-Visualization
> This project was made for Shwartz-Raisman Institute of Technology competition.

> The project's aim is to visualize Electric field lines with python.

## Installation
For numpy individual installation (might cause problems trying to download with pip):
```bash
py -3.10 -mpip install pipwin
py -3.10 -mpipwin refresh
py -3.10 -mpipwin install numpy
```
 The installation process might be shorter and easier in conda.
 
## Scientific explanation 
With matplotlib the implementation is quite staright forward. We generate randomly a couple of chargers on the grid based on the system args. Then, we can calculate the field - create several matrixes using numpy to represent the Electric Field on every point on the grid, and calculate it using a function. Now we can pass the matrixes with the field's values to matplotlib and get the graph with the charges and field lines.


**For E_y:**
$$\large E_y = \frac{q * K * sin(a)}{r^2}\ $$  
$$\large E_y = \frac{q * K * dy/r}{r^2}\ $$ 
$$\large E_y = \frac{q * K * dy}{r^3}\ $$ 

<p>
We can ignore K because we try to find the sum of all fields that are a multiply of K and the ratio will remain the same.
Final Formula for Ey (The same goes for Ex): 
</p>

$$\Large E_y = \frac{q * dy}{r^3}\ $$ 


# Usage
Run command:
```bash
python3 matplotlib_implementation.py <ARGS>
```
Or via the `.exe` file:
```bash
.\dist\matplotlib_implementation.exe <ARGS>
```

### Example run:
```bash
.\matplotlib_implementation.exe -c 2
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/101902014/206561069-f9c47ede-5634-41a2-ac04-239c345dbf4f.png" alt=""/>
</p>

