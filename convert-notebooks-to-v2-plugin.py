import os
import nbformat as nbf

outputDir = 'notebooks-converted-to-v2-plugin'
try:
    os.mkdir(outputDir)
except OSError:
    print ("Directory %s already exists" % outputDir)
else:
    print ("Successfully created the directory %s " % outputDir)


replaceList = [
    ("importAs","importAs_Python"),
    ("importFrom","importFrom_Python"),
    ("dummyOutputCodeBlock","dummyOutputCodeBlock_Python"),
    ("dummyNoOutputCodeBlock","dummyNoOutputCodeBlock_Python"),
    ("valueOutputCodeBlock","valueOutputCodeBlock_Python"),
    ("valueNoOutputCodeBlock","valueNoOutputCodeBlock_Python"),
    ("comprehensionForEach","comprehensionForEach_Python"),
    ("indexer","indexer_Python"),
    ("setBlock","setBlock_Python"),
    ("sortedBlock","sortedBlock_Python"),
    ("zipBlock","zipBlock_Python"),
    ("dictBlock","dictBlock_Python"),
    ("listBlock","listBlock_Python"),
    ("tupleBlock","tupleBlock_Python"),
    ("tupleConstructorBlock","tupleConstructorBlock_Python"),
    ("reversedBlock","reversedBlock_Python"),
    ("boolConversion","boolConversion_Python"),
    ("intConversion","intConversion_Python"),
    ("floatConversion","floatConversion_Python"),
    ("strConversion","strConversion_Python"),
    ("withAs","withAs_Python"),
    ("textFromFile","textFromFile_Python"),
    ("openReadFile","openReadFile_Python"),
    ("openWriteFile","openWriteFile_Python"),
    ("varGetProperty","varGetProperty_Python"),
    ("varDoMethod","varDoMethod_Python"),
    ("varCreateObject","varCreateObject_Python")
    ]

for file in os.listdir('.'):
    if file.endswith('.ipynb'):
        ntbk = nbf.read(file, nbf.NO_CONVERT)
        cells_to_keep = []
        for cell in ntbk.cells:
            # only mess with code cells that have xml 
            if cell.cell_type == "code" and "#<xml" in cell.source:
                # using a list of known block names, do replacement
                new_source = cell.source
                for v1,v2 in replaceList:
                    new_source = new_source.replace(v1, v2)
                cell.source = new_source
                # cell.source = []
                # cell.outputs = [] # I like the idea of showing the correct output, but it seems to create loading problems when bandwidth is low
            # blank out answer portion of reflection questions
            # if cell.cell_type == "markdown" and "**ANSWER:" in cell.source:
            #     newSource = []
            #     for line in cell.source.splitlines():
            #         newSource.append(line + "\n")
            #         if line.startswith("**ANSWER:"):
            #             newSource.append("\n\n<hr>")
            #             break
            #     cell.source = newSource
            cells_to_keep.append(cell)
        new_ntbk = ntbk
        new_ntbk.cells = cells_to_keep
        nbf.write(new_ntbk, os.path.join(outputDir,file), version=nbf.NO_CONVERT)
