# 📜 Templates

A personal find-and-replace based template system for new project skeletons. Focuses on creating basic configurations with plenty of options and uses composition for certain use cases like CLI programs and servers.


## Try it out

> Requires Python 3.11.x

```bash

# Get into the repo
git clone https://github.com/uhryniuk/tmpltr.git
cd tmpltr

# Build & install locally.
make build
pip install dist/tmpltr-latest.tar.gz

# Generate a basic cli
tmpltr python cli \
    --name "example" \
    --author-name "Johnny Five" \
    --author-email "johnny@five.com" \
    --deps "pandas,numpy,matplotlib" \
    --dir ./

# Build from template
cd example && make build && pip install dist/example-latest.tar.gz

# Run your new cli locally
example --help
```


