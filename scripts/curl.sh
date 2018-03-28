curl \
-H 'Content-Type: application/json' \
-XPOST 'http://localhost:3000' \
-d '
{
  "image_file" : "/Users/xiaojiew1/Projects/beauty/data/250.jpg",
  "image_url": ""
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
