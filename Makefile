### Global Variables ###
VENV_DIR := venv

### Cross Platform  ###
ifeq ($(OS),Windows_NT)
		ACTIVATE := $(VENV_DIR)\Scripts\activate
		RM := rmdir /s /q
		SHELL := "CMD"
else
	ACTIVATE := source $(VENV_DIR)/bin/activate
	RM := rm -rf
	SHELL := "BASH"
endif

### Virtual Environment ###
rmvenv:
	@$(RM) $(VENV_DIR)

venv:
	@echo Creating virtual envionrment in the $(VENV_DIR) directory...
	@python -m venv $(VENV_DIR)
	@echo Done! Now run the following command in $(SHELL) to activate and install:
	@echo "$(ACTIVATE) && echo pip install -r requirements.txt"


### Build Python Packages ###
rmbuild:
	@$(RM) build && echo Removing \'build\' folder
	@$(RM) dist && echo Removing \'dist\' folder
	@$(RM) tetty.egg-info && echo Removing \'tetty.egginfo\' folder

build: 
	@echo Running build
	python setup.py sdist bdist_wheel
	@echo Build complete


### Global Clean ###
clean: rmvenv rmbuild

### Run Modules
dev:
	@python -m 
	@uvicorn tetty.app:app --reload

d: dev 

.PHONY: dev d
