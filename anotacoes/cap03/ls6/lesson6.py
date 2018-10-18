# coding: utf-8

def soma(a, b):
    print 'a antes'
    print a
    a = a + b
    print 'a depois'
    print a
    return a

print soma(1,2)

def abbaize(input1, input2):
    string_normal = input1 + input2
    string_alternate = input2 + input1
    return string_normal + string_alternate
    

print abbaize('dog','cat')