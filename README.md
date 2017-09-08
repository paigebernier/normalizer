# normalizer

The normalizer is a python script that can read in a CSV from stdin and normalize the data emitting a CSV on stdout.

The data expected and transformation that will occur is outlined below in the Transformation Table. Read on for installation and execution instructions.

### Installation & Requirements
* Python 2.7
* Mac OS 10.12

1. Create a virtual environment by opening Terminal and running (this will help isolate the libraries we install) 

   ``` virtualenv env``` and enter it via ``` source env/bin/activate```

   * If virtualenv is not installed run ``` pip install virtualenv```

2. Install the dependencies found in requirements.txt 

   ``` pip install requirements.txt```

---
### Running the script

Open Terminal and run the following command substituting your csv in for _<csv.csv>_

``` cat <csv.csv> | python normalizer.py```

If you'd like a preview of the script run the above command using the example csv file named *sample-with-broken-utf8.csv*

When you're done running the script remember to exit the virtual environment by running

``` deactivate ```

---

### Transformation Table

| Header | Raw Data | Transformation | Formatted Data |
| --- | --- | --- | --- |
| _Timestamp_ | 4/1/11 11:00:00 AM | ISO-8601 Datetime US/Eastern | 2011-04-01T11:00:00-04:00
| _Address_ | 123 4th St, Anywhere, AA | unicode validation | 123 4th St, Anywhere, AA
| _ZIP_ | 121 | zero-padding enforcing 5 digits | 00121
| _FullName_ | Mary | uppercasing | MARY
| _FooDuration_ | 1:23:32.123 | floating point seconds | 5012.123
| _BarDuration_ | 1:32:33.123 | floating point seconds | 5553.123
| _TotalDuration_ | zzsasdfa | replace with sum of Foo and Bar Duration | 10565.246
| _Notes_ | I like Emoji! 🍏🍎😍 | unicode validation | I like Emoji! 🍏🍎😍


