# ipython-salesforce

Introduces a %%salesforce magic.
Connect to a salesforce, using beatbox and then issue SQL commands within IPython or IPython Notebook.

![](https://github.com/eyaltrabelsi/ipython-salesforce/blob/master/salesforce-y-u-no-work.jpg.png)

# Installing


Install the lastest release with:<br/>
    
    pip install ipython-sql 

or download from https://github.com/eyaltrabelsi/ipython-salesforce and:<br/>

    cd ipython-sql;
    sudo python setup.py install;

    
Examples
--------

    In [1]: %load_ext sql
    In [2]: %%sql postgresql://will:longliveliz@localhost/shakes
            select id from task
    In [3]: result = _
    In [4]: print(result)
   
   

