#!/bin/bash
echo "Content-Type: application/javascript"
echo

CACHE_FILE=/tmp/sbk.full_table.cgi.cache
TTL=60

function refresh_cache() {
  ./full_table.py | tr -d '\n' >$CACHE_FILE
}

function get_the_goods() {
  ./full_table.py | tr -d '\n'
#  if [[ -e $CACHE_FILE ]]; then
#    age=$(( $(date +%s) - $(stat -c "%Y" $CACHE_FILE) ))
#    if [[ $age -gt $TTL ]]; then
#      refresh_cache
#    fi
#  else
#    refresh_cache
#  fi
#  cat $CACHE_FILE
}

printf "full_table(%s);" "$(get_the_goods)"
echo
