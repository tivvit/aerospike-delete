# Aerospike-deleter

![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)

```python
usage: delete.py [-h] [-a HOSTS [HOSTS ...]] [-p PORT] [-s SET] namespace

positional arguments:
  namespace             aerospike namespace

optional arguments:
  -h, --help            show this help message and exit
  -a HOSTS [HOSTS ...], --hosts HOSTS [HOSTS ...]
                        [localhost] list of hosts
  -p PORT, --port PORT  [3000] aerospike port
  -s SET, --set SET     aerospike set
  -t TTL, --ttl TTL     touch set with TTL
```

### TODO
* Pack for pip and deploy

### Development

Feel free to contribute.
### Copyright and License

&copy; 2015 [Vít Listík](http://tivvit.cz)

Released under [MIT licence](https://github.com/tivvit/aerospike-deleter/blob/master/LICENSE)
