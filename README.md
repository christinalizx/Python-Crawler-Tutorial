# Python-Crawler-Tutorial

This is created to record my learning of web crawler using Python. Everything I've learned will be recorded here, I hope that at the end of my learning process, this can be a tutorial that will also be helpful to others such as beginners or seniors who want to review what they've studied before.

### Basic Information ###
Language used: Python

Libraries: requests

### Starters ###
1. Installing requests

```text
pip install requests
```
or
```text
python -m pip install requests
```
or to upgrade
```text
pip install --upgrade requests
```

2. GET or POST


|                    | GET      | POST |
|--------------------|------------------------------------------------------------|--------------------------------------------------------------------------------|
| BACK button/Reload | Harmless |Data will be re-submitted (the browser should alert the user that the data are about to be re-submitted)|
| Bookmarked         | Can be bookmarked |   Cannot be bookmarked   |
| Cached             | Can be cached | Not cached |
| Encoding type      |application/x-www-form-urlencoded| application/x-www-form-urlencoded or multipart/form-data. Use multipart encoding for binary data|
| History            |	Parameters remain in browser history |   	Parameters are not saved in browser history   |
| Restrictions on data length  | Yes, when sending data, the GET method adds the data to the URL; and the length of a URL is limited (maximum URL length is 2048 characters)         | No restriction  |
|  Restrictions on data type | Only ASCII characters allowed         |  No restriction  |
|  Security                  | GET is less secure compared to POST because data sent is part of the URL <br> Never use GET when sending passwords or other sensitive information!         |POST is a little safer than GET because the parameters are not stored in browser history or in web server logs     |
| Visibility                   |  Data is visible to everyone in the URL        | Data is not displayed in the URL     |
