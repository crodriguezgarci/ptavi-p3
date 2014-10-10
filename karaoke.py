#!/usr/bin/python
#-*- coding: UTF-8 -*-
#Carlos Rodriguez Garcia PTAVI Practica 3 Karaoke


from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import string
import os

tagsrc = ['img','audio','textstream']

class SmallSMILHandler(ContentHandler):

    def __init__(self, fichero ):

        pass






def imprimir(tags, atributos):

    for tag in tags:
        print tag['etiqueta'],
        for atributo in atributos[tag['etiqueta']]:
            if tag[atributo] != "":
                print "\t" + atributo + '="' + tag[atributo]+ '"',
        print "\n"

def do_local(tags):
    for tag in tags:
        if tag['etiqueta'] in tagsrc:
            link = tag["src"]
            if link.startswith('http://'):
                os.system("wget -q " + link)
                link = link.split("/")[-1]
                tag["src"] = link


if __name__ == "__main__":

    parser = make_parser()
    SmallSMILHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(SmallSMILHandler)
    parser.parse(open(sys.argv[1], "r"))
    tags = SmallSMILHandler.get_tags()
    imprimir(tags, SmallSMILHandler.atributos)
    do_local(tags)
    imprimir(tags, SmallSMILHandler.atributos)
