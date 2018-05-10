/*
 * =====================================================================================
 *
 *       Filename:  pythoncpp.cpp
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  2017年08月11日 14时22分14秒
 *  Last Modified:  2017年08月11日 14时22分14秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  zt (),
 *   Organization:
 *
 * =====================================================================================
 */

//g++ -fPIC -shared -o a.so pythoncpp.cpp
// use in python:
// import ctypes
// a = ctypes.CDLL('./a.so')
// a.Test()

#include <stdio.h>
#include <stdlib.h>

#ifdef __cplusplus
extern "C" {
#endif

void Test()
{
  printf ( "This is cpp Test\n" );
}

#ifdef __cplusplus
}
#endif


