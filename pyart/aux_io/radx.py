"""
pyart.aux_io.radx
=================

Reading files using Radx to first convert the file to Cf.Radial format

.. autosummary::
    :toctree: generated/

    read_radx

"""

import os
import tempfile
import subprocess

from ..io.cfradial import read_cfradial
from ..io.common import _test_arguments


def read_radx(filename, **kwargs):
    """
    Read a file by first converting it to Cf/Radial using RadxConvert.

    Parameters
    ----------
    filename : str
        Name of file to read using RadxConvert.

    Returns
    -------
    radar : Radar
        Radar object.

    """
    #test for non empty kwargs
    _test_arguments(kwargs)

    tmpfile = tempfile.mkstemp(suffix='.nc', dir='.')[1]
    head, tail = os.path.split(tmpfile)
    try:
        subprocess.check_call(
            ['RadxConvert', '-const_ngates',
             '-outdir', head, '-outname', tail, '-f', filename])
        radar = read_cfradial(tmpfile)
    finally:
        os.remove(tmpfile)
    return radar
