# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:56:22 2020

@author: Tomi
"""
import urllib.request
import urllib.parse
import urllib.error
import re
import ssl
import socket
import sys

def urllinks_extraction():
    '''urllib program to extract links in a webpage'''
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter url: ')
    html = urllib.request.urlopen(url, context=ctx).read()
    links = re.findall(b'href="(http[s]?://.*?)"', html)
    for link in links:
        print(link.decode())
#urllinks_extraction()

def common_words():
    '''using dictionary, gets key and value of most frequent words'''
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    counts = {}
    for line in fhand:
        line = line.decode().rstrip()
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    lst = []
    for key, value in counts.items():
        lst.append((value, key))
    print(counts)
    lst.sort(reverse=True)
    print(lst)
#common_words()

def urllib_image():
    '''extract image from webpage using urllib'''
    img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
    fhand = open('cover3.jpg', 'wb')
    size = 0
    while True:
        info = img.read(100000)
        if len(info) < 1:
            break
        size = size + len(info)
        fhand.write(info)
    fhand.close()
#urllib_image()

def exe1():
    '''create socket to read webpage and print content'''
    prompt = input('Enter url: ')
    try:
        split = prompt.split('/')
        print('Debug: split: ', split)
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((split[2], 80))
    except (TypeError, FileNotFoundError):
        print('This url does not exist')
        sys.exit()
    add = 'GET ' + prompt + ' HTTP/1.0\r\n\r\n'
    print('Debug: add: ', add)
    cmd = add.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
#exe1()

def exe2():
    '''count the number of characters but stop after 3000 characters'''
    prompt = input('Enter url: ')
    try:
        split = prompt.split('/') #we need the domain name
        # socket
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect
        mysock.connect((split[2], 80))
    except (TypeError, FileNotFoundError):
        print('This url does not exist or the file was not found')
        sys.exit()
    add = 'GET ' + prompt + ' HTTP/1.0\r\n\r\n'
    request = add.encode()
    # send
    mysock.send(request)
    # receive only 3000 characters
    data = mysock.recv(3000)
    count = 0
    fhand = data.decode()
    for line in fhand:
        char = len(line)
        count += char
        #print(line, count)
    print(count)
#exe2()

def exe3():
    '''modify exe2 to use urllib'''
    prompt = input('Enter url: ')
    try:
        fhand = urllib.request.urlopen(prompt)
    except (TypeError, FileNotFoundError):
        print('Url does not exist')
    #print(fhand.recv(3000))
    count = 0
    lst = []
    for line in fhand:
        words = line.decode()
        for word in words:
            for char in word:
                lst.append(char)
                count += 1
    print(count)
    print(lst[:3001])
#exe3()

def exe4():
    '''instead of extracting links, extract and count
    paragraph tags'''
    # ignore ssl certificate error
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter url: ')
    html = urllib.request.urlopen(url, context=ctx).read()
    links = re.findall(b'href="(http[s]?://.*?)"', html)
    # undone
