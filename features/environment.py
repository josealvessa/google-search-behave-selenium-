# -*- coding: utf-8 -*-
__author__ = 'Augusta Marques'

from selenium import webdriver
import os

def before_feature(context, feature):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()

def after_feature(context, feature):
    context.driver.close()
