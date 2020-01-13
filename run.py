#!/usr/bin/env python
import os
import config

from app import app

if __name__ == '__main__':
    port = config.PORT
    app.run('0.0.0.0', port=port, debug=True)
