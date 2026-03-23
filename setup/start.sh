#!/bin/bash
# Activates the Python virtual environment (if present) and starts starter.py.

ROBUS_CORE="$(cd "$(dirname "$0")/.." && pwd)"
PARENT="$(dirname "$ROBUS_CORE")"

if [ -f "$ROBUS_CORE/venv/bin/activate" ]; then
    echo "Activating venv: $ROBUS_CORE/venv"
    source "$ROBUS_CORE/venv/bin/activate"
elif [ -f "$ROBUS_CORE/env/bin/activate" ]; then
    echo "Activating venv: $ROBUS_CORE/env"
    source "$ROBUS_CORE/env/bin/activate"
elif [ -f "$PARENT/venv/bin/activate" ]; then
    echo "Activating venv: $PARENT/venv"
    source "$PARENT/venv/bin/activate"
elif [ -f "$PARENT/env/bin/activate" ]; then
    echo "Activating venv: $PARENT/env"
    source "$PARENT/env/bin/activate"
else
    echo "No virtual environment found in:"
    echo "  $ROBUS_CORE/venv"
    echo "  $ROBUS_CORE/env"
    echo "  $PARENT/venv"
    echo "  $PARENT/env"
    echo "Using system Python."
fi

python "$ROBUS_CORE/utils/starter.py"
