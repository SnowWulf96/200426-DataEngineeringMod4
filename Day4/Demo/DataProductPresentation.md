
Intro:
Our solution is a multi-part approach, including an Azure-Hosted Databricks instance, utilising medallion architecture, and a Python front end for users built in Flask, using Azure Entra ID to ensure access is controlled
Below we will cover a SWOT analysis of this approach, describe the solutions features and functions and detail the target user base. 


<img width="1180" height="521" alt="Screenshot 2026-04-23 145838" src="https://github.com/user-attachments/assets/5f4c86b3-9a09-4a61-a42d-13c245bdc5ad" />

Product Overview:
Data is ingested from multiple sources - This can be achieved in a number of ways depending on the source and the desired refresh. 
Databricks has a number of "Lakeflow" connectors to make this easy when dealing with common sources, such as ServiceNow.
If there isn't an existing connector, data can be ingested using custom notebook code to land this data into an Azure blob storage container. 
Where data needs to be constantly updated, Databricks supports streaming. If this isnt needed, batch updates are recommended to reduce cost. 

Once all data sources are ingested, we suggest taking a medallion architecture approach. This layer would be "Bronze", where raw data is stored, unaltered. 
From here data can be transformed where needed and moved to a Silver layer. 
PySpark notebooks can then be used to call the proprietery API and apply the changes to the data, then moving this on to "Gold", the data ready to be consumed by business users. 
<img width="951" height="535" alt="1746033137826" src="https://github.com/user-attachments/assets/aaf8fdc7-3a53-42f8-9292-683196cf6500" />

For the business users to access the data, we suggest building out a simple front-end application in Python, making use of the Flask package. 
This would allow the front end to be as simple as needed for non-technical business users.
Flask would then call the Databricks API to retrieve the data from our Gold layer, ready to present to the user. 

Flask also supports authentication in multiple forms. Our suggestion here is to stick with the Azure approach and make use of EntraID. 
Flask can be set up to utilise a Service Principal, and will query the data as needed (at regular intervals, on log-in, on clicking refresh etc). 
Utilisng an SVCP prevents exposing any users credentials and keeps things simple. However, that doesnt mean everyone needs to see the same data. 
Entra ID tokens can be taken from the user's login and passed to flask, to be used in the API call from flask. 
This would allow the creation of Role Based Access Control, or implementation of other security like row-level security or masking. 
This means that your users will only see what they should be seeing - the CIO can see it all, but less technical users dont get overwhelmed with everything. 


SWOT: 
Strengths:
- Unified Architecture: The Lakehouse model eliminates data silos by combining storage flexibility with warehouse-grade performance.
- Databricks can handle high-volume, real-time streaming (millisecond latency) or complex data transformations.
- Medallion architecture allows for data to be queried by technical staff at all levels of the journey if needed.
- Building out the front end bespoke means it can be as simple as needed.
- Doesnt have to be cloud-allgined, all tools are agnostic and solution could be applied to AWS, Azure or GCP

Weaknesses:
- Technical Complexity: Remains code-heavy, and will require in-house knowledge of the Flask app should the desire be to maintain this in-house 
- Performance "Bill Shock": Without strict governance (e.g., Unity Catalog), inefficient jobs and idle clusters can lead to unpredictable cloud costs.
- Multi-part - more powerful than say a Databricks Dashboard, but more parts means more troubleshooting if issues arise. 

Opportunities:
- Databricks offers powerful Machine Learning capabilities to expand in to 
- Flask app can be built out to the companies desire, growing as is seen fit. 

Threats:
- Direct Competitors: Databricks see pressure from Snowflake, which is aggressively adding AI and unstructured data capabilities to its warehouse-first model.
-

Market Analysis: 
Databricks current biggest comeptitor is Snowflake.
- Snowflake is another cloud-native data warehousing/lakehouse solution. Snowflake offers similar strong SQL analytics, governance and data sharing capabilities as Databricks does. 
- Snowflake is often seen as simpler and more business-user friendly, taking a SQL first approach, where Databricks offers much more powerful tools utilising spark-native open formats such as Delta, which are often more useful for ML/AI
- Tools such as Power BI and Tableau exist for visualisations of data, and are arguabley more common names and tools users may already be aware of, however
- ReTool connects to Databricks using SQL, and can build pages with tables, charts etc. Strong for interal portals, however doesnt have the strength of scalability which a Databricks soltuion does. 

