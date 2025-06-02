# Neo4j Query Runner

A command-line tool to execute Cypher queries against a Neo4j database.

## Features

- Execute arbitrary Cypher queries from CLI
- Supports local and remote Neo4j instances

## Prerequisites

   - Python 3.6+
   - Neo4j Module: `pip install neo4j`


## Usage

```bash
python neo4j_query_runner.py [OPTIONS] "CYPHER_QUERY"
```

### Examples

1. **Basic query** (default credentials):
   ```bash
   python neo4j_query_runner.py "MATCH (n) RETURN n LIMIT 5"
   ```

2. **Custom credentials**:
   ```bash
   python neo4j_query_runner.py "MATCH (p:Person) RETURN p.name" -u admin -p secure123
   ```

3. **Remote Neo4j instance**:
   ```bash
   python neo4j_query_runner.py "CALL db.schema()" --uri bolt://production-db:7687
   ```

4. **Help menu**:
   ```bash
   python neo4j_query_runner.py -h
   ```

### Options
| Flag | Description | Default |
|------|-------------|---------|
| `-u`, `--username` | Database username | `neo4j` |
| `-p`, `--password` | Database password | `neo4j` |
| `--uri` | Neo4j connection URI | `bolt://localhost:7687` |


## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

# **Ethical Use Only**  

This tool is intended for **legal and authorized security assessments only**. By using this software, you agree to comply with all applicable laws and regulations.  

## **Legal Disclaimer**  
The developers of this tool are **not responsible** for any misuse or illegal activities conducted with it.

**Use responsibly and ethically.** Always obtain **written permission** before scanning third-party systems.  

---  
*By using this tool, you acknowledge that you understand and agree to these terms.*
