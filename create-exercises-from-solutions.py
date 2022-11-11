import os
import nbformat as nbf

outputDir = 'exercises-from-solutions'
try:
    os.mkdir(outputDir)
except OSError:
    print ("Directory %s already exists" % outputDir)
else:
    print ("Successfully created the directory %s " % outputDir)

for file in os.listdir('.'):
    if file.endswith('.ipynb'):
        print(file)
        ntbk = nbf.read(file, nbf.NO_CONVERT)
        cells_to_keep = []
        for cell in ntbk.cells:
            # we assume that code cells containing serialize blocks are precisely those with solutions we need to delete 
            if cell.cell_type == "code" and "#<xml" in cell.source:
                cell.source = []
                cell.outputs = [] # I like the idea of showing the correct output, but it seems to create loading problems when bandwidth is low
            # blank out answer portion of reflection questions
            if cell.cell_type == "markdown" and "**ANSWER:" in cell.source:
                newSource = []
                for line in cell.source.splitlines():
                    newSource.append(line + "\n")
                    if line.startswith("**ANSWER:"):
                        newSource.append("\n\n<hr>")
                        break
                cell.source = newSource
            cells_to_keep.append(cell)
        new_ntbk = ntbk
        new_ntbk.cells = cells_to_keep
        nbf.write(new_ntbk, os.path.join(outputDir,file), version=nbf.NO_CONVERT)
