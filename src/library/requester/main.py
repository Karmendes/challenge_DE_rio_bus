from requests import Session
from retry_requests import retry

from src.library.logger.main import Logger

RETRY_CODES=(429,408,504,503,500)

def raise_trace(resp, *args, **kwargs):
    Logger.emit(f"raise_trace: {resp} - {args} - {kwargs}", Logger.DEBUG)
    resp.raise_for_status()

class Request:
    def __init__(self, headers, *, retries:int=2, status_to_retry:tuple=RETRY_CODES, backoff_factor:int=2):
        session = retry(Session(), retries=retries, backoff_factor=backoff_factor, status_to_retry=status_to_retry)
        session.headers.update(**headers)
        session.hooks = {
                        'response': lambda r, *args, **kwargs: raise_trace(r),
                        }
        self.session = session
        self.headers = headers
    def get(self, url, **params):
        Logger.emit(f'HTTP GET: {url}', Logger.DEBUG)
        Logger.emit(f'Params: {params}', Logger.DEBUG)
        return self.session.get(url, **params)