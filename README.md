# GitHub Download Stats

[![Build Status](https://travis-ci.org/kefir500/ghstats.svg)](https://travis-ci.org/kefir500/ghstats)
[![GitHub license](https://img.shields.io/github/license/kefir500/ghstats.svg)](https://raw.githubusercontent.com/kefir500/ghstats/master/LICENSE)

## Description

- Python script to obtain GitHub Release download count and other statistics.
- Can be used as a standalone script as well as a Python module.
- Supports both Python 2 and 3 out of the box.
- [Download](https://github.com/kefir500/ghstats/releases/latest) or manually save `ghstats.py` from the repository.

## Support

- Python 2 (2.6 or higher)
- Python 3

## Usage

```
ghstats.py [user] [repo] [tag] [options]
ghstats.py [user/repo] [tag] [options]
```

###### Arguments:

       | Description
------ | -----------
`user` | Repository owner. If not present, user will be prompted for input.
`repo` | Repository title. If not present, user will be prompted for input.
`tag`  | Release tag name. If not present, prints the total number of downloads.

###### Options:

                 | Description
---------------- | -----------
`-d`, `--detail` | Print detailed statistics for release(s).
`-q`, `--quiet`  | Print only resulting numbers and errors. Overrides `-d` option.
`-l`, `--latest` | Get stats for the latest release. `Tag` argument will be ignored.
`-h`, `--help`   | Show help on script usage.

###### Environment Variables:

               | Description
-------------- | -----------
`GITHUB_TOKEN` | GitHub OAuth token. Use to increase API request limit. https://github.com/settings/tokens

## Examples

Examples for [atom/atom](https://github.com/atom/atom) repository:

```Shell
python ghstats.py atom atom            # Fetch download count for all releases.
python ghstats.py atom/atom            # Fetch download count for all releases (alt. syntax).
python ghstats.py atom atom -q         # Quiet mode (print only numerical result).
python ghstats.py atom atom -d         # Detailed description for every release.
python ghstats.py atom atom -l         # Fetch download count for the latest release.
python ghstats.py atom atom -l -d      # Detailed description for the latest release.
python ghstats.py atom atom -l -q      # Quiet mode for the latest release.
python ghstats.py atom atom v1.0.0     # Fetch download count for "v1.0.0" release.
python ghstats.py atom atom v1.0.0 -d  # Detailed description for "v1.0.0" release.
python ghstats.py atom atom v1.0.0 -q  # Quiet mode for "v1.0.0" release.
python ghstats.py                      # Get input for username and repository from user.
python ghstats.py -h                   # Print help.
```

## License

###### MIT License

You are free to use, modify, distribute (including commercial purposes) as long as you credit the original author and include the license text.

License text: [MIT License](https://raw.githubusercontent.com/kefir500/ghstats/master/LICENSE)
