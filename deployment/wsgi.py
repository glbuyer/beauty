from beauty import server

# uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi
if __name__ == "__main__":
  server.run()