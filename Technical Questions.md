# Technical Questions
## A user is attempting to access a resource at a specific api endpoint.
The server response has a status code of `403 Forbidden`.
The user is asking us what's wrong, what would your initial thoughts/response be?
### Responses
1. The user have no permissions. The server may be configured to restrict access based on user roles or permissions settings.
2. The IP is blacklisted. Sometimes, access might be restricted based on IP addresses.

I tell him has a valid credentials, maybe has no permissions to access this resource,
server may be configured to restrict access based on user roles, group, or other
authorization settings.

## We have a Postgres table that is getting too big and queries are slowing down significantly.
What are some steps we could take to optimize this table?
### Responses
1. Indexing. Indexes are used to quickly locate data without having to search every row in a database table every time said table is accessed.
2. Partitioning. Data is divided into partitions that can be managed and accessed separately.
3. Optimize data types. Using smaller data types where possible can reduce storage requirements and improve query performance.

## Users are allowed to upload ads through our api. Ads require additional processing, such as compression, harvesting metadata, etc. 
How would you handle time consuming processing of large media files through a RESTful api?
### Responses
1. Asynchronous processing. Instead of processing the media files synchronously within the API request-response cycle, offload the processing to background workers or a separate service.
2. Job queue. Implement a job queue system where each uploaded media file corresponds to a job.
3. Worker nodes. Have one or more worker nodes continuously monitoring the job queue.