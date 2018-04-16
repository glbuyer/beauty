curl \
-H 'Content-Type: application/json' \
-XPOST 'http://localhost:3000' \
-d '
{
  "image_file" : "/root/beauty/data/xiaojie_1.jpg"
}
'

curl \
-H 'Content-Type: application/json' \
-XPOST 'http://localhost:3000' \
-d '
{
  "image_file" : "/Users/xiaojiew1/Projects/beauty/data/xiaojie_1.jpg"
}
'

curl \
-H 'Content-Type: application/json' \
-XPOST 'http://localhost:3000' \
-d '
{
  "image_file" : "/Users/xiaojiew1/Projects/beauty/data/img_2434.jpg"
}
'


scp data/xiaojie_1.jpg root@47.91.47.47:/root/beauty/data
scp data/xiaojie_2.jpg root@47.91.47.47:/root/beauty/data
scp data/star_encoding.p root@47.91.47.47:/root/beauty/data

