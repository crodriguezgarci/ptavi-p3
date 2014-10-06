#!/usr/bin/python
#-*- coding: UTF-8 -*-
#Carlos Rodriguez Garcia PTAVI Practica 3 Karaoke

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.elementos = []
        self.tags = ['root-layout', 'region', 'img', 'audio', 'textstream']
        self.atributos = {
            'root-layout' : ['width', 'height','background-color'],
            'region' : ['id', 'top', 'bottom', 'left', 'right'],
            'img' : ['src', 'region','begin', 'dur'],
            'audio' : ['src', 'begin', 'dur'],
            'textstream' : ['src', 'region']
        }

    def startElement(self, name, attrs):
        if name == 'root-layout':
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.background = attrs.get('background-color', "")
            rootlayout = {}
            rootlayout['etiqueta'] = name
            rootlayout['height'] = self.width
            rootlayout['width'] = self.width
            rootlayout['background'] = self.background
            self.elementos.append(rootlayout)
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            region = {}
            region['etiqueta'] = name
            region['id'] = self.id
            region['top'] = self.top
            region['bottom'] = self.bottom
            region['left'] = self.left
            region['right'] = self.right
            self.elementos.append(region)
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.top = attrs.get('top', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            img = {}
            img['etiqueta'] = name
            img['src'] = self.src
            img['top'] = self.top
            img['begin'] = self.begin
            img['dur'] = self.dur
            self.elementos.append(img)
        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            audio = {}
            audio['etiqueta'] = name
            audio['src'] = self.src
            audio['begin'] = self.begin
            audio['dur'] = self.dur
            self.elementos.append(audio)
        elif name == 'textstream':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            textstream = {}
            textstream['etiqueta'] = name
            textstream['src'] = self.src
            textstream['region'] = self.begin
            self.elementos.append(textstream)    

    def get_tags(self):
        return self.elementos

if __name__ == "__main__":

    parser = make_parser()
    SmallSMILHandler = SmallSMILHandler()
    parser.setContentHandler(SmallSMILHandler)
    parser.parse(open('karaoke.smil'))
    tags = SmallSMILHandler.get_tags()
    print tags
