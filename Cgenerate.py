# -*- coding: utf-8 -*-
from numpy import *
from os import listdir,mkdir,path
import re
from nltk.corpus import stopwords
import nltk
import operator

mainpath = "/home/bean/Desktop/20_newsgroups"
Doc_term = []

def createFiles():
	srcFilesList = listdir(mainpath)
	print srcFilesList
	for i in range(len(srcFilesList)):
		print i
		dataFileDir = mainpath+"/"+srcFilesList[i] #specific to each topic
		dataFilesList = listdir(dataFileDir)  # specific to each file
		targetDir = "/home/bean/Desktop/ProcessedDir"+"/"+srcFilesList[i]
		if path.exists(targetDir) == False:
			mkdir(targetDir)
		else:
			print '%s exists' % targetDir
		for j in range(len(dataFilesList)):
			print '%s %s' % (srcFilesList[i], dataFilesList[j])
			createProcessFile(srcFilesList[i],dataFilesList[j])

def createProcessFile(srcFilesName,dataFilesName):
	srcFile = mainpath+"/"+srcFilesName+"/"+dataFilesName
	targetFile = "/home/bean/Desktop/ProcessedDir"+"/"+srcFilesName+"/"+dataFilesName
	fw = open(targetFile,'w')
	datailst = open(srcFile).readlines()
	for line in datailst:
		resLine = lineProcess(line)
		for word in resLine:
			if word == '':
				continue
			fw.write('%s\n' % word)
	fw.close()

def lineProcess(line):
	stopwords = nltk.corpus.stopwords.words('english')
	# porter = nltk.PorterStemmer()
	lst = nltk.LancasterStemmer()
	splitter = re.compile('[^a-zA-Z]')
	words = [lst.stem(word.lower()) for word in splitter.split(line) if word.lower() not in stopwords]
	return words





		

