if [ -e ./src ]; then
  rm -rf ./src
fi
mkdir ./src
git clone https://github.com/titabash/python-clean-architecture-template.git ./src
rm -rf ./src/.git
rm -rf ./src/.gitignore
