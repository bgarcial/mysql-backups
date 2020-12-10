# MySQL backups

1. Data Security and confidentiality. 
This means the solution needs to consider data encryption in transit and at rest.

2. Should be easy to restore a single database and/or a single table/row from a database.

So data security and a standard process for restoring backups on MySQL Azure and other hosting providers will be the scope of this solution.

## Solution

### 1. Data Security and confidentiality. 
The connection needs to be confidential, the data has to be protected anyway. 
As a general measure, a firewall on the database server is set up to only allow incoming connections from trusted IP addresses.

#### 1.1 Data encryption in transit.

The MySQL server should be deployed enforcing SSL connections and supporting TLS protocols to protect the transport of information between a client (a web application or in the case of this solution the different backup tools used) and a server (MySQL server either Azure or some hosting provider). It will make any kind of data unreadable.

- Prevent Tampering and eavesdropping by anyone on the network (prevent decoded the data stream)
With an unencrypted connection between the MySQL client and the server, someone with access to the network could watch all the traffic and inspect the data being sent or received between client and server

- Prevent from an attacker for seeing/altering the application content when sniffing between client and db server.
 
- To ensure to the client that he is connecting to the authentic server, and not a man-in-the-middle.

#### 1.2 Data encryption at rest.

In addition to encrypt incoming and outcoming connections the data also should be encrypted. 

Data-at-rest encryption takes place by encrypting the physical files of the database. So the data is encrypted when on disk.
In Azure, managed keys are referenced for data protection at rest.

- A Key Encryption Key is used and stored in Azure KeyVaults and it is used to encrypt a partition or blocks of data in MySQL Azure
- If an attacker obtains a hard drive with encrypted data but not the encryption keys ... 
    -  The attacker must defeat the encryption to read the data. 
    - This attack is much more complex and resource consuming than accessing unencrypted data on a hard drive. 

Reference: https://docs.microsoft.com/en-gb/azure/security/fundamentals/encryption-atrest

### 2. Standardize the process for restoring backups

Should be easy to restore a single database and/or a single table/row from a database on MySQL Azure and other hosting providers.

The backup process is done via an small pipeline from Github Actions either Azure Database for MySQL or MySQL hosting providers

For Azure MySQL, I will assume the following assumptions:
- A service principal is created with a subscription scope contributor role.
- An azure storage and a container are created


![](https://cldup.com/EEDy8ZRIK6.jpg)

Since this is a backup approach under mysql client tools perspective, this same workflow apply for restoring backups on MySQL hosting providers, removing only the service principal authentication part.


![](https://cldup.com/1b7Xdp3Tek.jpg)

- At this section, to upload a sql backup to a blob container, the pipeline will use a shared access signature to get access to the storage account for specific periods of time.

- Every backup file either `.sql` file or compressed files are uploaded as a blob containers.

- Azure storage accounts/blob containers by default are encrypted at rest.

![](https://cldup.com/E_SzIPaXsL.png)

![](https://cldup.com/AeIbS4UCxX.png)

- Secure transfer required was configured for the storage account, rejecting upload request from insecurity connnections.

![](https://cldup.com/uGV_HSzcRl.png)
