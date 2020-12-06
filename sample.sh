#!/bin/bash
mysqldump -Fc -v -h castor-edc.mysql.database.azure.com -u bgarcial@castor-edc -p$1 -B edc-demo > edc-demo_backup.sql
# Uploading sql file
az storage blob upload \
    --account-name mysqlbackups007 \
    --container-name database-backups \
    --name edc-demo_backup.sql \
    --file edc-demo_backup.sql \
    --auth-mode login
# mysqldump -Fc -v --column-statistics=0 -h castor-edc.mysql.database.azure.com -u bgarcial@castor-edc -p$1 -B edc-demo > edc-demo_backup.sql
