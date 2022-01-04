if [ -e ./project ]; then
  read -n1 -p "Are you sure you want to permanently delete the project? (y/N): " yn
  if [[ $yn = [yY] ]]; then
    rm -rf ./project
    echo "\nProject has been deleted."
  else
    exit 0
  fi
fi

git clone https://github.com/titabash/python-clean-architecture-template.git ./project
if [[ $1 = true ]]; then
  echo "Clone the project to maintenace."
else
  cd ./project
  rm -rf .git
  rm -rf .gitignore
  rm -rf README.md
fi
