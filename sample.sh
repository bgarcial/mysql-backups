#!/bin/bash
#read -sp MYSQL_PASSWORD
# mysqldump -Fc -v --column-statistics=0 -h castor-edc.mysql.database.azure.com -u bgarcial@castor-edc -p"${MYSQL_PASSWORD}" -B edc-demo > test.sql
mysqldump -Fc -v -h castor-edc.mysql.database.azure.com -u bgarcial@castor-edc -p$1 -B edc-demo > test.sql
