from pathlib import Path


def path(file_name):
  return  str((Path(__file__).resolve().parents[1] / 'tests' / 'resources' / file_name).absolute())