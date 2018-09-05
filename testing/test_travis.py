import os


def test():
    from xdist.plugin import auto_detect_cpus

    print("AUTODETECT", auto_detect_cpus())
    print("TRAVIS=", os.environ["TRAVIS"])
    assert False
