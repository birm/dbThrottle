# dbThrottle
[![PyPI version](https://badge.fury.io/py/dbThrottle.svg)](https://badge.fury.io/py/dbThrottle)  [![Build Status](https://travis-ci.org/birm/dbThrottle.svg?branch=master)](https://travis-ci.org/birm/dbThrottle)

Python Class to run code with consideration to DB load.

## Why
Throttling code to work under the constraints of a server makes sense in certain situations, especially when replica lag comes into play. This project hopes to simplify acting on this consideration.

## What
A, still early, python module, which introduces a functional type to complete a task or continiously run an operation, taking database load and similar metrics into account.
The code will work with any metric you want to define, but we've included replia lag an open threads/connections as default metrics for mssql, mysql, postgresql, and oracle.

## Who
Ryan Birmingham, under GPL3
