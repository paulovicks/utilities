#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Script Name: tlds.py
# Description: Gather a current list of Top-Level Domains (TLDs) from ICANN.

# Author: Jason Paulovicks
# Email: jason@paulovicks.com
# Date Created: 2024-03-12
# Version: 1.0.0
# License:
tlds.py - Pull TLD data from ICANN data set.
    Copyright (C) 2024  Jason Paulovicks

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import argparse
import logging
import urllib.request
import urllib.error


def read_data_from_url(url: str, strip_pattern: list[str] = None, lowercase=False) -> list[str] | None:
    """
    Reads data from ICANN provided text file, includes handles for punycode characters.
    :param lowercase: Coverts output lines to lowercase. (Default: False)
    :param url: Uses the defined URL to parse data from.
    :param strip_pattern: A string pattern match to filter the line (optional)
    :return: list of lines from the text file or None if an error occurs
    """

    logger = logging.getLogger(__name__)

    try:
        with urllib.request.urlopen(url) as response:
            lines = response.readlines()
            if strip_pattern:
                # Strip lines based on patterns
                text = [line.decode("utf-8").strip()
                        for line in lines
                        if not any(pattern in line.decode("utf-8")
                                   for pattern in strip_pattern)]
            else:
                text = [line.decode("utf-8").strip() for line in lines]
            # Apply lowercase conversion if the flag is set
            if lowercase:
                text = [line.lower() for line in text]
            return text
    except (urllib.error.URLError, ConnectionError, TimeoutError) as e:
        logger.error(f"Error fetching data from URL: {url}", exc_info=True)
        return None


def main():
    parser = argparse.ArgumentParser(description='Reads TLDs from a ICANN')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug logging')
    parser.add_argument('-s', '--strip', nargs='+', help='Patterns to remove from lines (can be used multiple times)',
                        metavar="")
    parser.add_argument('-l', '--lowercase', action='store_true', help='Convert data to lowercase')
    args = parser.parse_args()

    # Configure logging based on debug flag
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    url = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'

    # Handle strip patterns (if provided)
    strip_patterns = args.strip if args.strip else None

    data = read_data_from_url(url, strip_patterns, lowercase=args.lowercase)

    if data:
        print(data)
    else:
        print("Encountered an error while reading the file.")


if __name__ == '__main__':
    main()
