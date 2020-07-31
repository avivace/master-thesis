# Experimental Anomaly Detection on CERN CMS Trigger Rates

Source of my a master thesis, typeset in LaTeX using the memoir class, for my MSc in Computer Science at Università degli studi di Milano Bicocca (2019/2020) describing the development and the data science/ML work done at CERN.

Supervisors: Fabio Antonio Stella (**unimib**), Simone Gennai (**INFN**), Glenn Dirkx (**CERN**).

### Building

Run `make` to produce a PDF build. `make publish` updates the build at [avivace.com/thesis.pdf](https://avivace.com/thesis.pdf).

Prerequisites: 

Typefaces:

- Adobe Caslon Pro
- Iosevka Etoile — Quasi-proportional, Slab-serif

Software:

- XeLaTeX
- latexmk
- betterbib
- latexindent
- inkscape (SVG -> PDF figures processing)
- Minted, Pygments (Syntax hightlighting in codeblocks)
- Python3.7, matplotlib and additional Python3 packages (figures generation, see `figures/src`)
- RateMon (to generate CMS Trigger Rate plots, fit functions plotting, ..)

```bash
# On Debian-based systems:
apt install texlive-xelatex latexmk inkscape
pip install betterbib pygments
```

### Figures

Some figures are generated with Python scripts and external tools. Use a virtual environment to set up the dependencies listed in `figures/src/requirements.txt`.

### Software

The actual software related to work reported in the thesis is not included here. See these repositories:

- [RateMon]()
- [RateMon API]()
- [RateMon UI]()
- [Triggers Anomaly Detection]()

### References

- [Minted](https://blog.wizardsoftheweb.pro/syntax-highlighting-in-latex-with-minted/#code)