<div align="center">
<img src="https://user-images.githubusercontent.com/49791407/186037770-d505c44c-3725-43bd-ba46-d08035277255.png">
<b>Simulates an elastic collision between two objects</b>
</div>
<br>

![](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=blue&color=white) 
![](https://img.shields.io/tokei/lines/github/AJM432/Elastic-Collision-Simulation) 
![](https://img.shields.io/github/repo-size/AJM432/Elastic-Collision-Simulation?style=flat)

## Demo
<div align="center">
<img src="https://user-images.githubusercontent.com/49791407/163589307-2b7e0575-63cb-4824-9abd-0b8e6167df97.gif" style="border: 1px solid white">
</div>

## Program Mechanics
- The program stores information about each object using the Block class.
- Every frame, the program checks for a collision and applies the following function to the velocity of each object.

$$v_a = \frac{m_a - m_b}{m_a + m_b} \cdot v_a + \frac{2m_b}{m_a + m_b} \cdot v_b$$

- Once a block hits a wall, the velocity of the block is inverted.

## License

Elastic-Collision-Simulation is licensed under the ![MIT License](https://github.com/AJM432/Elastic-Collision-Simulation/blob/main/LICENSE.md)