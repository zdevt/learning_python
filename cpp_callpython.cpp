/*
 * =====================================================================================
 *
 *       Filename:  python.cpp
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  2017年08月11日 14时46分32秒
 *  Last Modified:  2017年08月11日 14时46分32秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  zt (),
 *   Organization:
 *
 * =====================================================================================
 */

//g++ python.cpp -o a -g -lpython2.7
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

#include <python2.7/Python.h>

void Test_Add ( int a, int b )
{
  Py_Initialize();

  PyRun_SimpleString ( "import sys" );
  /*  */
  PyRun_SimpleString ( "sys.path.append('./')" );

  /* 模块不能用test之类常见的名字，python内置test模块优先级最高  */
  PyObject* pModule = PyImport_ImportModule ( "test2" );

  if ( !pModule )
    std::cout << "pModule error\n";

  PyObject* pv = PyObject_GetAttrString ( pModule, "Add" );

  if ( !pv )
    std::cout << "pv error\n";

  PyObject* pArg = Py_BuildValue ( "(i,i)", a, b );

  if ( !pArg )
    std::cout << "pArg error\n";

  PyEval_CallObject ( pv, pArg );

  Py_Finalize();
}

void Test_Class ( std::string name )
{
  Py_Initialize();

  PyRun_SimpleString ( "import sys" );
  PyRun_SimpleString ( "sys.path.append('./')" );

  PyObject* pModule = PyImport_ImportModule ( "test2" );

  if ( !pModule )
    std::cout << "pModule !\n";

  PyObject* pClass = PyObject_GetAttrString ( pModule, "TestClass" );

  if ( !pClass )
    std::cout << "pClass!\n";

  PyObject* pArg = PyTuple_New ( 1 );
  PyTuple_SetItem ( pArg, 0, Py_BuildValue ( "s", name.c_str() ) );

  if ( !pArg )
    std::cout << "pArg!\n";

  PyObject* pClassObj = PyEval_CallObject ( pClass, pArg );

  if ( !pClassObj )
    std::cout << "pClassObj!\n";

  PyObject* pFunc = PyObject_GetAttrString ( pClassObj, "printName" );

  if ( !pFunc )
    std::cout << "pFunc!\n";

  PyEval_CallObject ( pFunc, NULL );

  Py_Finalize();
}


int main ( int argc, char* argv[] )
{
  //Test_Add ( 10, 22 );
  Test_Class ( "test class" );
  return 0;
}


