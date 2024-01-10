# setup.py

from setuptools import find_packages, setup

setup(
    name="tetty",
    version="0.1.0",
    description="juicy lil tetris homage",
    author="The Dogs",
    packages=find_packages(),
    install_requires=[
    ],
    extras_require={
        "dev": [
            "iniconfig==2.0.0",
            "isort==5.13.2",
            "mypy==1.8.0",
            "mypy-extensions==1.0.0",
            "packaging==23.2",
            "pluggy==1.3.0",
            "pytest==7.4.4",
            "ruff==0.1.11",
            "setuptools-scm==8.0.4",
            "typing_extensions==4.9.0",
        ],
    },
    entry_points={
        # Add any console scripts your project needs
        "console_scripts": [
            "tetty = tetty.app:main",
        ],
    },
    python_requires=">=3.11",
)
