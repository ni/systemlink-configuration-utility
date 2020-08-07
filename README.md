# SystemLink Configuration Utility

The *systemlink-configuration-utility* package contains a command line utility for IT professionals to use
when managing the configuration of an NI [SystemLink Server](https://ni.com/systemlink) installation.

## Requirements

### SystemLink
- This utility assumes SystemLink Server version 2020R3 or later.
- This utility assume a single-box SystemLink installation.
- This utility is designed to run on the same machine as the SystemLink Server installation. It does not support remote migration.

### Python
- This utility requires >=Python3 to run. Installers can be found at [python.org](https://www.python.org/downloads/)
- The documentation in this repo assumes Python has been added to your PATH environment variable.
- Depending on the setup of your environment you may invoke python with `python`, `python3`, or `py`.

## Usage

See the [docs](docs) for documentation on usage of the utility.

## Contributing

See the [contributing guidelines](CONTRIBUTING.md) for how to set up and submit
contributions to the *systemlink-configuration-utility*.
