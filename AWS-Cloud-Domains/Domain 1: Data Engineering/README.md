# Domain 1.1: Create data repositories for machine learning

The whole field of ML revolves around data. With clean data, you can gain important business insights. Data allows you to be proactive rather than reactive in making strategic business decisions, and helps you understand your customers at a deeper level.

But...storing all of this data is challenging

Transctional, Database, Clickstream, IoT and sensors, Server, Disk, Multimedia,Social media.

Data lake as a key solution to this challenge
With a data lake, you can store structured and unstructured data

AWS Lake Formation and Amazon S3:
AWS Lake Formation is your data lake solution, and Amazon S3 is the preferred storage option for data science processing on AWS
Image of AWS Lake Formation as your AWS data lake solution and of Amazon S3 as your data lake storage option.

More on Amazon S3

Use Amazon S3 storage classes to reduce the cost of data storage. 

Frequent -> Infrequent
S3 Standard: Frequently accessed data
S3 Intelligent-Tiering : For Data with changing access patterns.
S3 Standard-IA : For Infrequntly accessed data.
S3 1Z-1A: For re-creatable, less accessed data.
Amazon Glacier : Archieve data.

However, Amazon S3 isn't your only storage solution for model training.

AWS Lake Formation:
With Lake Formation, you can move, store, catalog, and clean your data faster. You simply point Lake Formation at your data sources, and Lake Formation crawls those sources and moves the data into your new Amazon S3 data lake. Lake Formation organizes data in S3 around frequently used query terms and into right-sized chunks to increase efficiency. Lake Formation also changes data into formats like Apache Parquet and ORC for faster analytics. In addition, Lake Formation has built-in machine learning to deduplicate and find matching records (two entries that refer to the same thing) to increase data quality.

Amazon S3 with Amazon SageMaker: 
You can use Amazon S3 while you’re training your ML models with Amazon SageMaker. Amazon S3 is integrated with Amazon SageMaker to store your training data and model training output.

Amazon S3 with Amazon EFS:
Alternatively, if your training data is already in Amazon Elastic File System (Amazon EFS), we recommend using that as your training data source. Amazon EFS has the benefit of directly launching your training jobs from the service without the need for data movement, resulting in faster training start times. This is often the case in environments where data scientists have home directories in Amazon EFS and are quickly iterating on their models by bringing in new data, sharing data with colleagues, and experimenting with including different fields or labels in their dataset. For example, a data scientist can use a Jupyter notebook to do initial cleansing on a training set, launch a training job from Amazon SageMaker, then use their notebook to drop a column and re-launch the training job, comparing the resulting models to see which works better.

Amazon FSx for Lustre:
When your training data is already in Amazon S3 and you plan to run training jobs several times using different algorithms and parameters, consider using Amazon FSx for Lustre, a file system service. FSx for Lustre speeds up your training jobs by serving your Amazon S3 data to Amazon SageMaker at high speeds. The first time you run a training job, FSx for Lustre automatically copies data from Amazon S3 and makes it available to Amazon SageMaker. You can use the same Amazon FSx file system for subsequent iterations of training jobs, preventing repeated downloads of common Amazon S3 objects.


Domain 1.2: Identify and implement a data ingestion solution

To use this data for ML, you need to ingest it into a service like Amazon S3

One of the core benefits of a data lake solution is the ability to quickly and easily ingest multiple types of data. In some cases, your data will reside outside your Amazon S3 data lake solution, in databases, on-premises storage platforms, data warehouses, and other locations. To use this data for ML, you may need to ingest it into a storage service like Amazon S3.

Batch and stream processing are two kinds of data ingestion

Batch processing
Batch processing periodically collects and groups source data
With batch processing, the ingestion layer periodically collects and groups source data and sends it to a destination like Amazon S3. You can process groups based on any logical ordering, the activation of certain conditions, or a simple schedule. Batch processing is typically used when there is no real need for real-time or near-real-time data, because it is generally easier and more affordably implemented than other ingestion options.


Several services can help with batch processing into the AWS Cloud
For batch ingestions to the AWS Cloud, you can use services like AWS Glue, an ETL (extract, transform, and load) service that you can use to categorize your data, clean it, enrich it, and move it between various data stores. AWS Database Migration Service (AWS DMS) is another service to help with batch ingestions. This service reads from historical data from source systems, such as relational database management systems, data warehouses, and NoSQL databases, at any desired interval. You can also automate various ETL tasks that involve complex workflows by using AWS Step Functions.

Stream processing
Stream processing manipulates and loads data as it’s recognized
Stream processing, which includes real-time processing, involves no grouping at all. Data is sourced, manipulated, and loaded as soon as it is created or recognized by the data ingestion layer. This kind of ingestion is less cost-effective, since it requires systems to constantly monitor sources and accept new information. But you might want to use it for real-time predictions using an Amazon SageMaker endpoint that you want to show your customers on your website or some real-time analytics that require continually refreshed data, like real-time dashboards.

Amazon Kinesis is a platform for streaming data on AWS

AWS recommends that you capture and ingest this fast-moving data using Amazon Kinesis, a platform for streaming data on AWS. Amazon Kinesis gives you the opportunity to build custom streaming data applications for specialized needs, and it offers several services focused on making it easier to load and analyze your streaming data.

Amazon Kinesis Video Streams: Amazon Kinesis Video Streams provides SDKs that make it easy for devices to securely stream media to AWS for playback, storage, analytics, machine learning, and other processing. Kinesis Video Streams can ingest data from edge devices, smartphones, security cameras, and other data sources such as RADARs, LIDARs, drones, satellites, dash cams, and depth-sensors.
Amazon Kinesis Data Streams: Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events. The data collected is available in milliseconds to enable real-time analytics use cases such as real-time dashboards, real-time anomaly detection, dynamic pricing, and more.

Amazon Kinesis Data Firehose: Amazon Kinesis Data Firehose provides a simple way to capture, transform, and load streaming data with just a few clicks in the AWS Management Console. You can quickly create a Firehose delivery stream, select the destinations, and start sending real-time data from hundreds of thousands of data sources simultaneously. The service takes care of stream management, including all the scaling, sharding, and monitoring needed to continuously load the data to destinations at the intervals you specify.

Amazon Kinesis Data Analytics: Amazon Kinesis Data Analytics provides built-in functions to filter, aggregate, and transform streaming data for advanced analytics. It processes streaming data with sub-second latencies, enabling you to analyze and respond to incoming data and events in real time.

AWS Glue : AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics. You can create and run an ETL job with a few clicks in the AWS Management Console. ... Once cataloged, your data is immediately searchable, queryable, and available for ETL.

Apache Kafka: Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.

Domain 1.3: Identify and implement a data transformation solution
Raw ingested data is not ML ready
The raw data ingested into a service like Amazon S3 is usually not ML ready as is. The data needs to be transformed and cleaned, which includes deduplication, incomplete data management, and attribute standardization. Data transformation can also involve changing the data structures, if necessary, usually into an OLAP model to facilitate easy querying of data. 

Doing this in the context of ML, while using key services that help you with data transformation, is the focus of this subdomain.

Transforming your data for ML:
Data transformation is often necessary to deal with huge amounts of data. Distributed computation frameworks like MapReduce and Apache Spark provide a protocol of data processing and node task distribution and management. They also use algorithms to split datasets into subsets and distribute them across nodes in a compute cluster.

Using Apache Spark on Amazon EMR provides a managed framework
Using Apache Spark on Amazon EMR provides a managed framework that can process massive quantities of data. Amazon EMR supports many instance types that have proportionally high CPU with increased network performance, which is well suited for HPC (high-performance computing) applications.

A key step in data transformation for ML is partitioning your dataset:
Datasets required for ML applications are often pulled from database warehouses, streaming IoT input, or centralized data lakes. In many use cases, you can use Amazon S3 as a target endpoint for their training datasets. ETL processing services (Amazon Athena, AWS Glue, Amazon Redshift Spectrum) are functionally complementary and can be built to preprocess datasets stored in or targeted to Amazon S3. In addition to transforming data with services like Athena and Amazon Redshift Spectrum, you can use services like AWS Glue to provide metadata discovery and management features. The choice of ETL processing tool is also largely dictated by the type of data you have. For example, tabular data processing with Athena lets you manipulate your data files in Amazon S3 using SQL. If your datasets or computations are not optimally compatible with SQL, you can use AWS Glue to seamlessly run Spark jobs (Scala and Python support) on data stored in your Amazon S3 buckets.

You can store a single source of data in Amazon S3 and perform adhoc analysis:
This reference architecture shows how AWS services for big data and ML can help build a scalable analytical layer for healthcare data. Customers can store a single source of data in Amazon S3 and perform ad hoc analysis with Athena, integrate with a data warehouse on Amazon Redshift, build a visual dashboard for metrics using Amazon QuickSight, and build an ML model to predict readmissions using Amazon SageMaker. By not moving the data around and connecting to it using different services, customers avoid building redundant copies of the same data.

Apache Spark on Amazon EMR : Amazon EMR is the best place to run Apache Spark. You can quickly and easily create managed Spark clusters from the AWS Management Console, AWS CLI, or the Amazon EMR API

Apache Spark and Amazon SageMaker : SageMaker provides an Apache Spark library, in both Python and Scala, that you can use to easily train models in SageMaker using org.apache.spark.sql.

References: docs.aws.amazon.com

