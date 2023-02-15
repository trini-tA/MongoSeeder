#!/bin/bash
docker exec mongoseeder_mongodb sh -c 'exec mongodump --db bulk_example --gzip --archive' > dumps/dump_`date "+%Y-%m-%d"`.gz

# docker exec mongoseeder_mongodb sh -c 'exec mongorestore --archive < ./dumps/dump_2023-02-15'
