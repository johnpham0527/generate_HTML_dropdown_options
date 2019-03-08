# This Python code generates HTML drop-down selection options given a list of names strings from an input file.

def generateHTMLDropDownOptions(inputFileName, outputFileName="dropdown_output.txt"): #
    with open(inputFileName, encoding = 'utf-8') as inputFileHandler:  #open the given file for reading and automatically close it
        outputFileHandler = open(outputFileName,'w') #open the output file for writing
        for inputItem in inputFileHandler: #for each item in the input file
            modifiedString = inputItem.rstrip() #remove trailing white space such as line breaks
            outputString = "<option value=\"" + modifiedString + "\">" + modifiedString + "</option>\n"
            print(outputString) #print the result to the screen
            outputFileHandler.write(outputString) #write the result to the output file
        outputFileHandler.close() #close the output file

generateHTMLDropDownOptions("community_libraries.txt","community_library_dropdown_options.txt")