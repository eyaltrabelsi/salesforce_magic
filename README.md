# salesforce_magic

Introduces a %%salesforce magic.
Connect to a salesforce, using beatbox and then issue SQL commands within IPython or IPython Notebook.


# Installing

-   From Source:
    1. download from https://github.com/eyaltrabelsi/salesforce_magic
    2. cd jupyter-salesforce
    3. python setup.py install

-   Using pip install:
    pip install git+https://github.com/eyaltrabelsi/salesforce_magic

# Usage

    In [1]: %load_ext salesforce_magic
    In [2]: %%salesforce user,password,security_token
            select id from account
   
# Existing Issues:
- Long queries and salesforce time out

![](https://github.com/eyaltrabelsi/salesforce_magic/blob/master/salesforce-y-u-no-work.jpg.png)
