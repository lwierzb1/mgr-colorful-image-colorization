#!/usr/bin/env python
import configparser

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


class ConfigReader:
    """
    A class used to read CNN attributes from ini file.

    Attributes
    ----------
    __config_parser
        instance of ini reader.

    Methods
    -------
    get_property(name)
        Returns value of property with given name in 'CNN' section
    """

    def __init__(self):
        self.__INI_PATH = 'cnn_config.ini'
        self.__CNN_SECTION = 'CNN'
        self.__config_parser = configparser.ConfigParser()
        self.__config_parser.read(self.__INI_PATH)

    def get_string_property(self, name):
        return self.__config_parser[self.__CNN_SECTION][name]

    def get_int_property(self, name):
        return self.__config_parser.getint(self.__CNN_SECTION, name)
