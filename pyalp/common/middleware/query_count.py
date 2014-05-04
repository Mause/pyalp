from django.db import connection
from django.utils.log import getLogger

logger = getLogger(__name__)

IDENT = b'<!-- queries -->'


class QueryCountDebugMiddleware(object):
    """
    This middleware will log the number of queries run
    and the total time taken for each request (with a
    status code of 200). It does not currently support
    multi-db setups.
    """
    def process_response(self, request, response):
        if response is None:
            return None

        if response.status_code == 200:
            total_time = 0
            totals = {}

            for query in connection.queries:
                f = query['sql']

                if 'FROM' in f:
                    f = f.split('FROM')
                    # print(f, len(f))
                    f = f[1].split('"')[1]

                    *app, model = f.split('_')
                    app = '_'.join(app)

                    totals.setdefault(app, {})
                    totals[app].setdefault(model, 0)
                    totals[app][model] += 1
                else:
                    totals.setdefault('unknown_app', {})
                    totals['unknown_app'].setdefault('unknown_model', 0)
                    totals['unknown_app']['unknown_model'] += 1

                query_time = query.get('time')
                if query_time is None:
                    # django-debug-toolbar monkeypatches the connection
                    # cursor wrapper and adds extra information in each
                    # item in connection.queries. The query time is stored
                    # under the key "duration" rather than "time" and is
                    # in milliseconds, not seconds.
                    query_time = query.get('duration', 0) / 1000

                total_time += float(query_time)

            content = '{} queries taking {:.4f}s'.format(
                len(connection.queries),
                total_time
            )

            if totals:
                print()
                totals = sorted(
                    totals.items(),
                    key=lambda x: sum(x[1].values()),
                    reverse=True
                )
                for k, v in totals:
                    print('{};'.format(k))

                    v = sorted(
                        v.items(),
                        key=lambda x: x[1],
                        reverse=True
                    )
                    for sk, sv in v:
                        print('\t{} -> {}'.format(sk, sv))
                print()

            if IDENT in response.content:
                response.content = response.content.decode().replace(
                    IDENT.decode(),
                    content
                ).encode()
            else:
                logger.debug(content)

        return response
