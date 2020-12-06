#!/bin/bash
mysqldump -Fc -v --column-statistics=0 -h castor-edc.mysql.database.azure.com -u bgarcial@castor-edc -p$1 -B edc-demo > edc-demo_backup.sql
