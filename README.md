===========
ipython-sql
===========

:Author: Catherine Devlin, http://catherinedevlin.blogspot.com

Introduces a %sql (or %%sql) magic.

Connect to a database, using SQLAlchemy connect strings, then issue SQL
commands within IPython or IPython Notebook.

.. image:: https://raw.github.com/catherinedevlin/ipython-sql/master/examples/writers.png
   :width: 600px
   :alt: screenshot of ipython-sql in the Notebook

Examples
--------

.. code-block:: python

    In [1]: %load_ext sql

    In [2]: %%sql postgresql://will:longliveliz@localhost/shakes
       ...: select * from character
       ...: where abbrev = 'ALICE'
       ...:
    Out[2]: [(u'Alice', u'Alice', u'ALICE', u'a lady attending on Princess Katherine', 22)]

    In [3]: result = _

    In [4]: print(result)
    charid   charname   abbrev                description                 speechcount
    =================================================================================
    Alice    Alice      ALICE    a lady attending on Princess Katherine   22

    In [4]: result.keys
    Out[5]: [u'charid', u'charname', u'abbrev', u'description', u'speechcount']

    In [6]: result[0][0]
    Out[6]: u'Alice'

    In [7]: result[0].description
    Out[7]: u'a lady attending on Princess Katherine'

After the first connection, connect info can be omitted::

    In [8]: %sql select count(*) from work
    Out[8]: [(43L,)]

Connecting
----------

Connection strings are `SQLAlchemy`_ standard.

Some example connection strings::

    mysql+pymysql://scott:tiger@localhost/foo
    oracle://scott:tiger@127.0.0.1:1521/sidname
    sqlite://
    sqlite:///foo.db

.. _SQLAlchemy: http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls

Note that ``mysql`` and ``mysql+pymysql`` connections (and perhaps others)
don't read your client character set information from .my.cnf.  You need
to specify it in the connection string::

    mysql+pymysql://scott:tiger@localhost/foo?charset=utf8


Graphing
--------

If you have installed ``matplotlib``, you can use a result set's
``.plot()``, ``.pie()``, and ``.bar()`` methods for quick plotting

.. code-block:: python

    In[5]: result = %sql SELECT title, totalwords FROM work WHERE genretype = 'c'

    In[6]: %matplotlib inline

    In[7]: result.pie()

.. image:: https://raw.github.com/catherinedevlin/ipython-sql/master/examples/wordcount.png
   :alt: pie chart of word count of Shakespeare's comedies



Installing
----------

Install the lastest release with::

    pip install ipython-sql

or download from https://github.com/catherinedevlin/ipython-sql and::

    cd ipython-sql
    sudo python setup.py install
