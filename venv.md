# Create venv folder

`virtualenv venv`

# Activate

`source venv/bin/activate`

# Install requirements

`pip install -r requirements.txt`

# Deactivate

`deactivate`

# Run tests

`python3 -m pytest --html=build/pytest/report.html --self-contained-html`

# Run coverage

`python3 -m coverage run --source dboost --branch -m pytest`

`python3 -m coverage html -d build/coverage`