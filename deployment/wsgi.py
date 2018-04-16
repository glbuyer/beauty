from beauty import application

# uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi
if __name__ == "__main__":
  application.run()