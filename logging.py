import logging

logger = logging.getLogger(__name__)

stream_h = logging.StreamHandler()
file_h \ logging.FileHandler('file.log')

stram_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

stream_f = logging.Formatter()

