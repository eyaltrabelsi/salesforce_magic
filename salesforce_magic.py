import itertools
import beatbox
import pandas as pd


def query_salesforce(line, query=''):
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


class Salesforce(object):
    def __init__(self, user_name, password, security_token):
        """Constructor for salesforce api which open session with salesforce with given credentials
           Args: * user_name: salesforce user
                 * password: salesforce password
                 * security_token: salesforcesecurity_token """

        self.sf = beatbox._tPartnerNS
        self.svc = beatbox.Client()
        self.svc.login(user_name, password + security_token)

    def __get_query_results(self, is_actual_query, rest_of_query, deleted_included=False):
        """ Function to call the salesforce API given the calculated query
            Args: * is_actual_query: query to be sent to the api
                  * rest_of_query: if is_actual_query=true its the query string else its the continuation of
                                   the query given in iteration before
                  * deleted_included: should the query bring records from recycle bin (http://spanning.com/blog/what-you-need-to-know-about-salesforces-recycle-bin/)
            Returns: * res_[self.sf.records:] which represent list of the salesforce results and columns
                     * res_.done[0]  which indicates if there are more records which wasnt fetched for this specific query
                     * res_.queryLocator[0]= the query locator to be sent to this function in the next page"""

        if is_actual_query:
            res_ = self.svc.query(rest_of_query) if deleted_included else self.svc.queryAll(rest_of_query)
        else:
            res_ = self.svc.queryMore(rest_of_query)
        return res_[self.sf.records:], \
               res_.done[0] if hasattr(res_, 'done') else True, \
               res_.queryLocator[0] if res_.queryLocator else None

    @staticmethod
    def get_columns_names(row):
        return [str(col._name[1].lower()) for col in row[2:]]

    @staticmethod
    def get_columns_values(row):
        return [str(col) for col in row[2:]]

    def query(self, query, deleted_included=False):
        """ Function to call the salesforce API given the calculated query
            Args: * query: a given query for salesforce (https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select.htm)d
                  * deleted_included: should the query bring records from recycle bin (http://spanning.com/blog/what-you-need-to-know-about-salesforces-recycle-bin/)
            Returns: Dataframe with results from the given query"""

        res, done, header = [], 'false', []
        rest_of_query = query

        for i in itertools.takewhile(lambda c: done == 'false', itertools.count()):
            first_iteration = i == 0

            sf_results, done, rest_of_query = self.__get_query_results(first_iteration, \
                                                                       rest_of_query, \
                                                                       deleted_included)
            normalized_sf_results = [self.get_columns_values(row) for row in sf_results]
            res.extend(normalized_sf_results)

            if first_iteration and sf_results:
                header = self.get_columns_names(sf_results[0])
        return pd.DataFrame(res, columns=header)


def load_ipython_extension(ipython):
    ipython.register_magic_function(query_salesforce, 'cell', 'salesforce')
