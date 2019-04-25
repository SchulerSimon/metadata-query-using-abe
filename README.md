# metadata-queuing-using-abe

##### this is a proof of concept, it is not designed to be used in production or enterprise context 
- this project requires charm-crypto (a python wrapper for stanford pbc elliptic curve cryptography)
	- see http://pages.cs.wisc.edu/~ace/install-charm.html

#### contents:
- ```[~repo]/prototype/``` contains a prototype to queue bit wise encoded metadata from nodes (or people) in a privacy preserving matter
- ```[~repo]/tests/``` contains tests for encoding- and decoding-speed of different ABE-Schemes
- ```[~repo]/string_encryption/``` contains a prototype for encoding strings with EEC (Elliptic Curve Cryptography). This could be very handy once the prototype is used in a more complex manner

#### requirements:
- ubuntu 18.04 LTS
- python3
- charm-crypto

### installation:
- install python3
	- https://www.python.org/downloads/
- install charm-crypto
	 -  http://pages.cs.wisc.edu/~ace/install-charm.html

#### run the prototype:

```cd [~repo]/prototype/```

```python3 pyrototype.py```

the prototype is implemented with CPabe09. Because FAME has better performance the prototype should be updated to use FAME

#### run string encoding with EEC

```cd [~repo]/string_encoding/```

```python3 concept.py```


#### run the tests:
for testing CPabe09 (slightly modified version to fit needs)
(https://jhuisi.github.io/charm/charm/schemes/abenc/abenc_waters09.html#module-abenc_waters09)

```cd [~repo]/speed_tests/cp_abe/```

```python3 test.py```

for testing FAME
(https://jhuisi.github.io/charm/charm/schemes/abenc/ac17.html#ac17.AC17CPABE)

```cd [~repo]/speed_tests/fame_abe/```

```python3 test.py```
<br>
<br>
##### notes:
If you have any questions, you are welcome to write me: schuler.simon@gmx.net
