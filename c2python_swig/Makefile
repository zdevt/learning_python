
all:
	swig -c++ -python c2python_swig.i
	g++ -c -fpic c2python_swig.cpp c2python_swig_wrap.cxx -I /usr/include/python2.7/
	g++ -shared c2python_swig.o c2python_swig_wrap.o -o _c2python_swig.so

clean:
	rm -f *.o *.cxx *.so *.py *.pyc

