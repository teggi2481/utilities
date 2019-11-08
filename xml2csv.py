# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:37:20 2019

@author: halad
"""
from xml.etree import ElementTree
import os
import csv

# Change the working directory
os.chdir("C:\\Users\\halad.CORPDOM\\OneDrive - Micro Focus\\Ongoing Work\\ML\\Materials\\DataScience Documents\\Python Programming")

# Read the file
tree = ElementTree.parse('sitescope01.xml')

# Create a file for writing
sitescope_data = open('sitescope01.csv', 'w',newline='',encoding='utf-8')
csvwriter = csv.writer(sitescope_data)

col_names = ['id','title','description','state','solution','severity','priority','category','subCategory','timeCreated','application','object']
csvwriter.writerow(col_names)

root = tree.getroot()

for eventData in root.findall('eventData'):
    event_data = []
    event = eventData.find('event')
    
    event_id = event.find('id')
    if event_id != None :
        event_id = event_id.text
    event_data.append(event_id)
    
    event_title = event.find('title')
    if event_title != None :
        event_title = event_title.text
    event_data.append(event_title)
    
    event_description = event.find('description')
    if event_description != None :
        event_description = event_description.text
    event_data.append(event_description)
    
    event_state = event.find('state')
    if event_state != None :
        event_state = event_state.text
    event_data.append(event_state)
    
    event_solution = event.find('solution')
    if event_solution != None :
        event_solution = event_solution.text
    event_data.append(event_solution)
    
    event_severity = event.find('severity')
    if event_severity != None :
        event_severity = event_severity.text
    event_data.append(event_severity)
    
    event_priority = event.find('priority')
    if event_priority != None :
        event_priority = event_priority.text
    event_data.append(event_priority)
    
    event_category = event.find('category')
    if event_category != None :
        event_category = event_category.text
    event_data.append(event_category)
    
    event_subCategory = event.find('subCategory')
    if event_subCategory != None :
        event_subCategory = event_subCategory.text
    event_data.append(event_subCategory)
    
    event_timeCreated = event.find('timeCreated')
    if event_timeCreated != None :
        event_timeCreated = event_timeCreated.text
    event_data.append(event_timeCreated)
    
    event_application = event.find('application')
    if event_application != None :
        event_application = event_application.text
    event_data.append(event_application)
    
    event_object = event.find('object')
    if event_object != None :
        event_object = event_object.text
    event_data.append(event_object)
    
    print(event_id)
    csvwriter.writerow(event_data)
    
sitescope_data.close()
