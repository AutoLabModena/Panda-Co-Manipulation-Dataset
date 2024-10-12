# Panda-Co-Manipulation-Dataset
### A dataset of Franka Emika Panda recordings of 2D symbols.

![dataset](https://github.com/user-attachments/assets/dcf92aaf-e12a-4233-add4-427d039acaeb)

Welcome to the **Panda Co-Manipulation Dataset** page! <br>
This is a public available dataset and comprises of 21 different 2D symbols. Each symbol was printed in A4 format, then traced back with the help of a Franka Emika Panda robot, equipped with a Schunk FT-AXIA force/torque sensor. <br>
Six recordings were made for each symbols, by fixing the start and end point to be always the same. In the provided __files.pdf__ related to the symbols, start and end points are represented, respectively, by a circle and an asterisk.

<p align="center">
  <img src="https://github.com/user-attachments/assets/67841964-ded2-4989-a49e-a0452c548ffa" width="200" />
  <img src="https://github.com/user-attachments/assets/16bad41f-8c7f-46ee-8cf4-e21c8f67b6fa" width="200" />
  <img src="https://github.com/user-attachments/assets/ced2d879-6b27-423c-94de-d0b201010374" width="200" />
  <img src="https://github.com/user-attachments/assets/d4ea2900-801a-4849-bc18-1de5950609e3" width="200" />
</p>


A key feature of the dataset is that symbol's recordings of the same group do not differ in path, but instead vary significantly in time, including speed variations and pauses. <br>
The recordings are provided both as MATLAB and Python structures in every symbol folder, named respectively as __symbol_data.mat__ and __symbol_data.npy__ . The structure is the following: <br>
<br>
> symbol_data: structure of 6 elements with fields <br>
> --- symbol_data[i].pos : end-effector position recordings [3xT] <br>
> --- symbol_data[i].vel : end-effector velocity recordings [3xT] <br>
> --- symbol_data[i].F : end-effector force recordings [3xT] <br>
<br>
where T defines the number of samples for each recording.


Load **MATLAB** file example:
```matlab
load('symbol_data.mat');
i = 2; % 2nd recording
pos = symbol_data(i).pos;
vel = symbol_data(i).vel;
F   = symbol_data(i).F;
```
Load **Python** file example:
```python
import numpy as np
symbol_data = np.load('symbol_data.npy')
i = 2 # 2nd recording
pos = symbol_data[i]['pos']
vel = symbol_data[i]['vel']
F   = symbol_data[i]['F']
```


