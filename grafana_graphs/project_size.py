#!/usr/bin/env python3
"""
A script to collect images from a url.
This will then save them locally as a .png
"""

# Importing modules
import urllib.request

# Ignore ssl
import ssl

import datetime 
# Using relativedelta - can deal with leap years
from dateutil.relativedelta import relativedelta

import configparser


# This collects the necessary graphs for the SUWG report
##def image_collect(img_dir, startDate, epochFinish, configFile):
def image_collect(config,out_file):
  ssl._create_default_https_context = ssl._create_unverified_context

  print("***Image Collection Process Started***")

  epochStart='1690844400000'
  epochFinish='1693522799000'

  # all xcs over last 90 days

  get_url = config["grafana"]["url"]+"/" \
            + config["project_size_last_month"]["id"] + "/" \
            + config["project_size_last_month"]["name"] \
            + "?orgId=" + config["grafana"]["orgid"] \
            + "&from=" + epochStart + "&to=" + epochFinish + "&theme=light&panelId=" \
            + config["project_size_last_month"]["panel_id"] \
            + "&width="  + config["grafana"]["width"] + "&height=" + config["grafana"]["height"] \
            + "&tz=" + config["grafana"]["tz"]

  print("url="+get_url)
  print("file="+out_file)

  urllib.request.urlretrieve(get_url, out_file)

  print("***Image Collection Process Finished***")
  return()

def main():

  print("Reading config...")

  configFile="config.ini"
  config = configparser.ConfigParser(interpolation=None)
  config.read(configFile)

  # set output file

  out_file='./project_size_last_month.png' 

  # get the image

  image_collect(config,out_file)

  print("Goodbye")
  exit()

	
if __name__ == '__main__':
  main()