if [[ $SHELL == */zsh ]]
then
    local projects_file=$HOME/.nav/make_alias.sh

    local cmd="source $projects_file"

    echo -e "# Project Navigation\n$cmd" >> ~/.zshrc
    echo "Added to sourcing file to start-up script."

    pip install .
else
    echo "Scripts only work with zsh shell."
fi
