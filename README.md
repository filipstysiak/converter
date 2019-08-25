# Running the app

To run the app install it with docker. Run
```
docker build -t converter:latest .
```
in the project's directory to build the image, and then run

```
sudo docker run -d --network host converter
```
to run the image. The app uses port 4000 by default (since it's a pretty simple example it's configurable by editing
the ```config.py``` file). Alternatively you can run

```
sudo docker run -d -p local_port:application_port converter
```

and then retrieve the IP address of the container using

```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name
```

to retrieve the container's address.

# Implementation

This simple app is created with Flask framework. It has only one point of entry ('/convert/'), therefore to keep the
app simple it adds it's only method via @app.route annotation.

The method validates the POST request body (a JSON object) and then uses an external API to retrieve the list of
currency rates. The API is available [HERE](https://exchangeratesapi.io/).

The multiplication of the desired rate of exchange with the given value is done with the help of `money` package
(the data type used is Decimal).

Tests check for the validity of the JSON object. The testing framework of choice is pytest. The JSON validation is done
with the use of `flask-marshmallow` package.