#!/usr/bin/env python3
# Copyright 2025 yanks
# See LICENSE file for licensing details.

"""FastAPI Charm entrypoint."""

import logging
import typing

import ops

import paas_charm.fastapi

logger = logging.getLogger(__name__)


class FastapiHelloWorldCharm(paas_charm.fastapi.Charm):
    """FastAPI Charm service."""

    def __init__(self, *args: typing.Any) -> None:
        """Initialize the instance.

        Args:
            args: passthrough to CharmBase.
        """
        super().__init__(*args)


if __name__ == "__main__":
    ops.main(FastapiHelloWorldCharm)
