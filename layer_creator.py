#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import subprocess

subprocess.run('clear')

name = input('What package are you making a layer?: ')


def command_list(commands):
    commands = [subprocess.run(command) for command in commands]

def create(layer):

    path = f'Desktop/LambdaLayers/{layer}'
    first_command = [
        ['mkdir', f'{path}'],
        ['mkdir', f'{path}/python'],
        ['pip3', 'install', '-t', f'{path}/python', f'{layer}'],
        ['zip', '-r', f'{path}/python.zip', f'{path}']
         ]

    command_list(first_command)

    print(f"\n'{layer}' was successfully created!!!\n")

    
create(name)