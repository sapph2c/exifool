# Exifool

**Exifool** is a metadata analysis tool written for CSEC-473 - Penetration Testing.

Currently supported file formats include:

- `pdf`

## Install

Exifool is available as a python package on PyPi:

```
pip install exifool
```

## Usage

CLI options:

```
exifool --help

Usage: exifool [OPTIONS]

  ___________      .__  _____             .__
  \_   _____/__  __|__|/ ____\____   ____ |  |
  |     __)_\  \/  /  \   __\/  _ \ /  _ \|  |
  |         \>    <|  ||  | (  <_> |  <_> )  |__
  /_______  /__/\_ \__||__|  \____/ \____/|____/
          \/      \/

  Written with ❤️ by sapph2c

  Metadata analysis tool written for CSEC-473

Options:
  --path TEXT  Path to the file to perform metadata analysis on.
  --help       Show this message and exit.

```

Retrieving metadata from a pdf:

```bash
exifool --path example.pdf
```

Sample output:

```bash
{
    '/Author': '',
    '/CreationDate': 'D:20250205020514Z',
    '/Creator': 'LaTeX with hyperref',
    '/Keywords': '',
    '/ModDate': 'D:20250205020514Z',
    '/PTEX.Fullbanner': 'This is pdfTeX, Version 3.141592653-2.6-1.40.25 (TeX Live 2023) kpathsea version 6.3.5',
    '/Producer': 'pdfTeX-1.40.25',
    '/Subject': '',
    '/Title': '',
    '/Trapped': '/False'
}
```
