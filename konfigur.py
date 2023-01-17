#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
import sys

class log:
    _level = { "INFO" : True, "WARNING" : True, "ERROR" : True }
    _stdout = []
    _stderr = []
    def l(stdout, stderr):
        stdout = stdout if isinstance(stdout, list) else [stdout]
        stderr = stderr if isinstance(stderr, list) else [stderr]
        log._stdout = log._stdout + stdout
        log._stderr = log._stderr + stderr

    def p(msg, prefix = ""):
        _msg = ("" if prefix == "" else "[" + prefix + "] ") + msg
        log.l(_msg, _msg)
        if len(prefix) > 0 and log._level[prefix]:
            print(_msg)

    def i(msg, prefix="INFO"):
        log.p(msg, prefix)

    def w(msg, prefix="WARNING"):
        log.p(msg, prefix)

    def e(msg, prefix="ERROR"):
        log.p(msg, prefix)

    def print():
        print("########## STDOUT ##########")
        for l in log._stdout:
            print(l)
        print("########## STDERR ##########")
        for l in log._stderr:
            print(l)


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', metavar="FORMAT", help="get date-time", nargs='?', type=str, required=False, const="<none>")
    parser.add_argument('--desktop', help="generate desktop image", action='store_true', required=False)
    return parser.parse_args()


def _run(cmd, asRoot = False):
    _prompt = "# " if asRoot else "$ "
    log.i(_prompt + " ".join(cmd))
    return subprocess.run(cmd, capture_output=True, encoding="utf-8")


def _run_batch(cmds, asRoot = False, strict = False):
    for i, cmd in enumerate(cmds):
        wasError = False
        try:
            output = _run(cmd, asRoot)
            sys.stdout.flush()
            if output.returncode != 0:
                wasError = True
                _errMsg = "The '" + " ".join(cmd) + "' command return: " + str(output.returncode)
                log.e(_errMsg)
            log.l(output.stdout.split(sep="\n"), output.stderr.split(sep="\n"))
        except Exception as inst:
            wasError = True
            _errMsg = "Something went wrong when run: '" + " ".join(cmd) + "'."
            log.e(_errMsg)
            log.l(inst, inst)
        finally:
            if strict and wasError:
                for c in cmds[i:]:
                    _errMsg = "The '" + " ".join(c) + "' not run!"
                    log.e(_errMsg)
                return False
    return True

def _run_parallel(cmds, asRoot = False):
    pass


def apt_install(apps, yes="-y"):
    _apt = ["sudo", "apt", yes] + apps
    _run(_apt)


def pip_install(packages):
    _pip = ["pip", "install"] + packages
    _run(_pip)

_APPS = {
    "basic editors" : [
        "gedit",
        "cmake",
        "qtcreator"
    ],
    "GNOME" : [
        "gnome-tweaks",
        "gnome-clocks",
        "gnome-shell-extensions",
        "chrome-gnome-shell"
    ]
}
def install_all_apps(args):
    for key, value in _APPS.items():
        _run_batch(value)
    return
    _apps = ["gedit", "cmake", "qtcreator"]
    apt_install(_apps)
    _apps = ["gnome-tweaks", "gnome-clocks", "gnome-shell-extensions", "chrome-gnome-shell"]
    apt_install(_apps)
    _apps = ["gimp", "kolourpaint", "eog", "vlc"]
    apt_install(_apps)
    _apps = ["texlive-full"]
    apt_install(_apps)
    _apps = ["gparted", "htop"]
    apt_install(_apps)
    _apps = ["openjdk-11-jdk", "scrcpy"]
    apt_install(_apps)
    _apps = ["gir1.2-gtop-2.0", "gir1.2-nm-1.0", "gir1.2-clutter-1.0", "gnome-system-monitor"]
    apt_install(_apps)
    _apps = ["git-lfs", "screen", "wine"]
    apt_install(_apps)


def pip_all_packages(args):
    _mat_packages = ["numpy", "matplotlib"]
    pip_install(_mat_packages)
    _astro_packages = ["astropy", "astroquery", "astroplan", "pytest-astropy"]
    pip_install(_astro_packages)


def install_google_chrome(args):
    _download = ["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"]
    _run(_download)
    _install = ["sudo", "dpkg", "-i", "google-chrome-stable_current_amd64.deb"]
    _run(_install)
    _fix = ["sudo", "apt-get", "install", "-f"]
    _run(_fix)




if __name__ == '__main__':
    args = parseArgs()
    _run_batch([["ls"], ["ls", "Q"], ["ls", "-la"]])
    log.p("   ***   ")
    _run_batch([["ls"], ["ls", "Q"], ["ls", "-la"]], strict=True)
    log.p("   ***   ")
    _run_batch([["ls"], ["cd", "Q"], ["ls", "-la"]], strict=True)
    log.print()
    #install_all_apps(args)
    #pip_all_packages(args)
