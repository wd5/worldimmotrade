# -*- coding: utf-8 -*-
class urlGen:

    """
        REVISION: 1.0
        AUTHOR: NICKOLAS WHITING

        Build a URL QuerString based on given uri, param
        to add current querystring for a URL

        param: Parameter to add to querystring

        uri: Dictionary of current querystring Params | Accepts django's request.GET

        Usage Example

        Add a current URI param and remove if it exists

        uri = urlGen()

        Current URI: ?page=1&search=nick
        uri.urlgen('page', request.GET)
        Outputs: ?search=nick&page=

        Add a uri Param and exclude a current

        Current URI: ?search=nick&page=2
        urlgen('order', request.GET, ['page',])
        Outputs: ?search=nick&order=


    """

    def generate(self, param, uri = {}, exclude = []):
        self.param = param
        self.uri = uri
        self.exclude = exclude

        self.querystring = False

        """
        BUG FIX:

        Append param to exclude to ensure the param
        Doesnt get added twice to URI

        """
        exclude.append(param)

        # Add the URI Param if it is the only one given

        if len(self.uri) == 0:
            try:
                self.appendQuerystring(self.param)
            except ExceptionError:
                raise ExceptionError (
                    'urlgen recieved an unexpected error adding %s param failed' % (params)
                    )
        else:
            for k,v in self.uri.iteritems():
                if self.param is not str(k) and k not in self.exclude:
                    self.appendQuerystring(k, v)

            # Append the param to end of URL

            self.appendQuerystring(self.param)

        return self.querystring

    def appendQuerystring(self, param, value = False):

        """
        Appends a param to the current querystring
        """
        try:
            param = str(param.encode('ascii', 'ignore'))

            if self.querystring is False:
                if value is False:
                    self.querystring = '?%s=' % (param)
                else:
                    self.querystring = '?%s=%s' % (param, value)
            else:
                if value is False:
                    self.querystring  = '%s&%s=' % (self.querystring, param)
                else:
                    self.querystring  = '%s&%s=%s' % (self.querystring, param, value)
        except:
            pass
