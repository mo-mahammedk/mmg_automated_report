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


# This collects the necessary graphs for the MMG report
##def image_collect(img_dir, startDate, epochFinish, configFile):
def image_collect(config,out_file_xcs,out_file_collab_nodes,out_file_project_size):
  ssl._create_default_https_context = ssl._create_unverified_context

  print("***Image Collection Process Started***")

  epochStart='now-90d'
  epochFinish='now'

  # All XCS over last 90 days
  get_url_xcs= config["grafana"]["url"]+"/" \
            + config["all_monsoon_last_90d"]["id"] + "/" \
            + config["all_monsoon_last_90d"]["name"] \
            + "?orgId=" + config["grafana"]["orgid"] \
            + "&from=" + epochStart + "&to=" + epochFinish + "&theme=light&panelId=" \
            + config["all_monsoon_last_90d"]["panel_id"] \
            + "&width="  + config["grafana"]["width"] + "&height=" + config["grafana"]["height"] \
            + "&tz=" + config["grafana"]["tz"]

  print("url="+get_url_xcs)
  print("file="+out_file_xcs)

  urllib.request.urlretrieve(get_url_xcs, out_file_xcs)
  
  # Collaboration nodes last 90 days
  get_url_collab_nodes = config["grafana"]["url"]+"/" \
            + config["collab_nodes_last_90d"]["id"] + "/" \
            + config["collab_nodes_last_90d"]["name"] \
            + "?orgId=" + config["grafana"]["orgid"] \
            + "&from=" + epochStart + "&to=" + epochFinish + "&theme=light&panelId=" \
            + config["collab_nodes_last_90d"]["panel_id"] \
            + "&width="  + config["grafana"]["width"] + "&height=" + config["grafana"]["height"] \
            + "&tz=" + config["grafana"]["tz"]

  print("url="+get_url_collab_nodes)
  print("file="+out_file_collab_nodes)

  urllib.request.urlretrieve(get_url_collab_nodes, out_file_collab_nodes)
  
  #Project size last month
  get_url_project_size = config["grafana"]["url"]+"/" \
            + config["project_size_last_month"]["id"] + "/" \
            + config["project_size_last_month"]["name"] \
            + "?orgId=" + config["grafana"]["orgid"] \
            + "&from=" + epochStart + "&to=" + epochFinish + "&theme=light&panelId=" \
            + config["project_size_last_month"]["panel_id"] \
            + "&width="  + config["grafana"]["width"] + "&height=" + config["grafana"]["height"] \
            + "&tz=" + config["grafana"]["tz"]

  print("url="+get_url_project_size)
  print("file="+out_file_project_size)

  urllib.request.urlretrieve(get_url_project_size, out_file_project_size)


  print("***Image Collection Process Finished***")
  return()

def main():

  print("Reading config...")

  configFile="config.ini"
  config = configparser.ConfigParser(interpolation=None)
  config.read(configFile)

  # set output file

  out_file_xcs='./mmg_all_monsoon_last_90_days.png' 
  out_file_collab_nodes='./collaboration_nodes_last_90_days.png' 
  out_file_project_size='./project_size_last_month.png'

  # get the image

  image_collect(config,out_file_xcs,out_file_collab_nodes,out_file_project_size)

  print("Goodbye")
  exit()

	
if __name__ == '__main__':
  main()
