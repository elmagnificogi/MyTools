export http_proxy="127.0.0.1:1081" 
export https_proxy="127.0.0.1:1081"
git pull origin master
git add .;
git commit -m "update script";
git push origin master