from __future__ import absolute_import
import warnings


def random_user_agent():
    from user_agent import generate_user_agent
    warnings.warn('Funcion `user_agent::random_user_agent` is deprecated'
                  ' Use `user_agent` package instead (`pip install user_agent`)')
    return generate_user_agent()
