
if [[ $SHELL == */zsh ]]
then
    local projects_file=$(pwd)/projects.sh

    local cmd="source $projects_file"

    echo $cmd >> ~/.zshrc
    echo "Added to start-up script."
else
    echo "Scripts only work with zsh shell."
fi
