# coding=utf-8


class BassError(Exception):
    def __init__(self, value=""):
        self.message = value

    def __repr__(self):
        return repr(self.message)


class NoFoundElement(BassError):
    pass


class NoFoundTargetImage(BassError):
    pass


class ElementInputError(BassError):
    pass


class AssertFailError(BassError):
    pass


class TimeOutError(BassError):
    pass
