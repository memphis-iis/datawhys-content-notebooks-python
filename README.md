# DataWhys Content Notebooks

This repository contains data science training content for DataWhys in the form of JupyterLab notebooks (.ipynb files).

These notebooks are completely portable to all JupyterLab environments but require the Blockly extension for the full user experience (see prerequisites below).

For a complete list of topics covered, see [the course outline](Course-outline.ipynb).
Each topic has an introduction/worked example notebook and an independent problem solving notebook (`-PS`).


All materials are currently in Python.
Versions in R are forthcoming.

## Internal development

Any other content-related materials, e.g. spreadsheets, should be placed [in the OneDrive folder](https://livememphis-my.sharepoint.com/:f:/r/personal/aolney_memphis_edu/Documents/DataWhys/content-planning?csf=1&e=LPEGbr). If you create an issue that references a document in that folder, please try to link to said document.

If you want to change/correct content, either create an issue describing your change or [use a `git` workflow to make the change](https://www.atlassian.com/git/tutorials/making-a-pull-request).

## Prerequisites

### Development

- [JupyterLab](https://jupyter.org/install)
- [Blockly extension](https://github.com/aolney/fable-jupyterlab-blockly-extension) (optional but strongly recommended)
- [Xeus Python Kernel](https://github.com/jupyter-xeus/xeus-python) (optional but strongly recommended)

### Static viewing

Click on any notebook in the repository, and GitHub will render it in your browser as a non-interactive document.

### Dynamic viewing

Editors/content creators should follow the prerequisites for development.

Casual viewers can interact with notebooks by clicking on the Binder badge below.
Note Binder does not currently include the Blockly extension.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/memphis-iis/datawhys-content-notebooks/master?urlpath=lab)

