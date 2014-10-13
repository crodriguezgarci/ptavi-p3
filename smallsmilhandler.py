#!/usr/bin/python
#-*- coding: UTF-8 -*-
#Carlos Rodriguez Garcia PTAVI Practica 3 Karaoke.

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.elementos = []
        self.tags = ['root-layout', 'region', 'img', 'audio', 'textstream']
        self.atributos = {
            'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']
        }

    def startElement(self, name, attrs):
        diccionario = {}
        if name in self.tags:
            diccionario['etiqueta'] = name
            for atributo in self.atributos[name]:
                diccionario[atributo] = attrs.get(atributo, "")
            self.elementos.append(diccionario)

    def get_tags(self):
        return self.elementos

if __name__ == "__main__":

    parser = make_parser()
    SmallSMILHandler = SmallSMILHandler()
    parser.setContentHandler(SmallSMILHandler)
    parser.parse(open('karaoke.smil'))
    tags = SmallSMILHandler.get_tags()
    print tags
