# XY Utilities
Utilities for working with "XY data" in LabVIEW

## Getting Started
- Download and install using the VI Package Manager as described [here](https://levylabpitt.github.io/)
- [Video tutorial](https://www.youtube.com/watch?v=hYuaFTodvhw)

## Usage

The primitive datatype is "XY-data", a cluster containing an X and Y array:

![XY-Data](images/XY-Data.png)

Arrays of XY-data are also supported:

![XY-Data-Array](images/XY-Data-Array.png)

### Arithmetic Functions
#### Add.vi

![Add](images/Add.vi.png)

#### Subtract.vi

![Subtract.vi](images/Subtract.vi.png)

#### Multiply.vi

![Multiply.vi](images/Multiply.vi.png)

#### Divide.vi

![Divide.vi](images/Divide.vi.png)

#### Square.vi

![Square.vi](images/Square.vi.png)

### XY 'Array' Functions
#### Reverse.vi

![Reverse.vi](images/Reverse.vi.png)

#### Sort.vi

![Sort.vi](images/Sort.vi.png)

#### Decimate.vi

![Decimate.vi](images/Decimate.vi.png)

#### Decimate Array.vi

![Decimate Array.vi](images/Decimate-Array.vi.png)

#### Swap X and Y.vi

![Swap X and Y.vi](images/Swap-X-and-Y.vi.png)

#### Get X and Y.vi

![Get X and Y.vi](images/Get-X-and-Y.vi.png)

##### Append.vi

![Append.vi](images/Append.vi.png)

### Signal Processing
#### Derivative.vi

![Derivative.vi](images/Derivative.vi.png)

#### Resample.vi

![Resample.vi](images/Resample.vi.png)

#### Interpolate.vi

![Interpolate.vi](images/Interpolate.vi.png)

#### Interpolate Y.vi

![Interpolate Y.vi](images/Interpolate-Y.vi.png)

#### Interpolate Parameter.vi

![Interpolate Parameter.vi](images/Interpolate-Parameter.vi.png)

#### Average.vi

![Average.vi](images/Average.vi.png)

#### FFT Spectrum.vi

![FFT Spectrum.vi](images/FFT-Spectrum.vi.png)

#### FFT Power Spectrum.vi

![FFT Power Spectrum.vi](images/FFT-Power-Spectrum.vi.png)

#### Shift Zero.vi

![Shift Zero.vi](images/Shift-Zero.vi.png)

#### Symmetrize.vi

![Symmetrize.vi](images/Symmetrize.vi.png)

### 2D Array Conversion

#### 2D to YX.vi

![image](https://github.com/user-attachments/assets/d910acd5-da24-4182-9bf3-f50d6d4796a5)

#### 2D to YX.vi

![image](https://github.com/user-attachments/assets/d7181732-4c95-45ea-a0a1-5569bf60d50a)

#### XY to 2D.vi

![image](https://github.com/user-attachments/assets/8506c907-e7f7-4d49-a088-1728f6396368)

### Waveform Conversion

#### Waveform to XY.vi

![Waveform to XY.vi](images/Waveform-to-XY.vi.png)

#### XY to Waveform.vi

![XY to Waveform.vi](images/XY-to-Waveform.vi.png)

## Examples

### Tree.vi

![Tree.vi](images/Tree.vi.png)

**Tree.vi** shows all of the subVIs contained in the xy_utilities.lvlib library. It also displays the equivalent LabVIEW primitive VI (for example xy_utilities.lvlib:Sort.vi is equivalent to Sort 1D Array).

#### Arithemtic Functions

![Tree-0-Arithmetic](images/Tree-0-Arithmetic.png)

#### Array Functions

![Tree-1-Array](images/Tree-1-Array.png)

#### Signal Processing

![Tree-2-Signal-Processing](images/Tree-2-Signal-Processing.png)

#### Waveform Conversion

![Tree-3-Waveform](images/Tree-3-Waveform.png)

### Test.vi

![Test.vi](images/Test.vi.png)

**Test.vi** is a JKI State Machine that demonstrates how to build a signal processing application with scripted states.

## Contributing
Please contact [Patrick Irvin](https://github.com/ciozi137)

## License
[BSD-3](https://opensource.org/licenses/BSD-3-Clause)
