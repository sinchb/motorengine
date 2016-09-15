
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from motorengine.query.base import QueryOperator


class RegxQueryOperator(QueryOperator):
    '''
    Query operator used to return all documents that have the specified field with a value greater than the specified value.

    For more information on `$regx` go to https://docs.mongodb.com/manual/reference/operator/query/regex.

    '''

    def to_query(self, field_name, value):
        return {
            field_name: {"$regex": value}
        }
