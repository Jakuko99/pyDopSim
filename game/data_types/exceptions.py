class NotEnoughSpace(Exception):
    """Selected track is full. Cannot add more trains to it."""


class TrainAlreadyOnTrack(Exception):
    """Train is already on selected track."""


class AssetNotFound(Exception):
    """Asset not found in the asset folder."""


class InvalidTrainType(Exception):
    """Invalid train type."""


class InvalidTrainNumber(Exception):
    """Invalid train number."""


class TrainTooLong(Exception):
    """Train is too long for the selected track."""


class EmptyConsist(Exception):
    """Consist is empty."""


class InvalidTrack(Exception):
    """Invalid track number."""
