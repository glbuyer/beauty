curl \
-H 'Content-Type: application/json' \
-XPOST 'http://localhost:3000' \
-d '
{
  "image_file" : "/root/beauty/data/xiaojie.jpg"
}
'

curl \
-H 'Content-Type: application/json' \
-XPOST 'http://localhost:3000' \
-d '
{
  "image_file" : "/Users/xiaojiew1/Projects/beauty/data/error.jpg",
  "image_url": ""
}
'