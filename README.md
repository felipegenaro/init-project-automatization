For this project you need to have installed `cask` and the python package `selenium`.

If you dont't have them, please install:

```bash
$ brew cask install chromium
```

```bash	
$ pip3 install selenium
```

In your zshrc, bashrc_profile or correlated, don’t forget to 

```bash
$ source ~/.extra_zsh_commands
```

```bash
$ initProject <language/folder1> <projectName/folder2> <git>
```

The git argument is optional. To use this argument remember to fill up your git credentials


Example:

```bash
$ initProject js myNodeProject git
```

This will create a folder in `/Documents/Projects/javascript/myNodeProject`
and will create a git repository with the first commit
