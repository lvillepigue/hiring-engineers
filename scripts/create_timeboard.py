#! /usr/bin/python
from datadog import initialize

options = {
    'api_key':'ffab323179a991d3dcd567a7104a32b3',
    'app_key':'f4ac87aacccf4a2989e9b32addafce1021b75ce1'
}

initialize(**options)

# Use Datadog REST API client
from datadog import api

title = "My Timeboard"
description = "Timeboard created using the Python API"
graphs = [
{
	"title": "Custom random metric",
	"definition": { 
		"requests": [
		{
			"q": "avg:my_metric{host:ubuntu-bionic}"
		}
	]
	}	
},
{
	"title": "MySQL CPU time with anomalies",
	"definition": { 
		"requests": [
		{
			"q": "anomalies(avg:mysql.performance.cpu_time{*}, 'basic', 2)"
		}
	]
	}	
},
{
	"title": "Custom random metric with rollup function",
	"definition": { 
		"requests": [
		{
			"q": "my_metric{host:ubuntu-bionic}.rollup(sum,3600)"
		}
	]
	}	
}
]

template_variables = []

print(api.Timeboard.create(title=title, description=description,graphs=graphs, template_variables=template_variables, read_only = True))
