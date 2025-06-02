import sys
import json
import argparse
import logging
from neo4j import GraphDatabase, basic_auth

# Configure structured logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


def execute_query(uri, username, password, query, params=None):
    """
    Establish a secure Neo4j session and execute the Cypher query.
    """
    try:
        with GraphDatabase.driver(uri, auth=basic_auth(username, password)) as driver:
            with driver.session() as session:
                result = session.run(query, parameters=params or {})
                return [record.data() for record in result]
    except Exception as e:
        logging.error(f"Query execution failed: {e}")
        sys.exit(1)


def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Enterprise-Grade Neo4j Query Runner")

    parser.add_argument("query", help="Cypher query string or path to .cql file")
    parser.add_argument("--file", action="store_true", help="Flag to read the query from a file")
    parser.add_argument("--params", default="{}", help="JSON string of query parameters")

    # Mandatory credentials
    parser.add_argument("--uri", required=True, help="Neo4j connection URI (e.g., bolt://localhost:7687)")
    parser.add_argument("--username", required=True, help="Neo4j username")
    parser.add_argument("--password", required=True, help="Neo4j password")

    return parser.parse_args()


def main():
    args = parse_arguments()

    # Load query content
    if args.file:
        try:
            with open(args.query, 'r') as file:
                query = file.read()
        except Exception as e:
            logging.error(f"Unable to read query file: {e}")
            sys.exit(1)
    else:
        query = args.query

    # Parse parameter input
    try:
        parameters = json.loads(args.params)
    except json.JSONDecodeError:
        logging.error("Invalid JSON format for parameters.")
        sys.exit(1)

    logging.info("Running Cypher query against Neo4j...")
    results = execute_query(
        uri=args.uri,
        username=args.username,
        password=args.password,
        query=query,
        params=parameters
    )

    if results:
        logging.info("Query results:")
        print(json.dumps(results, indent=2))
    else:
        logging.info("Query returned no results.")


if __name__ == "__main__":
    main()
