#!/bin/bash
# aws sqs send-message-batch --queue-url $1 --entries file://$2  > ./test.output
# echo -n Password:
# read -s $MYSQL_PASSWORD
#echo
mysqldump -Fc -v --column-statistics=0 -h castor-edc.mysql.database.azure.com -u bgarcial@castor-edc -p$1 -B edc-demo > edc-demo_backup.sql
#echo $MYSQL_PASSWORD
#-p "Password: " $1