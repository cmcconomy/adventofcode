# Streamlined approach to iPython notebook usage

## Installation
### Requirements
- Python 3.8
- pip
- Virtualenv

### Instructions
- Clone folder
- run `virtualenv env`
- macos/linux: `source env/bin/activate` / windows: `env/scripts/activate`
- pip install -r requirements.txt
- Create a file in the root of the 2019 folder called `.env`
	- This file should contain one line: `AOC_SESSION=019d7234b6f108976h0127dnh01928d7401987j4d41` where this is the session code for your AOC login.
	- Run a browser in developer mode to inspect your cookie after you've logged into AOC to retrieve the 'session' value and enter it into the `.env` file.
	- These credentials are included in .gitignore and will not be submitted to your source control.

## Running
Run `jupyter notebook AOC-2019.ipynb` to launch a local notebook and open the 2019 notebook.

