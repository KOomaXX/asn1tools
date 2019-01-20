import time

from ..version import __version__
from . import uper


SOURCE_FMT = '''\
//! This file was generated by asn1tools version {version} {date}.

{helpers}
{structs}
{definitions}\
'''


def generate(compiled, codec):
    """Generate Rust source code from given compiled specification.

    """

    date = time.ctime()

    if codec == 'uper':
        structs, helpers, definitions = uper.generate(compiled)
    else:
        raise Exception()

    source = SOURCE_FMT.format(version=__version__,
                               date=date,
                               helpers=helpers,
                               structs=structs,
                               definitions=definitions)

    return source
