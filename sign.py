#
'''
This code is covered from the the login website's js code, to calculate
the sign code in the headers. Which is motherfxxker.

Hurray for js2py library! You could find it on:
https://github.com/PiotrDabkowski/Js2Py

2022 SuperBart, released under SuperBart Public Domain Software License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

Two additional terms:
1. As long as you use this software, you acknowledge that the author of
the software strongly against improper competition and labour, for
example, 996 working schedule. And the author dislike anything which are
bureaucratization, such as meaningless meeting and courses.
2. The additional terms have no mandatory in either laws, or other fields.
You don't need to agree with the additional terms in order to use this
software. And you may delete the additional terms when using this software,
as long as you obey the non-additional terms above.
'''

__all__ = ['sign']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['a'])
@Js
def getHim(t, this, arguments, var=var):
    var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'a', 'l', 'u', 'd', 'f', 'r', 'h', 'p', 'c', 'o', 'e', 't', 's', 'n'])
    @Js
    def PyJs_anonymous_0_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'R', 'A', 'P', 'e', 'B', 'N', 'C', 't', 'x', 'D', 'v', 'V', 's', 'I', 'E', 'y', 'b', 'o', 'O', 'a', 'n', 'm', 'w', 'T', 'M', 'g', 'S'])
        var.put('b', var.get('Array')())
        var.put('y', Js(7.0))
        var.put('w', Js(12.0))
        var.put('S', Js(17.0))
        var.put('T', Js(22.0))
        var.put('E', Js(5.0))
        var.put('D', Js(9.0))
        var.put('x', Js(14.0))
        var.put('B', Js(20.0))
        var.put('O', Js(4.0))
        var.put('R', Js(11.0))
        var.put('A', Js(16.0))
        var.put('V', Js(23.0))
        var.put('I', Js(6.0))
        var.put('N', Js(10.0))
        var.put('M', Js(15.0))
        var.put('P', Js(21.0))
        #for JS loop
        PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('t', var.get('d')(var.get('t'))),var.put('b', var.get('l')(var.get('t')))),var.put('a', Js(1732584193.0))),var.put('g', Js(4023233417.0))),var.put('v', Js(2562383102.0))),var.put('m', Js(271733878.0))),var.put('e', Js(0.0)))
        while (var.get('e')<var.get('b').get('length')):
            try:
                def PyJs_LONG_1_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('n', var.get('a')),var.put('r', var.get('g'))),var.put('o', var.get('v'))),var.put('s', var.get('m'))),var.put('a', var.get('h')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(0.0))), var.get('y'), Js(3614090360.0)))),var.put('m', var.get('h')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(1.0))), var.get('w'), Js(3905402710.0)))),var.put('v', var.get('h')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(2.0))), var.get('S'), Js(606105819.0)))),var.put('g', var.get('h')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(3.0))), var.get('T'), Js(3250441966.0)))),var.put('a', var.get('h')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(4.0))), var.get('y'), Js(4118548399.0)))),var.put('m', var.get('h')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(5.0))), var.get('w'), Js(1200080426.0)))),var.put('v', var.get('h')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(6.0))), var.get('S'), Js(2821735955.0)))),var.put('g', var.get('h')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(7.0))), var.get('T'), Js(4249261313.0)))),var.put('a', var.get('h')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(8.0))), var.get('y'), Js(1770035416.0)))),var.put('m', var.get('h')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(9.0))), var.get('w'), Js(2336552879.0)))),var.put('v', var.get('h')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(10.0))), var.get('S'), Js(4294925233.0)))),var.put('g', var.get('h')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(11.0))), var.get('T'), Js(2304563134.0)))),var.put('a', var.get('h')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(12.0))), var.get('y'), Js(1804603682.0)))),var.put('m', var.get('h')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(13.0))), var.get('w'), Js(4254626195.0)))),var.put('v', var.get('h')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(14.0))), var.get('S'), Js(2792965006.0)))),var.put('g', var.get('h')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(15.0))), var.get('T'), Js(1236535329.0)))),var.put('a', var.get('u')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(1.0))), var.get('E'), Js(4129170786.0)))),var.put('m', var.get('u')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(6.0))), var.get('D'), Js(3225465664.0)))),var.put('v', var.get('u')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(11.0))), var.get('x'), Js(643717713.0)))),var.put('g', var.get('u')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(0.0))), var.get('B'), Js(3921069994.0)))),var.put('a', var.get('u')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(5.0))), var.get('E'), Js(3593408605.0)))),var.put('m', var.get('u')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(10.0))), var.get('D'), Js(38016083.0)))),var.put('v', var.get('u')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(15.0))), var.get('x'), Js(3634488961.0)))),var.put('g', var.get('u')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(4.0))), var.get('B'), Js(3889429448.0)))),var.put('a', var.get('u')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(9.0))), var.get('E'), Js(568446438.0)))),var.put('m', var.get('u')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(14.0))), var.get('D'), Js(3275163606.0)))),var.put('v', var.get('u')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(3.0))), var.get('x'), Js(4107603335.0)))),var.put('g', var.get('u')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(8.0))), var.get('B'), Js(1163531501.0)))),var.put('a', var.get('u')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(13.0))), var.get('E'), Js(2850285829.0)))),var.put('m', var.get('u')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(2.0))), var.get('D'), Js(4243563512.0)))),var.put('v', var.get('u')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(7.0))), var.get('x'), Js(1735328473.0)))),var.put('g', var.get('u')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(12.0))), var.get('B'), Js(2368359562.0)))),var.put('a', var.get('c')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(5.0))), var.get('O'), Js(4294588738.0)))),var.put('m', var.get('c')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(8.0))), var.get('R'), Js(2272392833.0)))),var.put('v', var.get('c')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(11.0))), var.get('A'), Js(1839030562.0)))),var.put('g', var.get('c')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(14.0))), var.get('V'), Js(4259657740.0)))),var.put('a', var.get('c')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(1.0))), var.get('O'), Js(2763975236.0)))),var.put('m', var.get('c')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(4.0))), var.get('R'), Js(1272893353.0)))),var.put('v', var.get('c')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(7.0))), var.get('A'), Js(4139469664.0)))),var.put('g', var.get('c')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(10.0))), var.get('V'), Js(3200236656.0)))),var.put('a', var.get('c')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(13.0))), var.get('O'), Js(681279174.0)))),var.put('m', var.get('c')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(0.0))), var.get('R'), Js(3936430074.0)))),var.put('v', var.get('c')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(3.0))), var.get('A'), Js(3572445317.0)))),var.put('g', var.get('c')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(6.0))), var.get('V'), Js(76029189.0)))),var.put('a', var.get('c')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(9.0))), var.get('O'), Js(3654602809.0)))),var.put('m', var.get('c')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(12.0))), var.get('R'), Js(3873151461.0)))),var.put('v', var.get('c')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(15.0))), var.get('A'), Js(530742520.0)))),var.put('g', var.get('c')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(2.0))), var.get('V'), Js(3299628645.0)))),var.put('a', var.get('f')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(0.0))), var.get('I'), Js(4096336452.0)))),var.put('m', var.get('f')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(7.0))), var.get('N'), Js(1126891415.0)))),var.put('v', var.get('f')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(14.0))), var.get('M'), Js(2878612391.0)))),var.put('g', var.get('f')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(5.0))), var.get('P'), Js(4237533241.0)))),var.put('a', var.get('f')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(12.0))), var.get('I'), Js(1700485571.0)))),var.put('m', var.get('f')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(3.0))), var.get('N'), Js(2399980690.0)))),var.put('v', var.get('f')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(10.0))), var.get('M'), Js(4293915773.0)))),var.put('g', var.get('f')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(1.0))), var.get('P'), Js(2240044497.0)))),var.put('a', var.get('f')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(8.0))), var.get('I'), Js(1873313359.0)))),var.put('m', var.get('f')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(15.0))), var.get('N'), Js(4264355552.0)))),var.put('v', var.get('f')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(6.0))), var.get('M'), Js(2734768916.0)))),var.put('g', var.get('f')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(13.0))), var.get('P'), Js(1309151649.0)))),var.put('a', var.get('f')(var.get('a'), var.get('g'), var.get('v'), var.get('m'), var.get('b').get((var.get('e')+Js(4.0))), var.get('I'), Js(4149444226.0)))),var.put('m', var.get('f')(var.get('m'), var.get('a'), var.get('g'), var.get('v'), var.get('b').get((var.get('e')+Js(11.0))), var.get('N'), Js(3174756917.0)))),var.put('v', var.get('f')(var.get('v'), var.get('m'), var.get('a'), var.get('g'), var.get('b').get((var.get('e')+Js(2.0))), var.get('M'), Js(718787259.0)))),var.put('g', var.get('f')(var.get('g'), var.get('v'), var.get('m'), var.get('a'), var.get('b').get((var.get('e')+Js(9.0))), var.get('P'), Js(3951481745.0)))),var.put('a', var.get('i')(var.get('a'), var.get('n')))),var.put('g', var.get('i')(var.get('g'), var.get('r')))),var.put('v', var.get('i')(var.get('v'), var.get('o')))),var.put('m', var.get('i')(var.get('m'), var.get('s'))))
                PyJs_LONG_1_()
            finally:
                    var.put('e', Js(16.0), '+')
        var.put('C', (((var.get('p')(var.get('a'))+var.get('p')(var.get('g')))+var.get('p')(var.get('v')))+var.get('p')(var.get('m'))))
        return var.get('C').callprop('toLowerCase')
    PyJs_anonymous_0_._set_name('anonymous')
    var.put('e', PyJs_anonymous_0_)
    @Js
    def PyJs_anonymous_2_(t, e, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 't'])
        return ((var.get('t')<<var.get('e'))|PyJsBshift(var.get('t'),(Js(32.0)-var.get('e'))))
    PyJs_anonymous_2_._set_name('anonymous')
    var.put('n', PyJs_anonymous_2_)
    @Js
    def PyJs_anonymous_3_(t, e, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'r', 'o', 'e', 't', 's', 'n'])
        pass
        def PyJs_LONG_4_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('r', (Js(2147483648.0)&var.get('t'))),var.put('o', (Js(2147483648.0)&var.get('e')))),var.put('n', (Js(1073741824.0)&var.get('t')))),var.put('i', (Js(1073741824.0)&var.get('e')))),var.put('s', ((Js(1073741823.0)&var.get('t'))+(Js(1073741823.0)&var.get('e'))))),((((Js(2147483648.0)^var.get('s'))^var.get('r'))^var.get('o')) if (var.get('n')&var.get('i')) else (((((Js(3221225472.0)^var.get('s'))^var.get('r'))^var.get('o')) if (Js(1073741824.0)&var.get('s')) else (((Js(1073741824.0)^var.get('s'))^var.get('r'))^var.get('o'))) if (var.get('n')|var.get('i')) else ((var.get('s')^var.get('r'))^var.get('o')))))
        return PyJs_LONG_4_()
    PyJs_anonymous_3_._set_name('anonymous')
    var.put('i', PyJs_anonymous_3_)
    @Js
    def PyJs_anonymous_5_(t, e, n, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 't'])
        return ((var.get('t')&var.get('e'))|((~var.get('t'))&var.get('n')))
    PyJs_anonymous_5_._set_name('anonymous')
    var.put('r', PyJs_anonymous_5_)
    @Js
    def PyJs_anonymous_6_(t, e, n, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 't'])
        return ((var.get('t')&var.get('n'))|(var.get('e')&(~var.get('n'))))
    PyJs_anonymous_6_._set_name('anonymous')
    var.put('o', PyJs_anonymous_6_)
    @Js
    def PyJs_anonymous_7_(t, e, n, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 't'])
        return ((var.get('t')^var.get('e'))^var.get('n'))
    PyJs_anonymous_7_._set_name('anonymous')
    var.put('s', PyJs_anonymous_7_)
    @Js
    def PyJs_anonymous_8_(t, e, n, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'e', 't'])
        return (var.get('e')^(var.get('t')|(~var.get('n'))))
    PyJs_anonymous_8_._set_name('anonymous')
    var.put('a', PyJs_anonymous_8_)
    @Js
    def PyJs_anonymous_9_(t, e, o, s, a, h, u, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'o':o, 's':s, 'a':a, 'h':h, 'u':u, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'u', 'h', 'o', 'e', 't', 's'])
        return PyJsComma(var.put('t', var.get('i')(var.get('t'), var.get('i')(var.get('i')(var.get('r')(var.get('e'), var.get('o'), var.get('s')), var.get('a')), var.get('u')))),var.get('i')(var.get('n')(var.get('t'), var.get('h')), var.get('e')))
    PyJs_anonymous_9_._set_name('anonymous')
    var.put('h', PyJs_anonymous_9_)
    @Js
    def PyJs_anonymous_10_(t, e, r, s, a, h, u, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'r':r, 's':s, 'a':a, 'h':h, 'u':u, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'u', 'r', 'h', 'e', 't', 's'])
        return PyJsComma(var.put('t', var.get('i')(var.get('t'), var.get('i')(var.get('i')(var.get('o')(var.get('e'), var.get('r'), var.get('s')), var.get('a')), var.get('u')))),var.get('i')(var.get('n')(var.get('t'), var.get('h')), var.get('e')))
    PyJs_anonymous_10_._set_name('anonymous')
    var.put('u', PyJs_anonymous_10_)
    @Js
    def PyJs_anonymous_11_(t, e, r, o, a, h, u, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'r':r, 'o':o, 'a':a, 'h':h, 'u':u, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'u', 'r', 'h', 'o', 'e', 't'])
        return PyJsComma(var.put('t', var.get('i')(var.get('t'), var.get('i')(var.get('i')(var.get('s')(var.get('e'), var.get('r'), var.get('o')), var.get('a')), var.get('u')))),var.get('i')(var.get('n')(var.get('t'), var.get('h')), var.get('e')))
    PyJs_anonymous_11_._set_name('anonymous')
    var.put('c', PyJs_anonymous_11_)
    @Js
    def PyJs_anonymous_12_(t, e, r, o, s, h, u, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'r':r, 'o':o, 's':s, 'h':h, 'u':u, 'this':this, 'arguments':arguments}, var)
        var.registers(['u', 'r', 'h', 'o', 'e', 't', 's'])
        return PyJsComma(var.put('t', var.get('i')(var.get('t'), var.get('i')(var.get('i')(var.get('a')(var.get('e'), var.get('r'), var.get('o')), var.get('s')), var.get('u')))),var.get('i')(var.get('n')(var.get('t'), var.get('h')), var.get('e')))
    PyJs_anonymous_12_._set_name('anonymous')
    var.put('f', PyJs_anonymous_12_)
    @Js
    def PyJs_anonymous_13_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'a', 'r', 'h', 'o', 'e', 't', 's', 'n'])
        var.put('n', var.get('t').get('length'))
        var.put('i', (var.get('n')+Js(8.0)))
        var.put('r', ((var.get('i')-(var.get('i')%Js(64.0)))/Js(64.0)))
        var.put('o', (Js(16.0)*(var.get('r')+Js(1.0))))
        var.put('s', var.get('Array')((var.get('o')-Js(1.0))))
        var.put('a', Js(0.0))
        var.put('h', Js(0.0))
        while (var.get('h')<var.get('n')):
            PyJsComma(PyJsComma(PyJsComma(var.put('e', ((var.get('h')-(var.get('h')%Js(4.0)))/Js(4.0))),var.put('a', ((var.get('h')%Js(4.0))*Js(8.0)))),var.get('s').put(var.get('e'), (var.get('s').get(var.get('e'))|(var.get('t').callprop('charCodeAt', var.get('h'))<<var.get('a'))))),(var.put('h',Js(var.get('h').to_number())+Js(1))-Js(1)))
        def PyJs_LONG_14_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('e', ((var.get('h')-(var.get('h')%Js(4.0)))/Js(4.0))),var.put('a', ((var.get('h')%Js(4.0))*Js(8.0)))),var.get('s').put(var.get('e'), (var.get('s').get(var.get('e'))|(Js(128.0)<<var.get('a'))))),var.get('s').put((var.get('o')-Js(2.0)), (var.get('n')<<Js(3.0)))),var.get('s').put((var.get('o')-Js(1.0)), PyJsBshift(var.get('n'),Js(29.0)))),var.get('s'))
        return PyJs_LONG_14_()
    PyJs_anonymous_13_._set_name('anonymous')
    var.put('l', PyJs_anonymous_13_)
    @Js
    def PyJs_anonymous_15_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'r', 'e', 't', 'n'])
        var.put('i', Js(''))
        var.put('r', Js(''))
        #for JS loop
        var.put('n', Js(0.0))
        while (var.get('n')<=Js(3.0)):
            try:
                PyJsComma(PyJsComma(var.put('e', (PyJsBshift(var.get('t'),(Js(8.0)*var.get('n')))&Js(255.0))),var.put('r', (Js('0')+var.get('e').callprop('toString', Js(16.0))))),var.put('i', var.get('r').callprop('substr', (var.get('r').get('length')-Js(2.0)), Js(2.0)), '+'))
            finally:
                    (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
        return var.get('i')
    PyJs_anonymous_15_._set_name('anonymous')
    var.put('p', PyJs_anonymous_15_)
    @Js
    def PyJs_anonymous_16_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 't', 'e', 'n'])
        var.put('t', var.get('t').callprop('toString').callprop('replace', JsRegExp('/\\x0d\\x0a/g'), Js('\n')))
        #for JS loop
        var.put('e', Js(''))
        var.put('n', Js(0.0))
        while (var.get('n')<var.get('t').get('length')):
            try:
                var.put('i', var.get('t').callprop('charCodeAt', var.get('n')))
                def PyJs_LONG_17_(var=var):
                    return (PyJsComma(var.put('e', var.get('String').callprop('fromCharCode', ((var.get('i')>>Js(6.0))|Js(192.0))), '+'),var.put('e', var.get('String').callprop('fromCharCode', ((Js(63.0)&var.get('i'))|Js(128.0))), '+')) if ((var.get('i')>Js(127.0)) and (var.get('i')<Js(2048.0))) else PyJsComma(PyJsComma(var.put('e', var.get('String').callprop('fromCharCode', ((var.get('i')>>Js(12.0))|Js(224.0))), '+'),var.put('e', var.get('String').callprop('fromCharCode', (((var.get('i')>>Js(6.0))&Js(63.0))|Js(128.0))), '+')),var.put('e', var.get('String').callprop('fromCharCode', ((Js(63.0)&var.get('i'))|Js(128.0))), '+')))
                (var.put('e', var.get('String').callprop('fromCharCode', var.get('i')), '+') if (var.get('i')<Js(128.0)) else PyJs_LONG_17_())
            finally:
                    (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
        return var.get('e')
    PyJs_anonymous_16_._set_name('anonymous')
    var.put('d', PyJs_anonymous_16_)
    return var.get('e')(var.get('t'))
getHim.func_name = 'a'
var.put('a', getHim)
pass
pass


# Add lib to the module scope
sign = var.to_python()
