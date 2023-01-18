#!/bin/bash

echo "INLUDED"
rm stdout.log stderr.log s.log e.log 2> /dev/null
function _B (){ echo -n ""; }
function _A (){ _e=$?; if [ "$_e" -ne 0 ]; then echo -e "[ \033[0;31mERR\033[0m=$_e ] \$ ${@}"; cat s.log; cat e.log; else echo -e "[ \033[0;32mOK\033[0m ] \$ ${@}"; fi; rm s.log e.log 2> /dev/null; }
function _S () { _B "sudo ${@}"; sudo "${@}" > >(tee -a stdout.log) >s.log 2> >(tee -a stderr.log >&2) 2>e.log ; _A "sudo ${@}"; }
function _C () { _B "${@}"; eval "${@}" > >(tee -a stdout.log) >s.log 2> >(tee -a stderr.log >&2) 2>e.log ; _A "${@}"; }

_INFO=0
function logi () {}
