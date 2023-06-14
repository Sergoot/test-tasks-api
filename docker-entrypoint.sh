set -e

# Activate our virtual environment here
. /opt/pysetup/.venv/bin/activate

export PYTHONPATH=.


# alembic upgrade head

# Evaluating passed command:
exec "$@"