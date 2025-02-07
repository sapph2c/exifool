# Usage

Exifool provides a simple command-line interface for metadata analysis. Below is the basic usage:

```bash

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

Example:

To retrieve metadata from a PDF file named example.pdf:

```bash
exifool --path example.pdf
```
This command will display the extracted metadata in the terminal.

For more detailed information and advanced usage, refer to the Exifool GitHub repository.
