"""
NumpyExampleModule - NumPy Integration Examples for LabVIEW

This module demonstrates how to call NumPy functions from LabVIEW using the Python node.
It provides two patterns for passing array data and performing mathematical operations.

Author: Patrick Irvin
Date: December 2025
Requirements:
 - Python version matches LabVIEW bitness
 - numpy
"""

import numpy as np

# =============================================================================
# Example 1: Cluster-Based Interface (Minimal LabVIEW Wiring)
# =============================================================================

def XY_NumpyMath(xy, operation, params):
    """
    Perform NumPy operations using a cluster input containing two arrays.
    
    This function accepts arrays bundled in a LabVIEW cluster, making it easy
    to wire with minimal connections in the block diagram.
    
    Parameters
    ----------
    xy : tuple of array-like
        A tuple/cluster containing two arrays: (x, y)
        - xy[0] : first array (x)
        - xy[1] : second array (y)
    operation : str
        The operation to perform:
        - 'add' : element-wise addition (x + y)
        - 'multiply' : element-wise multiplication (x * y)
        - 'norm_x' : L2 norm of x
        - 'norm_y' : L2 norm of y
        - 'dot' : dot product of x and y (using matmul)
        - default : returns x unchanged
    params : str
        Reserved for future use (additional parameters/configuration)
    
    Returns
    -------
    tuple of ndarray
        (x, result) where:
        - x : original first array unchanged
        - result : operation result as 1D array
    
    Examples
    --------
    In LabVIEW, wire:
    - A cluster containing two 1D arrays to xy
    - A string control with operation name to operation
    - An empty string to params
    
    Notes
    -----
    The output tuple maps back to a LabVIEW cluster with two array elements.
    """
    x = np.array(xy[0])
    y = np.array(xy[1])
    
    if operation == 'add':
        result = x + y
    elif operation == 'multiply':
        result = x * y
    elif operation == 'norm_x':
        result = np.linalg.norm(x)
    elif operation == 'norm_y':
        result = np.linalg.norm(y)
    elif operation == 'dot':
        result = np.matmul(x, y)
    else:
        result = x  # default: return x unchanged
    
    return (x, np.atleast_1d(result))


# =============================================================================
# Example 2: Separate Arrays Interface (More Flexible)
# =============================================================================

def NumpyMath(x, y, operation, params):
    """
    Perform NumPy operations using separate array inputs.
    
    This function accepts arrays as separate parameters, providing more
    flexibility for wiring different data sources in LabVIEW.
    
    Parameters
    ----------
    x : array-like
        First input array
    y : array-like
        Second input array
    operation : str
        The operation to perform:
        - 'add' : element-wise addition (x + y)
        - 'multiply' : element-wise multiplication (x * y)
        - 'norm_x' : L2 norm of x
        - 'norm_y' : L2 norm of y
        - 'dot' : dot product of x and y (using matmul)
        - default : returns x unchanged
    params : str
        Reserved for future use (additional parameters/configuration)
    
    Returns
    -------
    tuple of ndarray
        (x, result) where:
        - x : original first array unchanged
        - result : operation result as 1D array
    
    Examples
    --------
    In LabVIEW, wire:
    - First 1D array to x
    - Second 1D array to y
    - A string control with operation name to operation
    - An empty string to params
    
    Notes
    -----
    This interface allows users to wire arrays from different sources more easily
    than bundling them into a cluster first.
    """
    x = np.array(x)
    y = np.array(y)
    
    if operation == 'add':
        result = x + y
    elif operation == 'multiply':
        result = x * y
    elif operation == 'norm_x':
        result = np.linalg.norm(x)
    elif operation == 'norm_y':
        result = np.linalg.norm(y)
    elif operation == 'dot':
        result = np.matmul(x, y)
    else:
        result = x  # default: return x unchanged
    
    return (x, np.atleast_1d(result))


# =============================================================================
# Debugging Utilities
# =============================================================================

def TestCluster(cluster):
    """
    Debug function to inspect Python datatypes from LabVIEW.
    
    This utility function helps verify how LabVIEW datatypes are converted
    to Python types when passed through the Python node.
    
    Parameters
    ----------
    cluster : any
        Any LabVIEW datatype to inspect
    
    Returns
    -------
    str
        A string describing the Python type and value
    
    Examples
    --------
    Use this to verify:
    - How LabVIEW clusters map to Python tuples
    - How arrays are converted
    - What datatypes are passed for various LabVIEW controls
    """
    type_info = f"Type: {type(cluster)}, Value: {cluster}"
    return type_info


# =============================================================================
# Usage Guide
# =============================================================================
"""
GETTING STARTED:

1. In LabVIEW, add a Python Node from the Connectivity palette
2. Configure the Python Node:
   - Module Path: directory containing this .py file
   - Function Name: XY_NumpyMath or NumpyMath
   - 'XY_' in front of function name tells LabVIEW to pass in the data as a cluster
3. Wire inputs according to the function signature
4. To modify behavior, edit the Python code - no LabVIEW changes needed!

DATATYPE MAPPINGS:

LabVIEW --> Python:
- 1D Array --> list or tuple
- Cluster --> tuple (elements in order)
- String --> str
- Numeric --> int or float

Python --> LabVIEW:
- tuple --> Cluster (elements in order)
- list/ndarray --> 1D Array
- str --> String
- int/float --> Numeric

TIPS:
- Keep Python logic simple and well-documented
- Use descriptive operation strings
- Test with TestCluster() to verify datatypes
- Reserve 'params' for future extensibility
"""