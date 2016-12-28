# -*- coding: utf-8
# pylint: disable=line-too-long
"""Classes to collect information about citables.

   Anvi'o relies on many open-source software to do its job. The purpose of this
   module is to provide classes to help user figure out what they used and should
   cite besides anvi'o.
"""

import anvio
import anvio.tables as t
import anvio.terminal as terminal

from anvio.errors import ConfigError


__author__ = "A. Murat Eren"
__copyright__ = "Copyright 2016, The anvio Project"
__credits__ = []
__license__ = "GPL 3.0"
__version__ = anvio.__version__
__maintainer__ = "A. Murat Eren"
__email__ = "a.murat.eren@gmail.com"


run = terminal.Run()
progress = terminal.Progress()


class Citation:
    def __init__(self, citation_info_dict):
        missing_citation_keys = [k for k in citation_info_dict if k not in t.citations_table_structure[1:]]
        if missing_citation_keys:
            raise ConfigError, "The citation dict does not seem to be compatible with the citations table :/ It\
                                is missing these items: '%s'" % ', '.join(missing_citation_keys)

        if not isinstance(citation_info_dict['purpose'], list):
            raise ConfigError, "The 'purpose' item in the citation dict should be of type 'list'. It can list\
                                as many uses as necessary. What you have in there is %s." % (str(type(citation_info_dict['purpose'])))


class Citations:
    def __init__(self, anvio_db_path):
        self.anvio_db_path = anvio_db_path
        self.citations_dict = {}

    def add(citation):
        pass
