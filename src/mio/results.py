# Copyright 2022 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################


import mio.cfg
import mio.clean
import mio.cmp
import mio.cov
import mio.dox
import mio.elab
import mio.history
import mio.sim
import mio.vivado

import yaml
from yaml.loader import SafeLoader
import os
import jinja2
from jinja2 import Template
import xml.etree.cElementTree as ET
from datetime import datetime
import re


uvm_warning_regex = "UVM_WARNING(?! \: )"
uvm_error_regex   = "UVM_ERROR(?! \: )"
uvm_fatal_regex   = "UVM_FATAL(?! \: )"



html_report_template = Template("""
<!doctype html>
<html lang="en">
<head title="{{ testsuites.name }}">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.min.js" integrity="sha384-PsUw7Xwds7x08Ew3exXhqzbhuEYmA2xnwc8BuD6SEr+UmEHlX8/MCltYEodzWA4u" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" integrity="sha384-uWxY/CJNBR+1zjPWmfnSnVxwRheevXITnMqoEIeG1LJrdI0GlVs/9cVSyPYXdcSF" crossorigin="anonymous">
</head>
<body>
{% if testsuites.passed %}
<h1>Simulation Test Results for {{ testsuites.name }} - <span style="font-weight: bold;">{{ testsuites.failures }} Failures</span> ({{ testsuites.timestamp }})</h1>
{% else %}
<h1>Simulation Test Results for {{ testsuites.name }} - <span style="font-weight: bold; color: red;">{{ testsuites.failures }} Failures</span> ({{ testsuites.timestamp }})</h1>
{% endif %}
{% for suite in testsuites.suites %}
<div style="padding: 10px; background-color: #EEEEEE;">
<h2>{{ suite.name }} - {{ suite.num_tests }} tests</h2>
<h3><span style="color: red;">{{ suite.failures }} failing</span> - <span style="color: green;">{{ suite.passing }} passing</span></h3>
<table class="table table-hover table-condensed" style="background-color: white;">
<thead>
<tr>
<th>#</th>
<th>Name</th>
<th>Seed</th>
<th>#Warnings</th>
<th>#Errors</th>
<th>Duration (sec)</th>
<th>Result</th>
</tr>
</thead>
<tbody>
{% for test in suite.tests %}
{% if test.passed %}
<tr>
{% else %}
<tr class="danger">
{% endif %}
<th>{{ test.index }}</th>
<td>{{ test.name }}</td>
<td>{{ test.seed }}</td>
<td>{{ test.num_warnings }}</td>
<td>{{ test.num_errors }}</td>
<td>{{ test.time }}</td>
<td>{{ test.conclusion }}</td>
</tr>
{% endfor %}
</tbody>
</table>
</div>
{% endfor %}
</body>
</html>
""")




def do_parse_results(snapshot, filename):
    test_count = 0
    failure_count = 0
    total_duration = 0
    
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M:%S")
    
    testsuites = ET.Element("testsuites")
    testsuites.set('id', timestamp)
    testsuites.set('name', snapshot)
    testsuite = ET.SubElement(testsuites, "testsuite")
    testsuite.set('id', timestamp)
    testsuite.set('name', "functional")
    
    suite_model = {}
    suite_model['id'] = timestamp
    suite_model['name'] = 'Functional'
    suite_model['tests'] = []
    results_model = {}
    results_model['testsuites'] = {}
    results_model['testsuites']['suites'] = []
    results_model['testsuites']['name'] = snapshot
    results_model['testsuites']['timestamp'] = timestamp
    results_model['testsuites']['suites'].append(suite_model)
    
    print("Parsing results ...")
    if not os.path.exists(cfg.history_file_path):
        sys.exit("No history log file")
    else:
        with open(cfg.history_file_path,'r') as yamlfile:
            cur_yaml = yaml.load(yamlfile, Loader=SafeLoader)
            if cur_yaml:
                for sim in cur_yaml[snapshot]['simulations']:
                    sim_log_path = sim + "/sim.log"
                    duration = int(cur_yaml[snapshot]['simulations'][sim]['duration'])
                    total_duration = total_duration + duration
                    
                    testcase = ET.SubElement(testsuite, "testcase")
                    testcase.set('id', snapshot + "." + cur_yaml[snapshot]['simulations'][sim]['test_name'])
                    testcase.set('name', cur_yaml[snapshot]['simulations'][sim]['test_name'])
                    testcase.set('time', str(duration))
                    testcase.set('seed', str(cur_yaml[snapshot]['simulations'][sim]['seed']))
                    
                    testcase_model = {}
                    suite_model['tests'].append(testcase_model)
                    testcase_model['name'] = cur_yaml[snapshot]['simulations'][sim]['test_name']
                    testcase_model['seed'] = cur_yaml[snapshot]['simulations'][sim]['seed']
                    testcase_model['time'] = duration
                    testcase_model['index'] = test_count
                    
                    args = ET.SubElement(testcase, "args")
                    testcase_model['args'] = []
                    for arg in cur_yaml[snapshot]['simulations'][sim]['args']:
                        arg_e = ET.SubElement(args, "arg")
                        arg_e.text = arg
                        testcase_model['args'].append(arg)
                    
                    passed = sim_parse_sim_results(sim_log_path, testcase, testcase_model)
                    if passed == "failed" or passed == "inconclusive":
                        failure_count = failure_count + 1
                        testcase_model['passed'] = False
                    else:
                        testcase_model['passed'] = True
                    test_count = test_count + 1
                    
        testsuites.set('tests', str(test_count))
        testsuites.set('failures', str(failure_count))
        testsuites.set('time', str(total_duration))
        testsuite.set('tests', str(test_count))
        testsuite.set('failures', str(failure_count))
        testsuite.set('time', str(total_duration))
        tree = ET.ElementTree(testsuites)
        tree.write(filename + ".xml")
        
        suite_model['num_tests'] = test_count
        suite_model['failures'] = failure_count
        suite_model['passing'] = test_count - failure_count
        suite_model['time'] = total_duration
        results_model['testsuites']['failures'] = failure_count
        if failure_count > 0:
            results_model['testsuites']['passed'] = False
        else:
            results_model['testsuites']['passed'] = True
        html_report_contents = html_report_template.render(testsuites=results_model['testsuites'])
        with open(filename + ".html",'w') as htmlfile:
            htmlfile.write(html_report_contents)
        htmlfile.close()






def sim_parse_sim_results(sim_log_path, testcase, testcase_model):
    test_result = "passed"
    num_warnings=0
    num_errors = 0
    num_fatals=0
    if not os.path.exists(cfg.history_file_path):
        print("No sim log file " + sim_log_path)
        test_result = "inconclusive"
    else:
        for i, line in enumerate(open(sim_log_path)):
            matches = re.search(uvm_warning_regex, line)
            if matches:
                num_warnings = num_warnings + 1
            matches = re.search(uvm_error_regex, line)
            if matches:
                failure = ET.SubElement(testcase, "failure")
                failure.set("message", line)
                failure.set("type", "ERROR")
                test_result = "failed"
                num_errors = num_errors + 1
            matches = re.search(uvm_fatal_regex, line)
            if matches:
                failure = ET.SubElement(testcase, "failure")
                failure.set("message", line)
                failure.set("type", "FATAL")
                test_result = "failed"
                num_fatals = num_errors + 1
    
    testcase.set("warnings", str(num_warnings))
    testcase.set("errors", str(num_errors))
    testcase.set("fatals", str(num_fatals))
    testcase_model['num_warnings'] = num_warnings
    testcase_model['num_errors'] = num_errors
    testcase_model['num_fatals'] = num_fatals
    testcase_model['conclusion'] = test_result
    return test_result
