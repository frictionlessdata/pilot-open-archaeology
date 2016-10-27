# Open Context and datapackage-r

This folder aims at experiment the intersection of Open Context Data with
datapackage-r.

## WIP!

To do list

- [ ] Sanitize `colnames(df)`
- [ ] Improve inferring of types 
- [ ] If not possible otherwise, script the edit of `data/datapackage.json` 

## How it works

Go to data-raw/ and in the CL write

    make 

## Dependencies for R

**datapkg** https://github.com/frictionlessdata/datapackage-r

    library(devtools)
    install_github("hadley/readr")
    install_github("ropenscilabs/jsonvalidate")
    install_github("ropenscilabs/datapkg")
