from sqlalchemy import create_engine


class DBConnector:
    class Postgres:
        @staticmethod
        def get_postgres_client(db_conn_details):
            connection_string_pareto = 'postgres://%(db_user)s:%(db_password)s@%(host)s/%(db_name)s' % db_conn_details
            engine = create_engine(connection_string_pareto)
            return engine
