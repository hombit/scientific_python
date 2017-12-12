# Creates and activates virtualenv for the scientific_python project.
# Do not call it directly. Instead type
# $ . ./virtualenv_activation.sh
# or
# $ source ./virtualenv_activation.sh
# You can deactivate virtualenv typing
# $ deactivate


ENV=$HOME/.virtualenvs/scientific_python
mkdir -vp $ENV
virtualenv $ENV  # for Python 3 use `python -m venv $ENV` instead
source $ENV/bin/activate

PYTHON_PATH=$(which python)
if [ "${PYTHON_PATH/$ENV}" = "${PYTHON_PATH}" ]; then
    echo "Activation failed"
else
    pip install -r requirements.txt
    python setup.py develop
fi
