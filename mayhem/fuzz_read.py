#!/usr/bin/python3
import atheris
import logging
import sys
import io
with atheris.instrument_imports():
    import soundfile

# No logging
logging.disable(logging.CRITICAL)


@atheris.instrument_func
def TestOneInput(data):
    # Get BytesIO file containing data
    try:
        data, samplerate = soundfile.read(io.BytesIO(data))
    except soundfile.SoundFileError:
        pass


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
