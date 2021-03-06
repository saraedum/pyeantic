#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
#  This file is part of pyeantic.
#
#        Copyright (C) 2019 Vincent Delecroix
#        Copyright (C) 2019 Julian Rüth
#
#  pyeantic is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or (at your
#  option) any later version.
#
#  pyeantic is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with pyeantic. If not, see <https://www.gnu.org/licenses/>.
#####################################################################


import sys
import pytest

from pyeantic import eantic

def test_nf():
    from sage.all import NumberField, QQ, AA, Rational, polygen
    from pyeantic.sage_conversion import sage_nf_to_eantic

    x = polygen(QQ)

    # linear
    K = NumberField(x - 3, 'x', embedding=QQ(3))
    L = sage_nf_to_eantic(K)

    # quadratic
    K = NumberField(2*x**2 - 3, 'A', embedding=AA(Rational((3,2)))**Rational((1,2)))
    L = sage_nf_to_eantic(K)

    # cubic
    p = x**3 - x**2 - x - 1
    s = p.roots(AA, False)[0]
    K = NumberField(x**3 - x**2 - x - 1, 's', embedding=s)
    L = sage_nf_to_eantic(K)

if __name__ == '__main__':
    try:
        import sage.all
    except ImportError:
        sys.exit(0)
    else:
        sys.exit(pytest.main(sys.argv))
