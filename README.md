# A Multiplication Lib
Example of python packaging.

# Installing
## From Private PyPi (playground)
run:
`pip install --extra-index-url https://arruda.pythonanywhere.com/simple super_kawaii_multiplication_lib`

## From Official PyPi
run:
`pip install super_kawaii_multiplication_lib`
**ps**: (check name of your lib, needs to be unique in the official pypi)

## Using the lib:

```python
from super_kawaii_multiplication_lib import *

print(fancy_multiplication(4, 5, 6))
```

Test this by running: `python example/my_script.py`


# Development Setup
run:
`pip install .[dev]`

Will install dev libs.

## Running Tests
run:
`python -m unittest discover`


## Building package
run:

`python -m build`

## Uploading

### Using private pypi (playground)
run:
`twine upload --repository-url https://arruda.pythonanywhere.com dist/*`

### Using official PyPi
run:
`twine upload dist/*`
You will be asked for you PyPi credentials.
**ps:** you may have to [create a API token](https://pypi.org/help/#apitoken) for your PyPi account and use it instead. Also avoid clutering by publishing fake packages to the official PyPi repository if you are just testing the process out.

# License
See `LICENSE` file for details.