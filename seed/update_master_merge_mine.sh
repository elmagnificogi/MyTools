git checkout master
git fetch upstream
git merge upstream/master
git push origin master
git checkout mine
git merge master
exec /bin/bash