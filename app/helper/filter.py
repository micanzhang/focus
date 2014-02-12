__author__ = 'micanzhang'
import time

def strftime(seconds, format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format, time.gmtime(seconds))