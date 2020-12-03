
if [[ $SHELL == */zsh ]]
then
    local projects_file=$(pwd)/projects.sh

    local cmd="source $projects_file"

    echo -e "# Project Navigation\n$cmd" >> ~/.zshrc
    echo "Added to start-up script."
else
    echo "Scripts only work with zsh shell."
fi
