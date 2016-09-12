#!/bin/bash
echo "Content-Type: application/javascript"
echo

function get_the_goods() {
  ./terms_data.py | tr -d '\n'
}

printf "terms_data(%s);" "$(get_the_goods)"
echo
