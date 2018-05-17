# -*- coding: utf-8 -*-

"""Main module."""
import re

PATTERNS = {
    'facebook': [
        'http(s)?://(www\.)?(facebook|fb)\.com/[A-z0-9_\-\.]+/?'
    ],
    'twitter': [
        'http(s)?://(.*\.)?twitter\.com\/[A-z0-9_]+/?'
    ],
    'linkedin': [
        'http(s)?://([\w]+\.)?linkedin\.com/in/(A-z0-9_-)\/?',
        'http(s)?://([\w]+\.)?linkedin\.com/pub/[A-z0-9_-]+(\/[A-z 0-9]+){3}/?'
    ],
}


class Extraction(object):
    """Extracted profiles."""

    _urls = None

    def __init__(self, urls):
        self._urls = urls

    def get_matches_per_platform(self):
        """
        Get lists of profiles keyed by platform name.
        :return: a dictionary with the platform as a key,
        and a list of the platform's profiles as values
        """
        return extract_matches_per_platform(self._urls)


def extract_matches_per_platform(urls):
    """
    Get lists of profiles keyed by platform name.
    :return: a dictionary with the platform as a key,
    and a list of the platform's profiles as values
    """
    matches = {}
    for url in urls:
        for plattform in PATTERNS:
            is_match = any(re.match(p, url) for p in PATTERNS[plattform])
            if is_match:
                if plattform not in matches:
                    matches[plattform] = []
                matches[plattform].append(url)

    return matches
