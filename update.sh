unset http_proxy;
unset https_proxy;
git pull origin master
git add .;
git commit -m "update script";
git push origin master