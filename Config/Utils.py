# Copyright (c) SilentX by aryodw
# Licensed under the MIT License.
# See LICENSE file in the project root for full license text.

import sys
try:
    import os, datetime, subprocess, ctypes, time, colorama, random, socket, socks, requests, threading, argparse, json
    import keyboard, concurrent.futures, urllib, urllib.parse, urllib3, ipaddress, re, errno, select, collections, warnings
    import hashlib, OpenSSL, struct, ipwhois, dns.resolver, base64, piexif, exifread, PIL.Image, mutagen, stat, ssl
    import bs4, webbrowser, shutil, tempfile, zipfile, tarfile, sqlite3, pathlib, wave, contextlib, fitz, lxml, lxml.html
    import phonenumbers, phonenumbers.geocoder, phonenumbers.carrier, phonenumbers.timezone, whois, smtplib, string, logging
    import instaloader, math, zlib, importlib.util
except Exception as e:
    print(f"\nModules of the python library required for SilentX are not installed, make sure you have correctly installed python and have launched the \"setup.py\" file which will install all the necessary modules.")
    sys.exit(f"Error: {e}")

try:    os_name     = "Windows" if sys.platform.startswith("win") else "Linux" if sys.platform.startswith("linux") else "Unknown"
except: os_name     = "Unknown"
try:    os_username = os.getlogin()
except: os_username = "username"

path_folder_tool                        = os.path.abspath(__file__).split(os.sep + "Config" + os.sep)[0]
path_folder_data                        = os.path.join(path_folder_tool,   "Data")
path_folder_plugins                     = os.path.join(path_folder_tool,   "Plugins")
path_folder_ouput                       = os.path.join(path_folder_tool,   "Ouput")
path_folder_ouput_file_metadata_scanner = os.path.join(path_folder_ou
