import random
from urllib import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/word.txt"
WORDS = []
PHRASES = {
    "class %%%(%%%) :":
    u"Создается класс с именем %%%, наследующим %%%.",
    "class %%%(object):\n\tdef __init_(self, ***)":
    u"класс комбинирует __init_ с параметрами self, *** .",
    "class %%%(object):\n\tdef ***(self, @@@) ":
    u"Класс %%% комбинирует функцию с именем *** с параметрами self, @@@ .",
    "*** = @@@() ":
    u"Создается *** как экземпляр класса %%%.",
    "***.***(self, @@@) ":
    u"Из *** получается функция ***, а затем вызывается с параметрами self,"
                                                                    "@@@.",
    "***.*** = '***'":
    u"Из *** получается атрибут ***, а затем устанавливается равным
    '* * *'."

}
