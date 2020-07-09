Setup a new documentation repository
====================================


Setup github repo with sphinx 
-----------------------------

0. create github repo
    
        https://help.github.com/en/github/getting-started-with-github/create-a-repo
        
1. setup sphinx in repo => config general info => should build::
    
        pip3 install sphinx==2.2.0
        
        sphinx-quickstart
        # fill in "Project name" and "Author name(s)"
        # for the question "> Separate source and build directories (y/n)" Answer: y
        # but for the other questions just press enter for the default value 
        
  
Config sphinx for  continuous_publishing 
-----------------------------------------

2. load continuous_publishing.py in conf.py::

      cd source/
      curl -O https://raw.githubusercontent.com/harcokuppens/continuous_publishing/master/source/continuous_publishing.py 
      cd - 
   
   then add to end of conf.py file::
   
      # -- Load Continuous publishing configuration ---------------------------------------------------

      includefile='continuous_publishing.py'
      exec(compile(source=open(includefile).read(), filename=includefile, mode='exec'))
   
3. config continuous_publishing.py : fill in config values in first section to setup github for cont. publishing::
  
 
4. set tool version in  TOOLVERSION.txt and add "sphinx-rtd-theme" python package as requirement for sphinx::

     TOOLVERSION=...     
     cd source      
     echo $TOOLVERSION > TOOLVERSION.txt  
     cd - 
     echo "sphinx-rtd-theme" > requirements.txt 
     git add .
     git commit -m'setup sphinx with continuous publishing'
    
Setup github actions for  continuous_publishing sphinx website and pdf on github 
----------------------------------------------------------------------------------

5. create orphan branch for gh-pages::
      
       WEBSITE_BRANCH=gh-pages
       git checkout --orphan $WEBSITE_BRANCH
       git rm -rf -q .
       # git only makes dirs empty, but leaves them in the working directory. Also removes these:
       rm -rf *
       printf 'Documentation:\n<li><a href="stable">stable</a></li>\n<li><a href="latest">latest</a></li>\n' > index.html
       touch .nojekyll 
       git add index.html
       git add .nojekyll  
       git commit -m "Adding index.html file to stable and latest documentation"     
       git push -u origin $WEBSITE_BRANCH

6. add workflow files in master branch::

       git checkout master
       mkdir .github
       mkdir .github/workflows
       cd .github/workflows
       curl -O https://raw.githubusercontent.com/harcokuppens/continuous_publishing/master/.github/workflows/continous_publishing_latest.yml
       curl -O https://raw.githubusercontent.com/harcokuppens/continuous_publishing/master/.github/workflows/continous_publishing_stable.yml 
       cd -
       git add .github 
       git commit -am "added workflows"
       git push
       # the first latest build will be build for your new repository; see its releases page



