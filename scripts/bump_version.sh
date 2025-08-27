#! /bin/bash

valid_commands=('major' 'minor' 'patch')

valid_command=false
for value in "${valid_commands[@]}"
do
    if [[ $1 == $value ]]; then
        command=$1
        valid_command=true
    fi
done

if ! $valid_command; then
    cat << EOF
No valid command: '$1'
Valid commands are 'major' 'minor' 'patch'
EOF
    exit 1
fi

old_version=`uv version | awk '{print $2}'`

uv version --quiet --bump $1

new_version=`uv version | awk '{print $2}'`

echo "Bump ruff version from $old_version to $new_version"

sed -i "s/ruff~=${old_version}/ruff~=${new_version}/g" pyproject.toml
sed -i "s/rev: 'v${old_version}'/rev: 'v${new_version}'/g" .pre-commit-config.yaml

pre-commit install
git add . && git commit --quiet -m "Ruff v${new_version}" && git tag "v${new_version}"
