if [ -e ./src ]; then
  rm -rf ./src
fi
if [ -e ./tests ]; then
  rm -rf ./tests
fi
mkdir ./src
git clone --filter=blob:none --sparse https://github.com/titabash/python-clean-architecture-template.git ./
git sparse-checkout set src
git sparse-checkout set tests
rm -rf ./src/.git
