'''Wrapper for gevapi.h

Generated with:
ctypesgen.py -lGevApi /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h -o gevapi.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["GevApi"] = load_library("GevApi")

# 1 libraries
# End libraries

# No modules

__time_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 148

__suseconds_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 150

u_int8_t = c_ubyte # /usr/include/x86_64-linux-gnu/sys/types.h: 161

u_int16_t = c_uint # /usr/include/x86_64-linux-gnu/sys/types.h: 162

u_int32_t = c_uint # /usr/include/x86_64-linux-gnu/sys/types.h: 163

u_int64_t = c_ulong # /usr/include/x86_64-linux-gnu/sys/types.h: 165

# /usr/include/x86_64-linux-gnu/bits/types/struct_timeval.h: 8
class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 82
class struct___pthread_internal_list(Structure):
    pass

struct___pthread_internal_list.__slots__ = [
    '__prev',
    '__next',
]
struct___pthread_internal_list._fields_ = [
    ('__prev', POINTER(struct___pthread_internal_list)),
    ('__next', POINTER(struct___pthread_internal_list)),
]

__pthread_list_t = struct___pthread_internal_list # /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 86

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 118
class struct___pthread_mutex_s(Structure):
    pass

struct___pthread_mutex_s.__slots__ = [
    '__lock',
    '__count',
    '__owner',
    '__nusers',
    '__kind',
    '__spins',
    '__elision',
    '__list',
]
struct___pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__nusers', c_uint),
    ('__kind', c_int),
    ('__spins', c_short),
    ('__elision', c_short),
    ('__list', __pthread_list_t),
]

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 151
class struct___pthread_cond_s(Structure):
    pass

struct___pthread_cond_s.__slots__ = [
    '__g_refs',
    '__g_size',
    '__g1_orig_size',
    '__wrefs',
    '__g_signals',
]
struct___pthread_cond_s._fields_ = [
    ('__g_refs', c_uint * 2),
    ('__g_size', c_uint * 2),
    ('__g1_orig_size', c_uint),
    ('__wrefs', c_uint),
    ('__g_signals', c_uint * 2),
]

pthread_t = c_ulong # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 27

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 36
class union_anon_9(Union):
    pass

union_anon_9.__slots__ = [
    '__size',
    '__align',
]
union_anon_9._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]

pthread_mutexattr_t = union_anon_9 # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 36

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 45
class union_anon_10(Union):
    pass

union_anon_10.__slots__ = [
    '__size',
    '__align',
]
union_anon_10._fields_ = [
    ('__size', c_char * 4),
    ('__align', c_int),
]

pthread_condattr_t = union_anon_10 # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 45

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 72
class union_anon_11(Union):
    pass

union_anon_11.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_11._fields_ = [
    ('__data', struct___pthread_mutex_s),
    ('__size', c_char * 40),
    ('__align', c_long),
]

pthread_mutex_t = union_anon_11 # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 72

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 80
class union_anon_12(Union):
    pass

union_anon_12.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_12._fields_ = [
    ('__data', struct___pthread_cond_s),
    ('__size', c_char * 48),
    ('__align', c_longlong),
]

pthread_cond_t = union_anon_12 # /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 80

UINT8 = u_int8_t # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/cordef.h: 799

UINT16 = u_int16_t # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/cordef.h: 801

INT32 = c_int32 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/cordef.h: 802

UINT32 = u_int32_t # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/cordef.h: 803

UINT64 = u_int64_t # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/cordef.h: 806

BOOL = c_int # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/posixcmn.h: 166

enum_anon_89 = c_int # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/corposix.h: 191

MutexType_t = enum_anon_89 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/corposix.h: 191

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/corposix.h: 204
class struct__CRITICAL_SECTION(Structure):
    pass

struct__CRITICAL_SECTION.__slots__ = [
    'type',
    'refCount',
    'waitCount',
    'ownerThread',
    'cvWaiter',
    'cvWaiterAttributes',
    'pCsMutex',
    'pCsMutexAttributes',
    'savedThreadCancelState',
]
struct__CRITICAL_SECTION._fields_ = [
    ('type', MutexType_t),
    ('refCount', c_long),
    ('waitCount', c_long),
    ('ownerThread', pthread_t),
    ('cvWaiter', pthread_cond_t),
    ('cvWaiterAttributes', pthread_condattr_t),
    ('pCsMutex', pthread_mutex_t),
    ('pCsMutexAttributes', pthread_mutexattr_t),
    ('savedThreadCancelState', c_int),
]

CRITICAL_SECTION = struct__CRITICAL_SECTION # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/corposix.h: 204

HANDLE = POINTER(None) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/corposix.h: 237

ULONG_PTR = c_ulong # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/cordef.h: 844

PUINT8 = POINTER(UINT8) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/cordef.h: 914

PUINT32 = POINTER(UINT32) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/cordef.h: 918

PUINT64 = POINTER(UINT64) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/cordef.h: 928

GEV_STATUS = c_int # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gev_linux.h: 95

GEVLIB_STATUS = c_int # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gev_linux.h: 96

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/dynaqueue.h: 59
class struct__DYNAMIC_FIFO(Structure):
    pass

struct__DYNAMIC_FIFO.__slots__ = [
    'Size',
    'Head',
    'Tail',
    'Data',
]
struct__DYNAMIC_FIFO._fields_ = [
    ('Size', INT32),
    ('Head', INT32),
    ('Tail', INT32),
    ('Data', ULONG_PTR * 1),
]

PDYNAMIC_FIFO = POINTER(struct__DYNAMIC_FIFO) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/dynaqueue.h: 59

enum_anon_103 = c_int # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/dynaqueue.h: 151

QueueMode = enum_anon_103 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/dynaqueue.h: 151

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/dynaqueue.h: 169
class struct__DQUEUE(Structure):
    pass

struct__DQUEUE.__slots__ = [
    'cSection',
    'waitEvent',
    'mode',
    'valid',
    'dFifo',
]
struct__DQUEUE._fields_ = [
    ('cSection', CRITICAL_SECTION),
    ('waitEvent', HANDLE),
    ('mode', QueueMode),
    ('valid', c_int),
    ('dFifo', PDYNAMIC_FIFO),
]

DQUEUE = struct__DQUEUE # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/dynaqueue.h: 169

enum_anon_104 = c_int # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtMono8 = 17301505 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtMono8Signed = 17301506 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtMono10 = 17825795 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtMono10Packed = 17563652 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtMono12 = 17825797 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtMono12Packed = 17563654 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtMono14 = 17825829 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtMono16 = 17825799 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerGR8 = 17301512 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerRG8 = 17301513 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerGB8 = 17301514 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerBG8 = 17301515 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerGR10 = 17825804 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerRG10 = 17825805 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerGB10 = 17825806 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerBG10 = 17825807 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerGR10Packed = 17563686 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerRG10Packed = 17563687 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerGB10Packed = 17563688 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerBG10Packed = 17563689 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerGR12 = 17825808 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerRG12 = 17825809 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerGB12 = 17825810 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerBG12 = 17825811 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerGR12Packed = 17563690 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerRG12Packed = 17563691 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerGB12Packed = 17563692 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fMtBayerBG12Packed = 17563693 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB8Packed = 35127316 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtBGR8Packed = 35127317 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGBA8Packed = 35651606 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtBGRA8Packed = 35651607 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB10Packed = 36700184 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtBGR10Packed = 36700185 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB12Packed = 36700186 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtBGR12Packed = 36700187 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB14Packed = 36700254 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtBGR14Packed = 36700234 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB16Packed = 36700211 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtBGR16Packed = 36700235 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGBA16Packed = 37748836 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtBGRA16Packed = 37748817 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB10V1Packed = 35651612 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB10V2Packed = 35651613 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtYUV411packed = 34340894 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtYUV422packed = 34603039 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtYUV444packed = 35127328 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_YUV422_8 = 34603058 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB8Planar = 35127329 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB10Planar = 36700194 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB12Planar = 36700195 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmtRGB16Planar = 36700196 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_BiColorBGRG8 = 34603174 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_BiColorBGRG10 = 35651753 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_BiColorBGRG10p = 34865322 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_BiColorBGRG12 = 35651757 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_BiColorBGRG12p = 35127470 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_BiColorRGBG8 = 34603173 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_BiColorRGBG10 = 35651751 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_BiColorRGBG10p = 34865320 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_BiColorRGBG12 = 35651755 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

fmt_PFNC_BiColorRGBG12p = 35127468 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

enumGevPixelFormat = enum_anon_104 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 249

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 272
if hasattr(_libs['GevApi'], 'GevIsPixelTypeMono'):
    GevIsPixelTypeMono = _libs['GevApi'].GevIsPixelTypeMono
    GevIsPixelTypeMono.argtypes = [UINT32]
    GevIsPixelTypeMono.restype = BOOL

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 273
if hasattr(_libs['GevApi'], 'GevIsPixelTypeRGB'):
    GevIsPixelTypeRGB = _libs['GevApi'].GevIsPixelTypeRGB
    GevIsPixelTypeRGB.argtypes = [UINT32]
    GevIsPixelTypeRGB.restype = BOOL

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 274
if hasattr(_libs['GevApi'], 'GevIsPixelTypeBayer'):
    GevIsPixelTypeBayer = _libs['GevApi'].GevIsPixelTypeBayer
    GevIsPixelTypeBayer.argtypes = [UINT32]
    GevIsPixelTypeBayer.restype = BOOL

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 275
if hasattr(_libs['GevApi'], 'GevIsPixelTypeCustom'):
    GevIsPixelTypeCustom = _libs['GevApi'].GevIsPixelTypeCustom
    GevIsPixelTypeCustom.argtypes = [UINT32]
    GevIsPixelTypeCustom.restype = BOOL

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 276
if hasattr(_libs['GevApi'], 'GevIsPixelTypePacked'):
    GevIsPixelTypePacked = _libs['GevApi'].GevIsPixelTypePacked
    GevIsPixelTypePacked.argtypes = [UINT32]
    GevIsPixelTypePacked.restype = BOOL

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 277
if hasattr(_libs['GevApi'], 'GevGetPixelSizeInBytes'):
    GevGetPixelSizeInBytes = _libs['GevApi'].GevGetPixelSizeInBytes
    GevGetPixelSizeInBytes.argtypes = [UINT32]
    GevGetPixelSizeInBytes.restype = UINT32

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 278
if hasattr(_libs['GevApi'], 'GevGetPixelDepthInBits'):
    GevGetPixelDepthInBits = _libs['GevApi'].GevGetPixelDepthInBits
    GevGetPixelDepthInBits.argtypes = [UINT32]
    GevGetPixelDepthInBits.restype = UINT32

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 279
if hasattr(_libs['GevApi'], 'GevGetRGBPixelOrder'):
    GevGetRGBPixelOrder = _libs['GevApi'].GevGetRGBPixelOrder
    GevGetRGBPixelOrder.argtypes = [UINT32]
    GevGetRGBPixelOrder.restype = UINT32

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 280
if hasattr(_libs['GevApi'], 'GevGetUnpackedPixelType'):
    GevGetUnpackedPixelType = _libs['GevApi'].GevGetUnpackedPixelType
    GevGetUnpackedPixelType.argtypes = [UINT32]
    GevGetUnpackedPixelType.restype = UINT32

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 281
if hasattr(_libs['GevApi'], 'GevGetBayerAsRGBPixelType'):
    GevGetBayerAsRGBPixelType = _libs['GevApi'].GevGetBayerAsRGBPixelType
    GevGetBayerAsRGBPixelType.argtypes = [UINT32]
    GevGetBayerAsRGBPixelType.restype = UINT32

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 282
if hasattr(_libs['GevApi'], 'GevGetPixelComponentCount'):
    GevGetPixelComponentCount = _libs['GevApi'].GevGetPixelComponentCount
    GevGetPixelComponentCount.argtypes = [UINT32]
    GevGetPixelComponentCount.restype = UINT32

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 283
if hasattr(_libs['GevApi'], 'GevGetConvertedPixelType'):
    GevGetConvertedPixelType = _libs['GevApi'].GevGetConvertedPixelType
    GevGetConvertedPixelType.argtypes = [c_int, UINT32]
    GevGetConvertedPixelType.restype = UINT32

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 285
if hasattr(_libs['GevApi'], 'GevTranslateRawPixelFormat'):
    GevTranslateRawPixelFormat = _libs['GevApi'].GevTranslateRawPixelFormat
    GevTranslateRawPixelFormat.argtypes = [UINT32, PUINT32, PUINT32, PUINT32]
    GevTranslateRawPixelFormat.restype = GEVLIB_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 286
if hasattr(_libs['GevApi'], 'GevGetFormatString'):
    GevGetFormatString = _libs['GevApi'].GevGetFormatString
    GevGetFormatString.argtypes = [UINT32]
    if sizeof(c_int) == sizeof(c_void_p):
        GevGetFormatString.restype = ReturnString
    else:
        GevGetFormatString.restype = String
        GevGetFormatString.errcheck = ReturnString

enum_anon_105 = c_int # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 295

GevMonitorMode = 0 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 295

GevControlMode = 2 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 295

GevExclusiveMode = 4 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 295

GevAccessMode = enum_anon_105 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 295

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 313
class struct_anon_106(Structure):
    pass

struct_anon_106.__slots__ = [
    'version',
    'logLevel',
    'numRetries',
    'command_timeout_ms',
    'discovery_timeout_ms',
    'enumeration_port',
    'gvcp_port_range_start',
    'gvcp_port_range_end',
    'manual_xml_handling',
]
struct_anon_106._fields_ = [
    ('version', UINT32),
    ('logLevel', UINT32),
    ('numRetries', UINT32),
    ('command_timeout_ms', UINT32),
    ('discovery_timeout_ms', UINT32),
    ('enumeration_port', UINT32),
    ('gvcp_port_range_start', UINT32),
    ('gvcp_port_range_end', UINT32),
    ('manual_xml_handling', UINT32),
]

GEVLIB_CONFIG_OPTIONS = struct_anon_106 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 313

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 302
class struct_anon_107(Structure):
    pass

struct_anon_107.__slots__ = [
    'version',
    'logLevel',
    'numRetries',
    'command_timeout_ms',
    'discovery_timeout_ms',
    'enumeration_port',
    'gvcp_port_range_start',
    'gvcp_port_range_end',
    'manual_xml_handling',
]
struct_anon_107._fields_ = [
    ('version', UINT32),
    ('logLevel', UINT32),
    ('numRetries', UINT32),
    ('command_timeout_ms', UINT32),
    ('discovery_timeout_ms', UINT32),
    ('enumeration_port', UINT32),
    ('gvcp_port_range_start', UINT32),
    ('gvcp_port_range_end', UINT32),
    ('manual_xml_handling', UINT32),
]

PGEVLIB_CONFIG_OPTIONS = POINTER(struct_anon_107) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 313

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 332
class struct_anon_108(Structure):
    pass

struct_anon_108.__slots__ = [
    'numRetries',
    'command_timeout_ms',
    'heartbeat_timeout_ms',
    'streamPktSize',
    'streamPktDelay',
    'streamNumFramesBuffered',
    'streamMemoryLimitMax',
    'streamMaxPacketResends',
    'streamFrame_timeout_ms',
    'streamThreadAffinity',
    'serverThreadAffinity',
    'msgChannel_timeout_ms',
    'enable_passthru_mode',
]
struct_anon_108._fields_ = [
    ('numRetries', UINT32),
    ('command_timeout_ms', UINT32),
    ('heartbeat_timeout_ms', UINT32),
    ('streamPktSize', UINT32),
    ('streamPktDelay', UINT32),
    ('streamNumFramesBuffered', UINT32),
    ('streamMemoryLimitMax', UINT32),
    ('streamMaxPacketResends', UINT32),
    ('streamFrame_timeout_ms', UINT32),
    ('streamThreadAffinity', INT32),
    ('serverThreadAffinity', INT32),
    ('msgChannel_timeout_ms', UINT32),
    ('enable_passthru_mode', UINT32),
]

GEV_CAMERA_OPTIONS = struct_anon_108 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 332

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 315
class struct_anon_109(Structure):
    pass

struct_anon_109.__slots__ = [
    'numRetries',
    'command_timeout_ms',
    'heartbeat_timeout_ms',
    'streamPktSize',
    'streamPktDelay',
    'streamNumFramesBuffered',
    'streamMemoryLimitMax',
    'streamMaxPacketResends',
    'streamFrame_timeout_ms',
    'streamThreadAffinity',
    'serverThreadAffinity',
    'msgChannel_timeout_ms',
    'enable_passthru_mode',
]
struct_anon_109._fields_ = [
    ('numRetries', UINT32),
    ('command_timeout_ms', UINT32),
    ('heartbeat_timeout_ms', UINT32),
    ('streamPktSize', UINT32),
    ('streamPktDelay', UINT32),
    ('streamNumFramesBuffered', UINT32),
    ('streamMemoryLimitMax', UINT32),
    ('streamMaxPacketResends', UINT32),
    ('streamFrame_timeout_ms', UINT32),
    ('streamThreadAffinity', INT32),
    ('serverThreadAffinity', INT32),
    ('msgChannel_timeout_ms', UINT32),
    ('enable_passthru_mode', UINT32),
]

PGEV_CAMERA_OPTIONS = POINTER(struct_anon_109) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 332

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 342
class struct_anon_110(Structure):
    pass

struct_anon_110.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'ifIndex',
]
struct_anon_110._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('ifIndex', UINT32),
]

GEV_NETWORK_INTERFACE = struct_anon_110 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 342

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 335
class struct_anon_111(Structure):
    pass

struct_anon_111.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'ifIndex',
]
struct_anon_111._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('ifIndex', UINT32),
]

PGEV_NETWORK_INTERFACE = POINTER(struct_anon_111) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 342

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 362
class struct_anon_112(Structure):
    pass

struct_anon_112.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'macLow',
    'macHigh',
    'host',
    'mode',
    'capabilities',
    'manufacturer',
    'model',
    'serial',
    'version',
    'username',
]
struct_anon_112._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('macLow', UINT32),
    ('macHigh', UINT32),
    ('host', GEV_NETWORK_INTERFACE),
    ('mode', UINT32),
    ('capabilities', UINT32),
    ('manufacturer', c_char * (64 + 1)),
    ('model', c_char * (64 + 1)),
    ('serial', c_char * (64 + 1)),
    ('version', c_char * (64 + 1)),
    ('username', c_char * (64 + 1)),
]

GEV_DEVICE_INTERFACE = struct_anon_112 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 362

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 346
class struct_anon_113(Structure):
    pass

struct_anon_113.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'macLow',
    'macHigh',
    'host',
    'mode',
    'capabilities',
    'manufacturer',
    'model',
    'serial',
    'version',
    'username',
]
struct_anon_113._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('macLow', UINT32),
    ('macHigh', UINT32),
    ('host', GEV_NETWORK_INTERFACE),
    ('mode', UINT32),
    ('capabilities', UINT32),
    ('manufacturer', c_char * (64 + 1)),
    ('model', c_char * (64 + 1)),
    ('serial', c_char * (64 + 1)),
    ('version', c_char * (64 + 1)),
    ('username', c_char * (64 + 1)),
]

PGEV_DEVICE_INTERFACE = POINTER(struct_anon_113) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 362

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 362
class struct_anon_114(Structure):
    pass

struct_anon_114.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'macLow',
    'macHigh',
    'host',
    'mode',
    'capabilities',
    'manufacturer',
    'model',
    'serial',
    'version',
    'username',
]
struct_anon_114._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('macLow', UINT32),
    ('macHigh', UINT32),
    ('host', GEV_NETWORK_INTERFACE),
    ('mode', UINT32),
    ('capabilities', UINT32),
    ('manufacturer', c_char * (64 + 1)),
    ('model', c_char * (64 + 1)),
    ('serial', c_char * (64 + 1)),
    ('version', c_char * (64 + 1)),
    ('username', c_char * (64 + 1)),
]

GEV_CAMERA_INFO = struct_anon_114 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 362

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 346
class struct_anon_115(Structure):
    pass

struct_anon_115.__slots__ = [
    'fIPv6',
    'ipAddr',
    'ipAddrLow',
    'ipAddrHigh',
    'macLow',
    'macHigh',
    'host',
    'mode',
    'capabilities',
    'manufacturer',
    'model',
    'serial',
    'version',
    'username',
]
struct_anon_115._fields_ = [
    ('fIPv6', BOOL),
    ('ipAddr', UINT32),
    ('ipAddrLow', UINT32),
    ('ipAddrHigh', UINT32),
    ('macLow', UINT32),
    ('macHigh', UINT32),
    ('host', GEV_NETWORK_INTERFACE),
    ('mode', UINT32),
    ('capabilities', UINT32),
    ('manufacturer', c_char * (64 + 1)),
    ('model', c_char * (64 + 1)),
    ('serial', c_char * (64 + 1)),
    ('version', c_char * (64 + 1)),
    ('username', c_char * (64 + 1)),
]

PGEV_CAMERA_INFO = POINTER(struct_anon_115) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 362

GEV_CAMERA_HANDLE = POINTER(None) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 364

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 399
class struct__tag_GEVBUF_ENTRY(Structure):
    pass

struct__tag_GEVBUF_ENTRY.__slots__ = [
    'payload_type',
    'state',
    'status',
    'timestamp_hi',
    'timestamp_lo',
    'timestamp',
    'recv_size',
    'id',
    'h',
    'w',
    'x_offset',
    'y_offset',
    'x_padding',
    'y_padding',
    'd',
    'format',
    'address',
    'chunk_data',
    'chunk_size',
    'filename',
]
struct__tag_GEVBUF_ENTRY._fields_ = [
    ('payload_type', UINT32),
    ('state', UINT32),
    ('status', INT32),
    ('timestamp_hi', UINT32),
    ('timestamp_lo', UINT32),
    ('timestamp', UINT64),
    ('recv_size', UINT64),
    ('id', UINT64),
    ('h', UINT32),
    ('w', UINT32),
    ('x_offset', UINT32),
    ('y_offset', UINT32),
    ('x_padding', UINT32),
    ('y_padding', UINT32),
    ('d', UINT32),
    ('format', UINT32),
    ('address', PUINT8),
    ('chunk_data', PUINT8),
    ('chunk_size', UINT32),
    ('filename', c_char * 256),
]

GEVBUF_ENTRY = struct__tag_GEVBUF_ENTRY # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 399

PGEVBUF_ENTRY = POINTER(struct__tag_GEVBUF_ENTRY) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 399

GEVBUF_HEADER = struct__tag_GEVBUF_ENTRY # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 399

PGEVBUF_HEADER = POINTER(struct__tag_GEVBUF_ENTRY) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 399

GEV_BUFFER_OBJECT = struct__tag_GEVBUF_ENTRY # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 399

PGEV_BUFFER_OBJECT = POINTER(struct__tag_GEVBUF_ENTRY) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 399

enum_anon_116 = c_int # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 414

Asynchronous = 0 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 414

SynchronousNextEmpty = 1 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 414

GevBufferCyclingMode = enum_anon_116 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 414

GEVTL_CBFUNCTION = CFUNCTYPE(UNCHECKED(None), PGEV_BUFFER_OBJECT, POINTER(None)) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 417

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 438
class struct__GEVBUF_QUEUE(Structure):
    pass

struct__GEVBUF_QUEUE.__slots__ = [
    'type',
    'size',
    'numBuffer',
    'height',
    'width',
    'depth',
    'lastBuffer',
    'nextBuffer',
    'trashCount',
    'cyclingMode',
    'pEmptyBuffers',
    'pFullBuffers',
    'trashBuf',
    'pCurBuf',
    'buffer',
]
struct__GEVBUF_QUEUE._fields_ = [
    ('type', UINT32),
    ('size', UINT64),
    ('numBuffer', UINT32),
    ('height', UINT32),
    ('width', UINT32),
    ('depth', UINT32),
    ('lastBuffer', INT32),
    ('nextBuffer', UINT32),
    ('trashCount', UINT32),
    ('cyclingMode', GevBufferCyclingMode),
    ('pEmptyBuffers', POINTER(DQUEUE)),
    ('pFullBuffers', POINTER(DQUEUE)),
    ('trashBuf', GEVBUF_ENTRY),
    ('pCurBuf', POINTER(GEVBUF_ENTRY)),
    ('buffer', GEVBUF_ENTRY * 1),
]

GEV_BUFFER_LIST = struct__GEVBUF_QUEUE # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 438

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 449
class struct_anon_117(Structure):
    pass

struct_anon_117.__slots__ = [
    'eventNumber',
    'streamChannelIndex',
    'blockId',
    'timestamp',
    'timeStampHigh',
    'timeStampLow',
]
struct_anon_117._fields_ = [
    ('eventNumber', UINT16),
    ('streamChannelIndex', UINT16),
    ('blockId', UINT64),
    ('timestamp', UINT64),
    ('timeStampHigh', UINT32),
    ('timeStampLow', UINT32),
]

EVENT_MSG = struct_anon_117 # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 449

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 441
class struct_anon_118(Structure):
    pass

struct_anon_118.__slots__ = [
    'eventNumber',
    'streamChannelIndex',
    'blockId',
    'timestamp',
    'timeStampHigh',
    'timeStampLow',
]
struct_anon_118._fields_ = [
    ('eventNumber', UINT16),
    ('streamChannelIndex', UINT16),
    ('blockId', UINT64),
    ('timestamp', UINT64),
    ('timeStampHigh', UINT32),
    ('timeStampLow', UINT32),
]

PEVENT_MSG = POINTER(struct_anon_118) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 449

GEVEVENT_CBFUNCTION = CFUNCTYPE(UNCHECKED(None), PEVENT_MSG, PUINT8, UINT16, POINTER(None)) # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 451

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 456
if hasattr(_libs['GevApi'], 'GevFormatCameraInfo'):
    GevFormatCameraInfo = _libs['GevApi'].GevFormatCameraInfo
    GevFormatCameraInfo.argtypes = [POINTER(GEV_DEVICE_INTERFACE), String, UINT32]
    GevFormatCameraInfo.restype = UINT32

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 458
if hasattr(_libs['GevApi'], 'GevPrint'):
    _func = _libs['GevApi'].GevPrint
    _restype = c_int
    _argtypes = [c_int, String, c_uint, String]
    GevPrint = _variadic_function(_func,_restype,_argtypes)

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 556
if hasattr(_libs['GevApi'], 'GevApiInitialize'):
    GevApiInitialize = _libs['GevApi'].GevApiInitialize
    GevApiInitialize.argtypes = []
    GevApiInitialize.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 557
if hasattr(_libs['GevApi'], 'GevApiUninitialize'):
    GevApiUninitialize = _libs['GevApi'].GevApiUninitialize
    GevApiUninitialize.argtypes = []
    GevApiUninitialize.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 561
if hasattr(_libs['GevApi'], 'GevGetLibraryConfigOptions'):
    GevGetLibraryConfigOptions = _libs['GevApi'].GevGetLibraryConfigOptions
    GevGetLibraryConfigOptions.argtypes = [POINTER(GEVLIB_CONFIG_OPTIONS)]
    GevGetLibraryConfigOptions.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 562
if hasattr(_libs['GevApi'], 'GevSetLibraryConfigOptions'):
    GevSetLibraryConfigOptions = _libs['GevApi'].GevSetLibraryConfigOptions
    GevSetLibraryConfigOptions.argtypes = [POINTER(GEVLIB_CONFIG_OPTIONS)]
    GevSetLibraryConfigOptions.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 566
if hasattr(_libs['GevApi'], 'GevDeviceCount'):
    GevDeviceCount = _libs['GevApi'].GevDeviceCount
    GevDeviceCount.argtypes = []
    GevDeviceCount.restype = c_int

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 567
if hasattr(_libs['GevApi'], 'GevGetCameraList'):
    GevGetCameraList = _libs['GevApi'].GevGetCameraList
    GevGetCameraList.argtypes = [POINTER(GEV_CAMERA_INFO), c_int, POINTER(c_int)]
    GevGetCameraList.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 569
if hasattr(_libs['GevApi'], 'GevForceCameraIPAddress'):
    GevForceCameraIPAddress = _libs['GevApi'].GevForceCameraIPAddress
    GevForceCameraIPAddress.argtypes = [UINT32, UINT32, UINT32, UINT32]
    GevForceCameraIPAddress.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 570
if hasattr(_libs['GevApi'], 'GevEnumerateNetworkInterfaces'):
    GevEnumerateNetworkInterfaces = _libs['GevApi'].GevEnumerateNetworkInterfaces
    GevEnumerateNetworkInterfaces.argtypes = [POINTER(GEV_NETWORK_INTERFACE), UINT32, PUINT32]
    GevEnumerateNetworkInterfaces.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 574
if hasattr(_libs['GevApi'], 'GevEnumerateGevDevices'):
    GevEnumerateGevDevices = _libs['GevApi'].GevEnumerateGevDevices
    GevEnumerateGevDevices.argtypes = [POINTER(GEV_NETWORK_INTERFACE), UINT32, POINTER(GEV_DEVICE_INTERFACE), UINT32, PUINT32]
    GevEnumerateGevDevices.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 577
if hasattr(_libs['GevApi'], 'GevSetCameraList'):
    GevSetCameraList = _libs['GevApi'].GevSetCameraList
    GevSetCameraList.argtypes = [POINTER(GEV_CAMERA_INFO), c_int]
    GevSetCameraList.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 581
if hasattr(_libs['GevApi'], 'GevOpenCamera'):
    GevOpenCamera = _libs['GevApi'].GevOpenCamera
    GevOpenCamera.argtypes = [POINTER(GEV_CAMERA_INFO), GevAccessMode, POINTER(GEV_CAMERA_HANDLE)]
    GevOpenCamera.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 582
if hasattr(_libs['GevApi'], 'GevOpenCameraByAddress'):
    GevOpenCameraByAddress = _libs['GevApi'].GevOpenCameraByAddress
    GevOpenCameraByAddress.argtypes = [c_ulong, GevAccessMode, POINTER(GEV_CAMERA_HANDLE)]
    GevOpenCameraByAddress.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 583
if hasattr(_libs['GevApi'], 'GevOpenCameraByName'):
    GevOpenCameraByName = _libs['GevApi'].GevOpenCameraByName
    GevOpenCameraByName.argtypes = [String, GevAccessMode, POINTER(GEV_CAMERA_HANDLE)]
    GevOpenCameraByName.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 584
if hasattr(_libs['GevApi'], 'GevOpenCameraBySN'):
    GevOpenCameraBySN = _libs['GevApi'].GevOpenCameraBySN
    GevOpenCameraBySN.argtypes = [String, GevAccessMode, POINTER(GEV_CAMERA_HANDLE)]
    GevOpenCameraBySN.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 586
if hasattr(_libs['GevApi'], 'GevCloseCamera'):
    GevCloseCamera = _libs['GevApi'].GevCloseCamera
    GevCloseCamera.argtypes = [POINTER(GEV_CAMERA_HANDLE)]
    GevCloseCamera.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 588
if hasattr(_libs['GevApi'], 'Gev_Reconnect'):
    Gev_Reconnect = _libs['GevApi'].Gev_Reconnect
    Gev_Reconnect.argtypes = [GEV_CAMERA_HANDLE]
    Gev_Reconnect.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 590
if hasattr(_libs['GevApi'], 'GevGetCameraInfo'):
    GevGetCameraInfo = _libs['GevApi'].GevGetCameraInfo
    GevGetCameraInfo.argtypes = [GEV_CAMERA_HANDLE]
    GevGetCameraInfo.restype = POINTER(GEV_CAMERA_INFO)

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 592
if hasattr(_libs['GevApi'], 'GevGetCameraInterfaceOptions'):
    GevGetCameraInterfaceOptions = _libs['GevApi'].GevGetCameraInterfaceOptions
    GevGetCameraInterfaceOptions.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_CAMERA_OPTIONS)]
    GevGetCameraInterfaceOptions.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 593
if hasattr(_libs['GevApi'], 'GevSetCameraInterfaceOptions'):
    GevSetCameraInterfaceOptions = _libs['GevApi'].GevSetCameraInterfaceOptions
    GevSetCameraInterfaceOptions.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_CAMERA_OPTIONS)]
    GevSetCameraInterfaceOptions.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 597
if hasattr(_libs['GevApi'], 'Gev_RetrieveXMLData'):
    Gev_RetrieveXMLData = _libs['GevApi'].Gev_RetrieveXMLData
    Gev_RetrieveXMLData.argtypes = [GEV_CAMERA_HANDLE, c_int, String, POINTER(c_int), POINTER(c_int)]
    Gev_RetrieveXMLData.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 598
if hasattr(_libs['GevApi'], 'Gev_RetrieveXMLFile'):
    Gev_RetrieveXMLFile = _libs['GevApi'].Gev_RetrieveXMLFile
    Gev_RetrieveXMLFile.argtypes = [GEV_CAMERA_HANDLE, String, c_int, BOOL]
    Gev_RetrieveXMLFile.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 602
if hasattr(_libs['GevApi'], 'GevConnectFeatures'):
    GevConnectFeatures = _libs['GevApi'].GevConnectFeatures
    GevConnectFeatures.argtypes = [GEV_CAMERA_HANDLE, POINTER(None)]
    GevConnectFeatures.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 603
if hasattr(_libs['GevApi'], 'GevGetFeatureNodeMap'):
    GevGetFeatureNodeMap = _libs['GevApi'].GevGetFeatureNodeMap
    GevGetFeatureNodeMap.argtypes = [GEV_CAMERA_HANDLE]
    GevGetFeatureNodeMap.restype = POINTER(None)

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 607
if hasattr(_libs['GevApi'], 'GevGetGenICamXML_FileName'):
    GevGetGenICamXML_FileName = _libs['GevApi'].GevGetGenICamXML_FileName
    GevGetGenICamXML_FileName.argtypes = [GEV_CAMERA_HANDLE, c_int, String]
    GevGetGenICamXML_FileName.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 608
if hasattr(_libs['GevApi'], 'GevInitGenICamXMLFeatures'):
    GevInitGenICamXMLFeatures = _libs['GevApi'].GevInitGenICamXMLFeatures
    GevInitGenICamXMLFeatures.argtypes = [GEV_CAMERA_HANDLE, BOOL]
    GevInitGenICamXMLFeatures.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 609
if hasattr(_libs['GevApi'], 'GevInitGenICamXMLFeatures_FromFile'):
    GevInitGenICamXMLFeatures_FromFile = _libs['GevApi'].GevInitGenICamXMLFeatures_FromFile
    GevInitGenICamXMLFeatures_FromFile.argtypes = [GEV_CAMERA_HANDLE, String]
    GevInitGenICamXMLFeatures_FromFile.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 610
if hasattr(_libs['GevApi'], 'GevInitGenICamXMLFeatures_FromData'):
    GevInitGenICamXMLFeatures_FromData = _libs['GevApi'].GevInitGenICamXMLFeatures_FromData
    GevInitGenICamXMLFeatures_FromData.argtypes = [GEV_CAMERA_HANDLE, c_int, POINTER(None)]
    GevInitGenICamXMLFeatures_FromData.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 612
if hasattr(_libs['GevApi'], 'GevGetFeatureValue'):
    GevGetFeatureValue = _libs['GevApi'].GevGetFeatureValue
    GevGetFeatureValue.argtypes = [GEV_CAMERA_HANDLE, String, POINTER(c_int), c_int, POINTER(None)]
    GevGetFeatureValue.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 613
if hasattr(_libs['GevApi'], 'GevSetFeatureValue'):
    GevSetFeatureValue = _libs['GevApi'].GevSetFeatureValue
    GevSetFeatureValue.argtypes = [GEV_CAMERA_HANDLE, String, c_int, POINTER(None)]
    GevSetFeatureValue.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 614
if hasattr(_libs['GevApi'], 'GevGetFeatureValueAsString'):
    GevGetFeatureValueAsString = _libs['GevApi'].GevGetFeatureValueAsString
    GevGetFeatureValueAsString.argtypes = [GEV_CAMERA_HANDLE, String, POINTER(c_int), c_int, String]
    GevGetFeatureValueAsString.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 615
if hasattr(_libs['GevApi'], 'GevSetFeatureValueAsString'):
    GevSetFeatureValueAsString = _libs['GevApi'].GevSetFeatureValueAsString
    GevSetFeatureValueAsString.argtypes = [GEV_CAMERA_HANDLE, String, String]
    GevSetFeatureValueAsString.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 620
if hasattr(_libs['GevApi'], 'GevInitializeTransfer'):
    GevInitializeTransfer = _libs['GevApi'].GevInitializeTransfer
    GevInitializeTransfer.argtypes = [GEV_CAMERA_HANDLE, GevBufferCyclingMode, UINT64, UINT32, POINTER(POINTER(UINT8))]
    GevInitializeTransfer.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 621
if hasattr(_libs['GevApi'], 'GevFreeTransfer'):
    GevFreeTransfer = _libs['GevApi'].GevFreeTransfer
    GevFreeTransfer.argtypes = [GEV_CAMERA_HANDLE]
    GevFreeTransfer.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 622
if hasattr(_libs['GevApi'], 'GevGetPayloadParameters'):
    GevGetPayloadParameters = _libs['GevApi'].GevGetPayloadParameters
    GevGetPayloadParameters.argtypes = [GEV_CAMERA_HANDLE, PUINT64, PUINT32]
    GevGetPayloadParameters.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 624
if hasattr(_libs['GevApi'], 'GevStartTransfer'):
    GevStartTransfer = _libs['GevApi'].GevStartTransfer
    GevStartTransfer.argtypes = [GEV_CAMERA_HANDLE, UINT32]
    GevStartTransfer.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 625
if hasattr(_libs['GevApi'], 'GevStopTransfer'):
    GevStopTransfer = _libs['GevApi'].GevStopTransfer
    GevStopTransfer.argtypes = [GEV_CAMERA_HANDLE]
    GevStopTransfer.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 626
if hasattr(_libs['GevApi'], 'GevAbortTransfer'):
    GevAbortTransfer = _libs['GevApi'].GevAbortTransfer
    GevAbortTransfer.argtypes = [GEV_CAMERA_HANDLE]
    GevAbortTransfer.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 628
if hasattr(_libs['GevApi'], 'GevQueryTransferStatus'):
    GevQueryTransferStatus = _libs['GevApi'].GevQueryTransferStatus
    GevQueryTransferStatus.argtypes = [GEV_CAMERA_HANDLE, PUINT32, PUINT32, PUINT32, PUINT32, POINTER(GevBufferCyclingMode)]
    GevQueryTransferStatus.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 629
if hasattr(_libs['GevApi'], 'GevWaitForNextFrame'):
    GevWaitForNextFrame = _libs['GevApi'].GevWaitForNextFrame
    GevWaitForNextFrame.argtypes = [GEV_CAMERA_HANDLE, POINTER(POINTER(GEV_BUFFER_OBJECT)), UINT32]
    GevWaitForNextFrame.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 630
if hasattr(_libs['GevApi'], 'GevGetNextFrame'):
    GevGetNextFrame = _libs['GevApi'].GevGetNextFrame
    GevGetNextFrame.argtypes = [GEV_CAMERA_HANDLE, POINTER(POINTER(GEV_BUFFER_OBJECT)), POINTER(struct_timeval)]
    GevGetNextFrame.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 632
if hasattr(_libs['GevApi'], 'GevReleaseFrame'):
    GevReleaseFrame = _libs['GevApi'].GevReleaseFrame
    GevReleaseFrame.argtypes = [GEV_CAMERA_HANDLE, POINTER(GEV_BUFFER_OBJECT)]
    GevReleaseFrame.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 633
if hasattr(_libs['GevApi'], 'GevReleaseFrameBuffer'):
    GevReleaseFrameBuffer = _libs['GevApi'].GevReleaseFrameBuffer
    GevReleaseFrameBuffer.argtypes = [GEV_CAMERA_HANDLE, POINTER(None)]
    GevReleaseFrameBuffer.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 637
if hasattr(_libs['GevApi'], 'GevGetImageParameters'):
    GevGetImageParameters = _libs['GevApi'].GevGetImageParameters
    GevGetImageParameters.argtypes = [GEV_CAMERA_HANDLE, PUINT32, PUINT32, PUINT32, PUINT32, PUINT32]
    GevGetImageParameters.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 638
if hasattr(_libs['GevApi'], 'GevSetImageParameters'):
    GevSetImageParameters = _libs['GevApi'].GevSetImageParameters
    GevSetImageParameters.argtypes = [GEV_CAMERA_HANDLE, UINT32, UINT32, UINT32, UINT32, UINT32]
    GevSetImageParameters.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 640
if hasattr(_libs['GevApi'], 'GevInitImageTransfer'):
    GevInitImageTransfer = _libs['GevApi'].GevInitImageTransfer
    GevInitImageTransfer.argtypes = [GEV_CAMERA_HANDLE, GevBufferCyclingMode, UINT32, POINTER(POINTER(UINT8))]
    GevInitImageTransfer.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 641
if hasattr(_libs['GevApi'], 'GevInitializeImageTransfer'):
    GevInitializeImageTransfer = _libs['GevApi'].GevInitializeImageTransfer
    GevInitializeImageTransfer.argtypes = [GEV_CAMERA_HANDLE, UINT32, POINTER(POINTER(UINT8))]
    GevInitializeImageTransfer.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 650
if hasattr(_libs['GevApi'], 'GetPixelSizeInBytes'):
    GetPixelSizeInBytes = _libs['GevApi'].GetPixelSizeInBytes
    GetPixelSizeInBytes.argtypes = [UINT32]
    GetPixelSizeInBytes.restype = c_int

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 653
if hasattr(_libs['GevApi'], 'GevGetImageBuffer'):
    GevGetImageBuffer = _libs['GevApi'].GevGetImageBuffer
    GevGetImageBuffer.argtypes = [GEV_CAMERA_HANDLE, POINTER(POINTER(None))]
    GevGetImageBuffer.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 654
if hasattr(_libs['GevApi'], 'GevGetImage'):
    GevGetImage = _libs['GevApi'].GevGetImage
    GevGetImage.argtypes = [GEV_CAMERA_HANDLE, POINTER(POINTER(GEV_BUFFER_OBJECT))]
    GevGetImage.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 655
if hasattr(_libs['GevApi'], 'GevWaitForNextImageBuffer'):
    GevWaitForNextImageBuffer = _libs['GevApi'].GevWaitForNextImageBuffer
    GevWaitForNextImageBuffer.argtypes = [GEV_CAMERA_HANDLE, POINTER(POINTER(None)), UINT32]
    GevWaitForNextImageBuffer.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 664
if hasattr(_libs['GevApi'], 'GevRegisterEventCallback'):
    GevRegisterEventCallback = _libs['GevApi'].GevRegisterEventCallback
    GevRegisterEventCallback.argtypes = [GEV_CAMERA_HANDLE, UINT32, GEVEVENT_CBFUNCTION, POINTER(None)]
    GevRegisterEventCallback.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 665
if hasattr(_libs['GevApi'], 'GevRegisterApplicationEvent'):
    GevRegisterApplicationEvent = _libs['GevApi'].GevRegisterApplicationEvent
    GevRegisterApplicationEvent.argtypes = [GEV_CAMERA_HANDLE, UINT32, HANDLE]
    GevRegisterApplicationEvent.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 666
if hasattr(_libs['GevApi'], 'GevUnregisterEvent'):
    GevUnregisterEvent = _libs['GevApi'].GevUnregisterEvent
    GevUnregisterEvent.argtypes = [GEV_CAMERA_HANDLE, UINT32]
    GevUnregisterEvent.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 680
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ConvertBayerToRGB'):
        continue
    ConvertBayerToRGB = _lib.ConvertBayerToRGB
    ConvertBayerToRGB.argtypes = [c_int, UINT32, UINT32, UINT32, POINTER(None), UINT32, POINTER(None)]
    ConvertBayerToRGB.restype = GEV_STATUS
    break

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 683
if hasattr(_libs['GevApi'], 'Gev_UnpackMonoPackedFrame'):
    Gev_UnpackMonoPackedFrame = _libs['GevApi'].Gev_UnpackMonoPackedFrame
    Gev_UnpackMonoPackedFrame.argtypes = [UINT32, UINT32, POINTER(None), UINT32, POINTER(None)]
    Gev_UnpackMonoPackedFrame.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 686
if hasattr(_libs['GevApi'], 'Gev_DecodeTurboDriveFrame'):
    Gev_DecodeTurboDriveFrame = _libs['GevApi'].Gev_DecodeTurboDriveFrame
    Gev_DecodeTurboDriveFrame.argtypes = [UINT32, UINT32, UINT32, UINT32, UINT32, UINT64, POINTER(None), UINT64, POINTER(None), POINTER(UINT64), POINTER(UINT64)]
    Gev_DecodeTurboDriveFrame.restype = GEV_STATUS

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 46
try:
    GENICAM_TARGET_ROOT_VERSION = 'GENICAM_ROOT_V3_0'
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 47
try:
    GIGEV_XML_DOWNLOAD = 'GIGEV_XML_DOWNLOAD'
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 65
try:
    GEV_LOG_LEVEL_OFF = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 66
try:
    GEV_LOG_LEVEL_NORMAL = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 67
try:
    GEV_LOG_LEVEL_ERRORS = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 68
try:
    GEV_LOG_LEVEL_WARNINGS = 2
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 69
try:
    GEV_LOG_LEVEL_DEBUG = 3
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 70
try:
    GEV_LOG_LEVEL_TRACE = 4
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 72
try:
    GEV_LOG_FATAL = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 73
try:
    GEV_LOG_ERROR = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 74
try:
    GEV_LOG_WARNING = 2
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 75
try:
    GEV_LOG_INFO = 3
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 76
try:
    GEV_LOG_DEBUG = 3
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 77
try:
    GEV_LOG_TRACE = 4
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 82
try:
    GEVLIB_OK = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 83
try:
    GEVLIB_SUCCESS = GEVLIB_OK
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 84
try:
    GEVLIB_STATUS_SUCCESS = GEVLIB_OK
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 85
try:
    GEVLIB_STATUS_ERROR = (-1)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 88
try:
    GEVLIB_ERROR_GENERIC = (-1)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 89
try:
    GEVLIB_ERROR_NULL_PTR = (-2)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 90
try:
    GEVLIB_ERROR_ARG_INVALID = (-3)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 91
try:
    GEVLIB_ERROR_INVALID_HANDLE = (-4)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 92
try:
    GEVLIB_ERROR_NOT_SUPPORTED = (-5)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 93
try:
    GEVLIB_ERROR_TIME_OUT = (-6)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 94
try:
    GEVLIB_ERROR_NOT_IMPLEMENTED = (-10)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 95
try:
    GEVLIB_ERROR_NO_CAMERA = (-11)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 96
try:
    GEVLIB_ERROR_INVALID_PIXEL_FORMAT = (-12)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 97
try:
    GEVLIB_ERROR_PARAMETER_INVALID = (-13)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 98
try:
    GEVLIB_ERROR_SOFTWARE = (-14)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 99
try:
    GEVLIB_ERROR_API_NOT_INITIALIZED = (-15)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 100
try:
    GEVLIB_ERROR_DEVICE_NOT_FOUND = (-16)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 101
try:
    GEVLIB_ERROR_ACCESS_DENIED = (-17)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 102
try:
    GEVLIB_ERROR_NOT_AVAILABLE = (-18)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 103
try:
    GEVLIB_ERROR_NO_SPACE = (-19)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 104
try:
    GEVLIB_ERROR_XFER_NOT_INITIALIZED = (-20)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 105
try:
    GEVLIB_ERROR_XFER_ACTIVE = (-21)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 106
try:
    GEVLIB_ERROR_XFER_NOT_ACTIVE = (-22)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 109
try:
    GEVLIB_ERROR_SYSTEM_RESOURCE = (-2001)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 110
try:
    GEVLIB_ERROR_INSUFFICIENT_MEMORY = (-2002)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 111
try:
    GEVLIB_ERROR_INSUFFICIENT_BANDWIDTH = (-2003)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 112
try:
    GEVLIB_ERROR_RESOURCE_NOT_ALLOCATED = (-2004)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 113
try:
    GEVLIB_ERROR_RESOURCE_IN_USE = (-2005)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 114
try:
    GEVLIB_ERROR_RESOURCE_NOT_ENABLED = (-2006)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 115
try:
    GEVLIB_ERROR_RESOURCE_NOT_INITIALIZED = (-2007)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 116
try:
    GEVLIB_ERROR_RESOURCE_CORRUPTED = (-2008)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 117
try:
    GEVLIB_ERROR_RESOURCE_MISSING = (-2009)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 118
try:
    GEVLIB_ERROR_RESOURCE_LACK = (-2010)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 119
try:
    GEVLIB_ERROR_RESOURCE_ACCESS = (-2011)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 120
try:
    GEVLIB_ERROR_RESOURCE_INVALID = (-2012)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 121
try:
    GEVLIB_ERROR_RESOURCE_LOCK = (-2013)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 122
try:
    GEVLIB_ERROR_INSUFFICIENT_PRIVILEGE = (-2014)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 123
try:
    GEVLIB_ERROR_RESOURCE_WRITE_PROTECTED = (-2015)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 124
try:
    GEVLIB_ERROR_RESOURCE_INCOHERENCY = (-2016)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 127
try:
    GEVLIB_ERROR_DATA_NO_MESSAGES = (-5001)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 128
try:
    GEVLIB_ERROR_DATA_OVERFLOW = (-5002)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 129
try:
    GEVLIB_ERROR_DATA_CHECKSUM = (-5003)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 130
try:
    GEVLIB_ERROR_DATA_NOT_AVAILABLE = (-5004)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 131
try:
    GEVLIB_ERROR_DATA_OVERRUN = (-5005)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 132
try:
    GEVLIB_ERROR_DATA_XFER_ABORT = (-5006)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 133
try:
    GEVLIB_ERROR_DATA_INVALID_HEADER = (-5007)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 134
try:
    GEVLIB_ERROR_DATA_ALIGNMENT = (-5008)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 137
try:
    GEVLIB_ERROR_CONNECTION_DROPPED = (-11000)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 138
try:
    GEVLIB_ERROR_ANSWER_TIMEOUT = (-11001)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 139
try:
    GEVLIB_ERROR_SOCKET_INVALID = (-11002)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 140
try:
    GEVLIB_ERROR_PORT_NOT_AVAILABLE = (-11003)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 141
try:
    GEVLIB_ERROR_INVALID_IP = (-11004)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 142
try:
    GEVLIB_ERROR_INVALID_CAMERA_OPERATION = (-11005)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 143
try:
    GEVLIB_ERROR_INVALID_PACKET = (-11006)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 144
try:
    GEVLIB_ERROR_INVALID_CONNECTION_ATTEMPT = (-11007)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 145
try:
    GEVLIB_ERROR_PROTOCOL = (-11008)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 146
try:
    GEVLIB_ERROR_WINDOWS_SOCKET_INIT = (-11009)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 147
try:
    GEVLIB_ERROR_WINDOWS_SOCKET_CLOSE = (-11010)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 148
try:
    GEVLIB_ERROR_SOCKET_CREATE = (-11011)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 149
try:
    GEVLIB_ERROR_SOCKET_RELEASE = (-11012)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 150
try:
    GEVLIB_ERROR_SOCKET_DATA_SEND = (-11013)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 151
try:
    GEVLIB_ERROR_SOCKET_DATA_READ = (-11014)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 152
try:
    GEVLIB_ERROR_SOCKET_WAIT_ACKNOWLEDGE = (-11015)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 153
try:
    GEVLIB_ERROR_INVALID_INTERNAL_COMMAND = (-11016)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 154
try:
    GEVLIB_ERROR_INVALID_ACKNOWLEDGE = (-11017)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 155
try:
    GEVLIB_ERROR_PREVIOUS_ACKNOWLEDGE = (-11018)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 156
try:
    GEVLIB_ERROR_INVALID_MESSAGE = (-11019)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 157
try:
    GEVLIB_ERROR_GIGE_ERROR = (-11020)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 163
try:
    GEV_STATUS_SUCCESS = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 164
try:
    GEV_STATUS_NOT_IMPLEMENTED = 32769
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 165
try:
    GEV_STATUS_INVALID_PARAMETER = 32770
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 166
try:
    GEV_STATUS_INVALID_ADDRESS = 32771
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 167
try:
    GEV_STATUS_WRITE_PROTECT = 32772
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 168
try:
    GEV_STATUS_BAD_ALIGNMENT = 32773
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 169
try:
    GEV_STATUS_ACCESS_DENIED = 32774
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 170
try:
    GEV_STATUS_BUSY = 32775
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 171
try:
    GEV_STATUS_LOCAL_PROBLEM = 32776
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 172
try:
    GEV_STATUS_MSG_MISMATCH = 32777
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 173
try:
    GEV_STATUS_INVALID_PROTOCOL = 32778
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 174
try:
    GEV_STATUS_NO_MSG = 32779
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 175
try:
    GEV_STATUS_PACKET_UNAVAILABLE = 32780
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 176
try:
    GEV_STATUS_DATA_OVERRUN = 32781
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 177
try:
    GEV_STATUS_INVALID_HEADER = 32782
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 179
try:
    GEV_STATUS_ERROR = 36863
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 251
try:
    GEV_PIXFORMAT_ISMONO = 16777216
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 252
try:
    GEV_PIXFORMAT_ISCOLOR = 33554432
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 253
try:
    GEV_PIXFORMAT_ISCUSTOM = 2147483648
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 255
try:
    GEV_PIXEL_FORMAT_MONO = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 256
try:
    GEV_PIXEL_FORMAT_MONO_PACKED = 2
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 257
try:
    GEV_PIXEL_FORMAT_RGB = 4
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 258
try:
    GEV_PIXEL_FORMAT_RGB_PACKED = 8
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 259
try:
    GEV_PIXEL_FORMAT_BAYER = 16
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 260
try:
    GEV_PIXEL_FORMAT_YUV = 32
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 261
try:
    GEV_PIXEL_FORMAT_RGB_PLANAR = 64
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 263
try:
    GEV_PIXEL_ORDER_NONE = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 264
try:
    GEV_PIXEL_ORDER_RGB = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 265
try:
    GEV_PIXEL_ORDER_BGR = 2
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 266
try:
    GEV_PIXEL_ORDER_GRB = 4
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 267
try:
    GEV_PIXEL_ORDER_GBR = 8
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 268
try:
    GEV_PIXEL_ORDER_RGB10V1 = 61440
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 269
try:
    GEV_PIXEL_ORDER_RGB10V2 = 57344
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 344
try:
    MAX_GEVSTRING_LENGTH = 64
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 401
try:
    GEV_FRAME_STATUS_RECVD = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 402
try:
    GEV_FRAME_STATUS_PENDING = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 403
try:
    GEV_FRAME_STATUS_TIMEOUT = 2
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 404
try:
    GEV_FRAME_STATUS_OVERFLOW = 3
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 405
try:
    GEV_FRAME_STATUS_BANDWIDTH = 4
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 406
try:
    GEV_FRAME_STATUS_LOST = 5
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 407
try:
    GEV_FRAME_STATUS_RELEASED = (-1)
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 517
try:
    GENAPI_UNUSED_TYPE = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 518
try:
    GENAPI_VALUE_TYPE = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 519
try:
    GENAPI_BASE_TYPE = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 520
try:
    GENAPI_INTEGER_TYPE = 2
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 521
try:
    GENAPI_BOOLEAN_TYPE = 3
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 522
try:
    GENAPI_COMMAND_TYPE = 4
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 523
try:
    GENAPI_FLOAT_TYPE = 5
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 524
try:
    GENAPI_STRING_TYPE = 6
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 525
try:
    GENAPI_REGISTER_TYPE = 7
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 526
try:
    GENAPI_CATEGORY_TYPE = 8
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 527
try:
    GENAPI_ENUM_TYPE = 9
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 528
try:
    GENAPI_ENUMENTRY_TYPE = 10
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 531
try:
    GENAPI_ACCESSMODE_NI = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 532
try:
    GENAPI_ACCESSMODE_NA = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 533
try:
    GENAPI_ACCESSMODE_WO = 2
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 534
try:
    GENAPI_ACCESSMODE_RO = 3
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 535
try:
    GENAPI_ACCESSMODE_RW = 4
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 536
try:
    GENAPI_ACCESSMODE_NONE = 5
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 539
try:
    GENAPI_VISIBILITY_BEGINNER = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 540
try:
    GENAPI_VISIBILITY_EXPERT = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 541
try:
    GENAPI_VISIBILITY_GURU = 2
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 542
try:
    GENAPI_VISIBILITY_INVISIBLE = 3
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 543
try:
    GENAPI_VISIBILITY_UNDEFINED = 99
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 546
try:
    GENAPI_INCREMENT_NONE = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 547
try:
    GENAPI_INCREMENT_FIXED = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 548
try:
    GENAPI_INCREMENT_LIST = 2
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 644
try:
    GevFreeImageTransfer = GevFreeTransfer
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 645
try:
    GevStartImageTransfer = GevStartTransfer
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 646
try:
    GevStopImageTransfer = GevStopTransfer
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 647
try:
    GevAbortImageTransfer = GevAbortTransfer
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 648
try:
    GevQueryImageTransferStatus = GevQueryTransferStatus
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 657
try:
    GevGetNextImage = GevGetNextFrame
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 658
try:
    GevWaitForNextImage = GevWaitForNextFrame
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 659
try:
    GevReleaseImage = GevReleaseFrame
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 660
try:
    GevReleaseImageBuffer = GevReleaseFrameBuffer
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 674
try:
    BAYER_ALIGN_GB_RG = 0
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 675
try:
    BAYER_ALIGN_BG_GR = 1
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 676
try:
    BAYER_ALIGN_RG_GB = 2
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 677
try:
    BAYER_ALIGN_GR_BG = 3
except:
    pass

# /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 679
try:
    BAYER_CONVERSION_2X2 = 0
except:
    pass

_tag_GEVBUF_ENTRY = struct__tag_GEVBUF_ENTRY # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 399

_GEVBUF_QUEUE = struct__GEVBUF_QUEUE # /home/david/GigE-V-Framework_2.10.0.0157/DALSA/GigeV/include/gevapi.h: 438

# No inserted files

