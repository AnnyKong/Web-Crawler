# Web-Crawler
A multiprocess web crawler for crawling historical photo records, and store outputs in `json` format

### HOW TO RUN
```
python3 web3.py
```
Notes: python 3 required.

### How to read output files?
```
python3 read.py dicts3/<json_filename>
```

### Some useful commands to check # records in an output file:
```
cd dicts3/
python3 ../read.py $(ls -tr | grep "dict*" | tail -1)
```
Notes:
- `ls -tr | grep "dict*" | tail -1`: gives the most recent output file.
- `ls -tr`: list all files in reverse order of time (earlier->latest)
- `grep "dict*"`: find all files starts with the pattern "dict"
- `tail -1`: get the last one in the list

### Overview of output files
- Where can I find my output files?

  output files will be located under your `$project/dicts3` directory

- What is the format of my output files?

  Mapping from a dictionary to another dictionary:
  ```
    dict -> dict

  dict {
          index : {
            Webpage : 
            Creator : 
            ...
            Subjects: [
              xxx, 
              xxx,
              ...
            ]
          },
          ...
        }
  ```

- Example:
  ```
  {
    "14400": {
      "Webpage": "http://ucr.emuseum.com/view/objects/asitem/3631/2",
      "Creator": "Not Known",
      "Publisher": "Underwood & Underwood",
      "Title": "(37) Honorable Heber M. Wells, Governor of Utah, in his office, Salt Lake City",
      "Date": "1904",
      "Medium": "Gelatin silver contact print",
      "Credit Line": "Keystone-Mast Collection, UCR/California Museum of Photography, University of California, Riverside",
      "Accession Number": "1996.0009.X75160",
      "Inscriptions": "[No inscription]",
      "Subjects": [
        "Wells, Heber M. (Heber Manning), 1859-1938",
        "Portraits",
        "Offices",
        "Governors",
        "Paperwork"
      ]
    },
    "26348": {
      "Webpage": "http://ucr.emuseum.com/view/objects/asitem/3631/0",
      "Creator": "Not Known",
      "Publisher": "Keystone View Company",
      "Title": "\"End of the Trail\"",
      "Date": "1915",
      "Medium": "Gelatin silver contact print",
      "Credit Line": "Keystone-Mast Collection, UCR/California Museum of Photography, University of California, Riverside",
      "Accession Number": "1996.0009.17827",
      "Inscriptions": "Statue \"End of the Trail\" at the Entrance to the Court of the Palms. California [Panama-Pacific Exposition]",
      "Description": "Person standing next to statue",
      "Place Depicted": "North and Central America, United States, California, San Francisco",
      "Subjects": [
        "Exhibition buildings",
        "Sculpture",
        "Panama-Pacific International Exposition (1915 : San Francisco, Calif.)"
      ]
    },
    "86636": {
      "Webpage": "http://ucr.emuseum.com/view/objects/asitem/3631/1",
      "Creator": "Not Known",
      "Publisher": "Keystone View Company",
      "Title": "\"So you think that one's good? Wait 'till you see this one!\" Henry Ford and Anton Lang in Oberammergau.",
      "Date": "[Date not indicated]",
      "Medium": "Stereo card",
      "Credit Line": "Keystone-Mast Collection, UCR/California Museum of Photography, University of California, Riverside",
      "Accession Number": "1996.0009.28024",
      "Description": "Men looking at stereo cards",
      "Place Depicted": "Europe, Germany, Bavaria, Oberammergau",
      "Subjects": [
        "Business people",
        "Stereoscopes",
        "Lang, Anton, 1875-1938",
        "Ford, Henry, 1863-1947",
        "Actors"
      ]
    }
  }
  ```

### Modules needed
- For getting the webpage:
  - requests_html
  
- For pattern match:
  - re

- For multiprocessing:
  - multiprocessing
  Notes: 
  How to obtain the number of CPUs/cores in Linux from the command line?
  (linux)
  ```
  cat /proc/cpuinfo | awk '/^processor/{print $3}' | wc -l
  ```
  
  - functools
  
- For output format:
  - pandas (for `.tsv`)
  - json (for `.json`) preferred
