# copy content to gatsby folder without .obsidian
cp -r ./promised-victory ./gatsby/content/promised-victory
rm -rf ./gatsby/content/promised-victory/.obsidian

# do some shit to the content
# ...


cd ./gatsby
# build gatsby
npm install
npm run build

#build is stored in ./gatsby/public