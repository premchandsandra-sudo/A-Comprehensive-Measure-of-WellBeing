import sys
import os

# Add project directories to sys.path so app.py can be imported correctly
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
dev_phase_dir = os.path.join(project_root, "5. Project Development Phase")

sys.path.insert(0, dev_phase_dir)
sys.path.insert(0, project_root)

from app import app
