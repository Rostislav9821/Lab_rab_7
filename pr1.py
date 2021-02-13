#! / usr / bin / env python3
# - * - кодировка: utf-8 - * -

import  sys

если  __name__  ==  '__main__' :
    A  =  кортеж ( карта ( int , input (). Split ()))
    если  len ( A ) ! =  10 :
        print ( 'Неверный размер кортежа' , file = sys . stderr )
        выход ( 1 )

    s  =  сумма ( a  для  a  в  A,  если  abs ( a ) <  5 )
    печать ( и )