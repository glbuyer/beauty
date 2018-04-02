curl \
-H 'Content-Type: application/json' \
-XPOST 'http://localhost:3000' \
-d '
{
  "image_file" : "/root/beauty/data/xiaojie_0.jpg"
}
'

curl \
-H 'Content-Type: application/json' \
-XPOST 'http://localhost:3000' \
-d '
{
  "image_file" : "/root/beauty/data/xiaojie_1.jpg"
}
'

scp root@47.91.47.47:~/