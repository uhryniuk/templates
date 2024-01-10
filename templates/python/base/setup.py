# setup.py

from setuptools import find_packages, setup

setup(
    name="tetty",
    version="0.1.0",
    description="juicy lil tetris homage",
    author="The Dogs",
    packages=find_packages(),
    install_requires=[
        # Specify your project dependencies here
        "annotated-types==0.6.0",
        "anyio==4.2.0",
        "click==8.1.7",
        "fastapi==0.108.0",
        "h11==0.14.0",
        "httptools==0.6.1",
        "idna==3.6",
        "pydantic==2.5.3",
        "pydantic_core==2.14.6",
        "python-dotenv==1.0.0",
        "PyYAML==6.0.1",
        "sniffio==1.3.0",
        "starlette==0.32.0.post1",
        "typing_extensions==4.9.0",
        "uvicorn==0.25.0",
        "uvloop==0.19.0",
        "watchfiles==0.21.0",
        "websockets==12.0",
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
