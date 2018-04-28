
/*
 * =========================================================================
 *
 *       FileName:  c2python_swig.h
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  2018-02-27 10:12:18
 *  Last Modified:  2018-02-27 10:12:37
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  zt ()
 *   Organization:
 *
 * =========================================================================
 */


#ifndef C2PYTHON_SWIG_INC
#define C2PYTHON_SWIG_INC

#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <string>


class c2python_swig
{
  public:
    c2python_swig();
    virtual ~c2python_swig();
    void test ( std::string a );

  private:

};

#endif /*  C2PYTHON_SWIG_INC  */

