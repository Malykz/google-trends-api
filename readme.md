# Google Trends API

This project provides a simple interface to fetch trend data from Google Trends using Python.

## Instalation
```bash
pip install git+https://github.com/Malykz/google-trends-api
```

## Usage
```python
> import google_trends
> google_trends.fetch(geo="id")
```

## Output
```json
[
  {
    "title": "man utd vs wolves",
    "region": "ID",
    "category": 17,
    "searchVolume": 200000,
    "breakdown": [
      "man utd vs wolves",
      "mu vs wolves",
      "man united vs wolves",
      "tempat menonton manchester united f.c. vs wolves",
      "manchester united f.c. vs wolves",
      "manchester united vs wolves",
      "susunan pemain manchester united f.c. vs wolves",
      "wolves",
      "wolverhampton wanderers f.c.",
      "wolverhampton wanderers fc"
    ]
  },
  . . .
]
```

## Disclaimer
Whatever the error is, I'm too lazy to make a handling for it. And if there is an error, it will return None.
