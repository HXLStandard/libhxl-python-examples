# Sample Script for the HXL Python library

This is a simple sample script to demonstrate the use of filter chains
in libhxl, for the
[Humanitarian Exchange Language](http://hxlstandard.org). The script
should work with both Python2 (2.7+) or Python3. Read the comments to
see how the code works.

## Setup

* Get the latest version of [libhxl](https://github.com/HXLStandard/libhxl-python).
* Install the library to pull in dependencies (``python setup.py
  install`` or ``python setup.py develop``).

## Usage

From the command line:

```
python clean-data.py sample-data.csv
python clean-data.py sample-data.xlsx
```

