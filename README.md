Documentation
=============

Machine learning implementation for cms

see cloudmesh.cmd5

* https://github.com/cloudmesh/cloudmesh.cmd5
### TO DO
* Further develop use of input file i.e. read in line by line and
assign each line to a value currently it just takes the first line.

* MOST Critical set up the post to put new data into set
* Create use of input files for SVM
* Implement def for normalization 
* Create use of input file for knn
* Finish NN implementation
* Implement a decision tree to choose experiment
* Instead of just reading in a csv it would make sense to to read in
  csv and put in the mongoDB then we can add new data to DB

### Data
Identify the useful end points for data gathering and exploring
here. Currently the user most add a data dir before the download will
execute. 

### Experiment

Clean up files and mke seperate .py files for each experiment,
currently they are all wrapped up in one file that is not named in a
useful way.

### Using the service

## File creation
Currently the service takes a downloadble csv file--need to provide how
to do this with google drive.

## Download endpoint
```
localhost:8080/project19/data/output/<output>
```
Where the argument inside the <> is what you want to name you file. 



