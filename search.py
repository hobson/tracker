#!/usr/bin/env python
from sys import stdout
import gi
from gi.repository import Tracker


def wait_for_results(query_str, N=3, verbosity=1):
    conn = Tracker.SparqlConnection.get(None)
    cursor = conn.query(query_str, None)

    results = []
    while (len(results < N) and cursor.next(None)):
        results += [cursor.get_string(0)]
        if verbosity:
            stdout.write(results[-1] + '\n')


if __name__ == "__main__":
    exit(0)
    from sys import argv
    if len(argv) > 1:
        search_terms = argv[1:]
    query_str = "SELECT nie:url(?f) WHERE { ?f fts:match '%s' }" % ' '.join(search_terms)
