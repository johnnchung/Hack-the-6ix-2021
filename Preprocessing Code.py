import numpy as np 
import pandas as pd 
import seaborn as sns
import joblib 
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import whois


def NosOfSubdomain(string):
    split = string.split('.')
    if('/' not in string):
        return len(split) - 1
    else:
        count = 0
        for val in split:
            if('/' in val):
                break
            else:
                count += 1

        return count

def activeDuration(string):
    try:
        w = whois.whois(string)
        creation_date = w.creation_date
        creation_year = creation_date.year
        current_year = 2021
        
        difference = abs(current_year - creation_year)
        days = difference * 365 - 365
    except:
        days = 0
    
    return days

def valid(string):
    try:
        w = whois.whois(string)
        return 1
    except:
        return 0

def urlLen(string):
    return len(string)

def isat(string):
    if('@' in string):
        return 1
    else:
        return 0

def isredirect(string):
    if('--' in string):
        return 1
    else:
        return 0

def havedash(string):
    if('-' in string):
        return 1
    else:
        return 0

def domainLength(string):
    count = 0
    for val in string:
        if(val == '/'):
            return count
        else:
            count += 1
    return count