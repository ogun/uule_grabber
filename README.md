# uule_grabber
Generates UULE codes for Google Search

## Installation
You can install the package from PyPI by using pip:
```sh
$ pip install uule_grabber
```
## Usage
```python
>>> import uule_grabber
>>>
>>> city = "Lezigne,Pays de la Loire,France"
>>> uule_grabber.uule(city)
"w+CAIQICIfTGV6aWduZSxQYXlzIGRlIGxhIExvaXJlLEZyYW5jZQ"
```

## Latest Geo Targets
You can directly download the data from Google AdWords API:
https://developers.google.com/adwords/api/docs/appendix/geotargeting

## Credits
Ported to Python based on:
- Google UULE parameter: https://valentin.app/uule.html
