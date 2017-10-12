# Creates and activates virtualenv for the scientific_python project.
# Do not call it directly. Instead type
# $ . ./virtualenv_activation.sh
# or
# $ source ./virtualenv_activation.sh
# You can deactivate virtualenv typing
# $ deactivate


ENV=$HOME/.virtualenvs/scientific_python
mkdir -vp $ENV
virtualenv $ENV
source $ENV/bin/activate

PYTHON_PATH=$(which python)
if [ "${PYTHON_PATH/$ENV}" = "${PYTHON_PATH}" ]; then
    echo "Activation failed"
else
    python setup.py install
    pip install -r requirements.txt
fi
