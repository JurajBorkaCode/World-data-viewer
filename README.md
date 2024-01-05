# World data viewer
 A tool to visualize global data

## Description

A command line tool to to plot data from a csv onto a map of the world

## Getting Started

### Dependencies

* Python
* pandas
* pygal
* webbrowser

### Installing

* Install all the modules listed in the dependencies
* Simply open a command line interface at the worldDataGenerator.py file's location.

### Executing program

* The tool should be run with a csv file in the command line
* adding -h shows a help section
```
py worldDataGenerator.py file.csv
py worldDataGenerator.py -h
```

### Example
* When running the program, you will be shown a screen and asked to fill in certain sections

![input](https://github.com/JurajBorkaCode/World-data-viewer/blob/main/example%20input.PNG)

* Once you fill in all of the information, you will be prompted asking you wether you want to generate the map.

* A SVG map will be generated and a list of unsupported countries will be listed.

![output](https://github.com/JurajBorkaCode/World-data-viewer/blob/main/example%20output.PNG)

## Help
A country may not be supported. 
This can be fixed by adding the country and the 2 letter country code into the countryCodes dictionary in the code.  
This should fix the issue. However, some countries may not be supported in the pygal python module.

If you are using a CSV file with a space in the name, put the file in quotation marks.
```
py worldDataGenerator.py  "long file name.csv"
```

## Authors

Juraj Borka