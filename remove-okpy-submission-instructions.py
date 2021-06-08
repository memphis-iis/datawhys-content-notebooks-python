import os
import nbformat as nbf

outputDir = 'new-notebooks'
try:
    os.mkdir(outputDir)
except OSError:
    print ("Directory %s already exists" % outputDir)
else:
    print ("Successfully created the directory %s " % outputDir)

for file in os.listdir('.'):
    if file.endswith('.ipynb'):
        ntbk = nbf.read(file, nbf.NO_CONVERT)
        cells_to_keep = []
        for cell in ntbk.cells:
            # remove okpy submission instructions, which ?always? start with ## Submit
            if cell.cell_type == "markdown" and "## Submit" in cell.source:
                cell.source = []
            cells_to_keep.append(cell)
        new_ntbk = ntbk
        new_ntbk.cells = cells_to_keep
        nbf.write(new_ntbk, os.path.join(outputDir,file), version=nbf.NO_CONVERT)
