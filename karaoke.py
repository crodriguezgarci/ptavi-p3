#!/usr/bin/python
#-*- coding: UTF-8 -*-
#Carlos Rodriguez Garcia PTAVI Practica 3 Karaoke


from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys

atributos = {
            'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region'] 
}



def imprimir(tags):
    for n in range(len(tags)):
        print tags[n]['etiqueta'],
       
        for atributo in atributos[tags[n]['etiqueta']]:
            print "\t" + atributo + '="' + tags[n][atributo]+ '"',
        print "\n"
    

if __name__ == "__main__":

    parser = make_parser()
    SmallSMILHandler = SmallSMILHandler()
    parser.setContentHandler(SmallSMILHandler)
    parser.parse(open(sys.argv[1], "r"))
    tags = SmallSMILHandler.get_tags()
    imprimir(tags)
