ZMT to Cartesian Conversion (parameters) Tool

This Python script allows you to convert Z-Matrix (ZMT) coordinates to Cartesian coordinates. It calculates bond lengths, angles, and dihedral angles from the Z-Matrix and XYZ files.

Table of Contents:
1. Prerequisites
2. Project Structure
3. How to Execute
4. Input Files and Format
5. Files and Modules
6. Example Input Files

1. Prerequisites:
- Python 3.x installed on your system.
- NumPy library is required. You can install it using: `pip install numpy`.

2. Project Structure:
The project is organized into several files to manage different aspects of the conversion process.

- calculations.py: Calculates bond lengths, angles, and dihedral angles using provided ZMT coordinates and XYZ file.
- data_processing.py: Processes the ZMT input file to create dictionaries for different arrays.
- main.py: The main script that orchestrates the entire conversion process.
- utils.py: Contains utility functions to read input, perform array operations, and calculate geometric properties.
- connect.txt: Input ZMT file containing Z-Matrix coordinates.
- First.xyz: XYZ file containing Cartesian coordinates.

3. How to Execute:
- Ensure that you have the necessary prerequisites installed.
- Place the input files "connect.txt" and "First.xyz" in the same directory as the script files.
- Open a terminal or command prompt and navigate to the directory containing the script files.
- Run the main.py script using the command: `python main.py`.

4. Input Files and Format:
- "connect.txt": Z-Matrix input file containing ZMT coordinates. The file should be formatted as follows:

Atom1 Index Atom2 Index Bond Length
Atom2 Index Atom3 Index Bond Length Angle
Atom3 Index Atom4 Index Bond Length Angle Dihedral Angle
...

- "First.xyz": XYZ file containing Cartesian coordinates. The file should be formatted as follows:

Number of Atoms
Atom Symbol X Y Z
Atom Symbol X Y Z
...

Example:
3
C 0.0 0.0 0.0
H 1.0 0.0 0.0
H 0.0 1.0 0.0


5. Files and Modules:
- utils.py: Contains utility functions to read input, perform array operations, and calculate geometric properties.
- data_processing.py: Processes ZMT input and creates dictionaries for different arrays.
- calculations.py: Calculates bond lengths, angles, and dihedral angles.
- main.py: Orchestrates the conversion process and saves calculated values to a text file.

6. Example Input Files:
- "connect.txt": Provided ZMT input file with sample Z-Matrix coordinates.
- "First.xyz": Provided XYZ file with sample Cartesian coordinates.

Important Note:
This tool assumes that the input files are formatted correctly. Ensure that the ZMT input file and XYZ file match the expected format.

For any issues or questions, feel free to contact [Dilawars941@.gmail].

##License
MIT License

Copyright (c) [2023] [Dilawar Singh Siodiya]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

