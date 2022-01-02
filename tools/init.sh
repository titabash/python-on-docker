CURRENT_DIR = $(pwd)
if [ -e ./project ]; then
  rm -rf ./project
fi

git clone https://github.com/titabash/python-clean-architecture-template.git ./project
cd ./project
rm -rf .git
rm -rf .gitignore
rm -rf README.md
