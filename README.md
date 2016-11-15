# pilot-open-archaeology
This is a repository for piloting a packaging approach to archaeology data

**The Cultural Evolution of Neolithic Europe. EUROEVOL Dataset**

http://openarchaeologydata.metajnl.com/articles/10.5334/joad.42/ (data: http://discovery.ucl.ac.uk/1469811/)

Characteristics of this dataset:

* It is small-ish 
* Consists of several tables that relate to each other which can be modeled in a Data Package
* Has an existing SQL dump for comparison on e.g. ease-of-use, performance, import into different backends
* Has existing metadata about each table prepared already

Start the script by running `python3 scripts/euroevol.py` in a virtual envinronment with the appropriate packages.