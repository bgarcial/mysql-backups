# The problem: MySQL backups

We store almost all our application data in MySQL. For our core product, EDC, every study actually receives its own database schema, which means on our biggest install we have about 25,000 databases (about 1 TiB of data) in a single MySQL server.
Our SLA promises customers that we make backups twice a day and that we keep these backups for 30 days. It also promises an additional monthly backup that is stored for 1 year.
Historically, because we have been growing on a mixed set of different hosting providers, we've used different backup tools for the different environments. We would like to standardize on one single implementation that we can use everywhere, so that the process for restoring backups can be the same everywhere.
We'd like you to design a solution to this, keeping these constraints in mind:
We still use a mix of Azure and managed hosting providers, so we cannot pick a technology which only works on Azure.
Security and confidentiality of this data is critical. This means data will need to be encrypted both in transit and at rest.
It needs to be easy for us to restore a single database (or even a single table/row from a database), as opposed to restoring all the databases for an entire server. This is because we don't use this for disaster recovery primarily, but mostly to restore data for a single study when a customer accidentally messes up their data and comes to us asking if we can restore a backup from a few days ago.
Our EDC application architecture means that we have many (thousands) of databases. With tools used in the past, we’ve seen that backing all of them up sequentially takes between 1-3 days.



IDENTIFY THE PROBLEM LIKE OTHER DOCS 

DOCUMENT STUFF I DID 

CHECK FOR BENEFITS SSL CONNECTIONS
https://tableplus.com/blog/2018/08/why-using-ssl-is-a-must-for-production-database-connection.html