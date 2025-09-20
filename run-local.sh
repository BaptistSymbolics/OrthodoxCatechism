#!/bin/bash

# Create the dist directory if it doesn't exist
mkdir -p dist

# Run the Python script to generate LaTeX directly
python scripts/toml_to_latex.py -s src -o dist/orthodox-catechism.tex

# First run of xelatex to generate initial PDF and auxiliary files
docker run --rm --volume "$(pwd):/data" --workdir /data texlive/texlive:latest \
  xelatex -interaction=nonstopmode -output-directory=dist dist/orthodox-catechism.tex

# Second run of xelatex to incorporate table of contents and references
docker run --rm --volume "$(pwd):/data" --workdir /data texlive/texlive:latest \
  xelatex -interaction=nonstopmode -output-directory=dist dist/orthodox-catechism.tex

# Copy the final PDF to the final directory
cp dist/orthodox-catechism.pdf final/orthodox-catechism.pdf

echo "Orthodox Catechism PDF generation complete!"
