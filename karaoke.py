#!/usr/bin/python
#-*- coding: UTF-8 -*-
#Carlos Rodriguez Garcia PTAVI Practica 3 Karaoke.


from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import os

tagsrc = ['img', 'audio', 'textstream']


class KaraokeLocal(ContentHandler):
    def __init__(self, fichero):
        parser = make_parser()
        SmallSMILHandler = smallsmilhandler.SmallSMILHandler()
        self.atributos = SmallSMILHandler.atributos
        parser.setContentHandler(SmallSMILHandler)
        parser.parse(fichero)
        self.tags = SmallSMILHandler.get_tags()

    def __str__(self):
        exit = ""
        for tag in self.tags:
            exit += tag['etiqueta']
            for atributo in self.atributos[tag['etiqueta']]:
                if tag[atributo] != "":
                    exit += "\t" + atributo + '="' + tag[atributo] + '"'
            exit += "\n"
        return exit

    def do_local(self):
        for tag in self.tags:
            if tag['etiqueta'] in tagsrc:
                link = tag["src"]
                if link.startswith('http://'):
                    os.system("wget -q " + link)
                    link = link.split("/")[-1]
                    tag["src"] = link

if __name__ == "__main__":
    try:
        fichero = open(sys.argv[1], "r")
        karaokelocal = KaraokeLocal(fichero)
        print karaokelocal
        karaokelocal.do_local()
        print karaokelocal
    except IndexError:
        print "Usage: python karaoke.py file.smil."
