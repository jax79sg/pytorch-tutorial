mkdir data
apt update && apt install -y axel 
axel -n 15 -a -o ./data http://msvocds.blob.core.windows.net/annotations-1-0-3/captions_train-val2014.zip
axel -n 15 -a -o ./data http://images.cocodataset.org/zips/train2014.zip
axel -n 15 -a -o ./data http://images.cocodataset.org/zips/val2014.zip

unzip ./data/captions_train-val2014.zip -d ./data/
rm ./data/captions_train-val2014.zip
unzip ./data/train2014.zip -d ./data/
rm ./data/train2014.zip 
unzip ./data/val2014.zip -d ./data/ 
rm ./data/val2014.zip 

exec(open("build_vocab.py").read())
exec(open("resize.py").read())
exec(open("train.py").read())
