import logging

from dotenv import load_dotenv

from app.logger import INFOFORMATTER, \
                           DEBUGFORMATTER

load_dotenv('./app/app.env')

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


_sh = logging.StreamHandler()
_sh.setLevel(logging.INFO)
_sh.setFormatter(logging.Formatter(INFOFORMATTER))
log.addHandler(_sh)

_sh_dbg = logging.StreamHandler()
_sh_dbg.setLevel(logging.DEBUG)
_sh_dbg.setFormatter(logging.Formatter(DEBUGFORMATTER))
log.addHandler(_sh_dbg)

_fh = logging.FileHandler("app.log", mode='a')    
_fh.setLevel(logging.DEBUG)
_fh.setFormatter(logging.Formatter(DEBUGFORMATTER))
log.addHandler(_fh)