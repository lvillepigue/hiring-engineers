Your answers to the questions go here.

# What is DataDog?

???

## DataDog's features

???


## Installing DataDog for your environment
Let's say you are running a MySQL server on an Ubuntu server you would like to monitor

### 1. Prerequisites - Setup the environment

![Installing on Ubuntu](screenshots/InstallingOnUbuntuDDPage.PNG)


![Install agent command line](screenshots/InstallAgentCommandLine.PNG)

To edit the agent configuration file
sudo -u dd-agent vi /etc/datadog-agent/datadog.yaml


### 2. Collecting Metrics

![Editing datadog.yaml](screenshots/datadog.yaml.PNG)

[datadog.yaml](etc/datadog-agent/datadog.yaml)


Host map with tags
![Host map with tags](screenshots/HostMapWithTags.PNG)


Installation of a MySQL database on Ubuntu:
```
sudo apt-get install mysql-server
```

The instructions the links below show how to 

- create a datadog MySQL user and password
- enable replicate




https://docs.datadoghq.com/integrations/mysql/
or if logged in to the DataDog website
https://app.datadoghq.com/account/settings#integrations/mysql




The integration for MySQL comes with the DataDog agent. We only need to copy the example file
```
/etc/datadog-agent/conf.d/mysql.d
sudo -u dd-agent cp conf.yaml.example conf.yaml
sudo -u dd-agent vi conf.yaml
```

Uncomment the entries in the red rectangles then 
- replace user and password with the relevant entries
- use tags relevant to the MySQL server. Here hrdatabase1 and plant6
- set options
    - set replication to 0
    - set galera_cluster to 1


![MySQL integration configuration](screenshots/MysqlIntegrationConfigYaml.PNG)


#### Create a custom agent check

An agent check can be written in Python. Documentation is [here](https://docs.datadoghq.com/developers/agent_checks/).
It is a class with a check method with a parameter of type AgentCheck. the AgentCheck package needs to be imported. 
Please find source of the [my_metric_check.py](etc/datadog-agent/checks.d/my_metric_check.py) file below
```
from checks import AgentCheck
import random
class HelloCheck(AgentCheck):
    def check(self, instance):
        self.gauge('my_metric', random.randint(0,1001))
```
For the DataDog agent to find it a corresponding .yaml file with the same name ([my_metric_check.yaml](etc/datadog-agent/conf.d/my_metric_check.yaml)) need to be written in the /etc/datadog-agent/conf.d folder. The *min_collection_interval* parameter for the instance determines how often the check python file is called by the DataDog agent so there is no need to modify the Python check file (answer to the bonus question).
```
init_config:

instances:
    - url: http://localhost
      min_collection_interval: 45
```

Restart the DataDog agent so it reads the new *my_metric_check.yaml* file
```
sudo systemctl restart datadog-agent
```


### 3. Visualizing Data
#### Create a new Timeboard using the DataDog API
To make calls to the API both an API key and an application Key are required. We so far have an API key. To the find the documentation about creating these keys, we navigate to the DataDog Docs Authentication section and click on the link [Manage your account’s API and application keys] (https://app.datadoghq.com/account/settings#api). As we are using the MySQL database, we use 'mysql' as the App key name


3 steps

1. install the Python DataDog API from the command line 
```pip install datadog```

2. write the [create_timeboard.py](scripts/create_timeboard.py) script

3. run the script ```python create_timeboard.py```


???


### 4. Monitoring Data
Create a metric monitor on my_metric

https://docs.datadoghq.com/monitors/monitor_types/metric/
https://docs.datadoghq.com/monitors/notifications/


curl "https://api.datadoghq.com/api/v1/dash?api_key=ffab323179a991d3dcd567a7104a32b3&application_key=f4ac87aacccf4a2989e9b32addafce1021b75ce1"


[Issues encountered](issues.md)