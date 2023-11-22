__all__ = ['log_request']

from datetime import datetime


def log_request(where, req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with open('log.log', 'a') as log:
        print(req.remote_addr, req.user_agent, datetime.now(), where, req.form, res, file=log, sep='|')
