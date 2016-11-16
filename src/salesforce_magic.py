from IPython.core.magic import Magics, magics_class, cell_magic

from salesforce_api import Salesforce


@magics_class
class SalesforceMagic(Magics):
    """Runs SQL statement against a salesforce, using specified user,password and security token and beatbox.
       Provides the %%salesforce magic."""

    @cell_magic('salesforce')
    def execute(self, line, query=''):
        """Runs SQL statement against a salesforce, using specified user,password and security token and beatbox.
           If no user,password and security token has been given, an error will be raised
           Examples::
             %%salesforce user,password,security_token
             SELECT id FROM task """
        assert len(line.split(',')) == 3, 'You should specify 3 arguments:\nuser_id, password, security_token'
        user, password, security_token = line.split(',')
        sf = Salesforce(user, password, security_token)
        df = sf.query(query, deleted_included=True)
        return df


def load_ipython_extension(ip):
    ip.register_magics(SalesforceMagic)
