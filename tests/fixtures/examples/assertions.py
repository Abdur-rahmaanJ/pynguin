#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2020 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#
from typing import Union

static_state = 0


class Human:
    def __init__(self, name: str, number: Union[int, float]) -> None:
        self._name = name
        self._number = number

    def __str__(self):
        return super().__str__()

    def get_name(self) -> str:
        return self._name

    def get_number(self) -> Union[int, float]:
        return self._number

    def static_state(self) -> float:
        global static_state
        static_state += 1
        return static_state * self._number
