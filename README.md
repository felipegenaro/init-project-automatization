If you not already have, please install:
$ brew cask install chromium
$ pip3 install selenium


In your zshrc, bashrc_profile or correlated, don’t forgot to 
$ source ~/.extra_zsh_commands


$ initProject <language/folder1> <projectName/folder2> <git>


The git argument is optional. For use this argument remember to fill up your git credentials


Example:

$ initProject js myNodeProject git

This will create a folder in /Documents/Projects/javascript/myNodeProject
and will create a git repository with the first commit