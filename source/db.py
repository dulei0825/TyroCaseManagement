import sqlite3 as sql


class DB:
    def __init__(self):
        self.__dbfile = '..\resource\db.sqlite3'
        self.__dbconnection = None
        self.__dbcursor = None

    def __connect(self):
        self.__dbconnection = sql.connect(self.__dbfile)
        self.__dbcursor = self.__dbconnection.cursor()

    def __disconnect(self):
        self.__dbcursor.close()
        self.__dbconnection.close()

    def __parserargs(self, *arg, **kwargs):
        pass

    def get_summary_info(self):
        """
        返回表信息，不返回记录内容
        （总记录条数， 最后一条记录的Incident字段， 返回最后一条记录的Client Ref字段， 最后一条记录的Opened字段）
        :return:(counts(int), incident(string), clientref(string), opened(string))
        """
        pass

    def get_summary_records(self, *arg, **kwargs):
        """
        返回记录查询结果
        :param arg:
        :param kwargs:
        :return: records(tuple)
        """
        pass

    def set_summary_withfield(self, fieldname, fieldvalue):
        """
        插入单体记录
        :param fieldname: tuple
        :param fieldvalue: tuple
        :return:
        """

    def set_summary_withvalue(self, fieldvalue):
        """
        插入单条记录
        :param fieldvalue: tuple
        :return:
        """

