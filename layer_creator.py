#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import subprocess

subprocess.run('clear')

layer = input('What package are you making a layer?: ')


def execute(commands):
    commands = [subprocess.run(command) for command in commands]

def create(package):

    path = f'' # The path where you would like to store the package
    cmd = [
        ['mkdir', f'{path}'],
        ['mkdir', f'{path}/python'],
        ['pip3', 'install', '-t', f'{path}/python', f'{package}'],
        ['zip', '-r', f'{path}/python.zip', f'{path}']
         ]

    execute(cmd)

    print(f"\n'{package}' was successfully created!!!\n")

    
create(layer)