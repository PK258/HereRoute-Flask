# -*- coding: utf-8 -*-
#!/usr/bin/env bash

mysql_ConnectionString = 'mssql+pyodbc://{uid}:{password}@{server}:1433/{database}?driver={driver}'.format(
    uid='sa-digital-cloud-two',
    password='ERTYsoc123',
    server='digital-cloud-two.database.windows.net',
    database='Digital_Cloud_Two_SQL',
    driver='SQL+Server')


FromID_query = """
            SELECT id
                FROM open_data.here_routing_analytics_ref
                WHERE country = ? and
                    city = ? and
                    railwaystation = ? and
                    usage_origin_traffic = 'active' and
                    direction = ? and
                    distance = ?;
        """

ToID_query = """
            SELECT id
                FROM open_data.here_routing_analytics_ref
                WHERE country = ? and
                    city = ? and
                    railwaystation = ? and
                    direction = ? and
                    distance = ?;
        """

FetchData_query = """
                SELECT time_rounded, duration, distance from open_data.here_routing_analytics_optimized
                WHERE origin_id = ? and 
                        destination_id =?;
                """


