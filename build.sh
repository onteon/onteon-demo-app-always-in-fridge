#!/usr/bin/env bash

set -e

SOURCE=${BASH_SOURCE[0]}
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
  SOURCE=$(readlink "$SOURCE")
  [[ $SOURCE != /* ]] && SOURCE=$DIR/$SOURCE # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )

rm -rf "${DIR}/target/"
mkdir -p "${DIR}/target/tar/bin/"
mkdir -p "${DIR}/target/tar/conf/"

cp "${DIR}/main.py" "${DIR}/target/tar/bin/"
cp "${DIR}/bin/"* "${DIR}/target/tar/bin/"
cp "${DIR}/conf.yml" "${DIR}/target/tar/conf/"
cp "${DIR}/conf.yml" "${DIR}/target/tar/conf/"

cd "${DIR}/target/tar" && tar -zcvf "${DIR}/target/onteon-demo-app-always-in-fridge-native.tar.gz" *
