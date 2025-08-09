#!/usr/bin/bash
# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.

python3 _manage.py migrate
python3 _manage.py loaddata fixtures/easter.json
