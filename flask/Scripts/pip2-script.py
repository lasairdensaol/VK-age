#!"C:\Program Files (x86)\microblog-0.1\flask\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==7.1.2','console_scripts','pip2'
__requires__ = 'pip==7.1.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pip==7.1.2', 'console_scripts', 'pip2')()
    )
